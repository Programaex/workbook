#!/usr/bin/env python3
"""Utilitário do workbook: status | index | check | build.

Uso: python3 500_Copiloto_templates/scripts/workbook.py <comando> [--incluir-vazios]
"""
import csv, re, sys, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[2]
WB = ROOT / "00_Workbook"
SCORE = {"empty": 0, "draft": 33, "review": 66, "done": 100}
FRONT = ["00_capa.md", "01_indice.md", "02_sumario-executivo.md", "03_escopo-e-metodo.md"]
ID_RE = re.compile(r"^(EP|PJ|IS|SI)-([A-Z]{2}\.[A-Z]{3})-(\d{4})$")
OPEN_STATES = {"backlog", "todo", "doing", "blocked"}


def fm(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    data = {}
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep:
                data[k.strip()] = v.strip().strip('"')
    return data


def areas():
    with open(ROOT / "OWNERS.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def area_dir(a):
    return ROOT / a["path"].rstrip("/")


def chapter_dir(a):
    return WB / "capitulos" / a["path"].rstrip("/")


def sections(a):
    return sorted(chapter_dir(a).glob("S[0-9][0-9]_*.md"))


def tasks(a):
    d = area_dir(a) / "tarefas"
    return sorted(p for p in d.glob("*.md") if p.name != "README.md") if d.exists() else []


def area_state(a):
    st = [fm(p).get("status", "empty") for p in sections(a)]
    pct = round(sum(SCORE.get(s, 0) for s in st) / len(st)) if st else 0
    open_tasks = sum(1 for p in tasks(a) if fm(p).get("status") in OPEN_STATES)
    if all(s == "empty" for s in st):
        state = "nao_iniciada"
    elif all(s == "done" for s in st) and open_tasks == 0 and a["person"]:
        state = "concluida"
    elif all(s in ("review", "done") for s in st):
        state = "em_revisao"
    else:
        state = "em_andamento"
    return pct, state, open_tasks, len(st)


def cmd_status():
    rows, pcts = [], []
    for a in areas():
        pct, state, ot, n = area_state(a)
        pcts.append(pct)
        rows.append([a["area_id"], a["owner_code"], a["person"] or "", n, pct, state, ot])
    front = [SCORE.get(fm(WB / f).get("status", "empty"), 0) for f in FRONT]
    overall = round(0.8 * sum(pcts) / len(pcts) + 0.2 * sum(front) / len(front))
    all_done = all(r[5] == "concluida" for r in rows) and all(x == 100 for x in front)
    out = WB / "_controle" / "COMPLETUDE.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["area_id", "owner", "pessoa", "secoes", "completude_pct", "estado", "tarefas_abertas"])
        w.writerows(rows)
        w.writerow(["WORKBOOK", "", "", "", overall, "concluido" if all_done else "em_andamento", ""])
    for r in rows:
        print(f"{r[0]} {r[1]:7} {r[4]:>3}%  {r[5]:13} tarefas_abertas={r[6]}")
    print(f"WORKBOOK {overall}% {'concluido' if all_done else 'em_andamento'}  (gerado em {out.relative_to(ROOT)})")


def cmd_index():
    lines = []
    for f in FRONT[2:]:
        t = fm(WB / f).get("title", f)
        lines.append(f"- {t} — `{f}`")
    for a in areas():
        ch = chapter_dir(a)
        t = fm(ch / "00_capitulo.md").get("title", a["area_name"])
        lines.append(f"- **{a['area_id']} · {t}** — owner `{a['owner_code']}`")
        for s in sections(a):
            m = fm(s)
            lines.append(f"  - {m.get('id','')} · {m.get('title', s.stem)} _({m.get('status','empty')})_")
    block = "<!-- INDICE:INICIO -->\n" + "\n".join(lines) + "\n<!-- INDICE:FIM -->"
    p = WB / "01_indice.md"
    txt = p.read_text(encoding="utf-8")
    txt = re.sub(r"<!-- INDICE:INICIO -->.*?<!-- INDICE:FIM -->", lambda _: block, txt, flags=re.S)
    p.write_text(txt, encoding="utf-8")
    print("índice atualizado")


def cmd_check():
    errs = []
    for a in areas():
        for p in tasks(a):
            m = fm(p)
            tid = m.get("id", "")
            g = ID_RE.match(tid)
            if not g:
                errs.append(f"{p}: id inválido '{tid}'"); continue
            if p.stem != tid:
                errs.append(f"{p}: nome do arquivo difere do id")
            if g.group(2) != a["owner_code"]:
                errs.append(f"{p}: owner do id difere do owner da área {a['owner_code']}")
            if g.group(3) != str(m.get("github_number", "")).zfill(4):
                errs.append(f"{p}: número do id difere de github_number")
            if not m.get("github_url", "").startswith("https://github.com/"):
                errs.append(f"{p}: clone 1 ausente (github_url)")
            if m.get("type") == "subissue" and not m.get("parent"):
                errs.append(f"{p}: sub-issue sem parent")
            if not (WB / "anexos" / "C_registro-de-tarefas" / f"{tid}.md").exists():
                errs.append(f"{p}: clone 3 ausente no workbook")
    for p in (WB / "anexos" / "C_registro-de-tarefas").glob("*.md"):
        if p.name == "README.md":
            continue
        if not any((area_dir(a) / "tarefas" / p.name).exists() for a in areas()):
            errs.append(f"{p}: clone 3 sem clone 2 na pasta do owner")
    print("\n".join(errs) if errs else "check ok")
    sys.exit(1 if errs else 0)


def cmd_build(incl_empty):
    parts = []
    for f in FRONT:
        parts.append(re.sub(r"^---\n.*?\n---\n", "", (WB / f).read_text(encoding="utf-8"), flags=re.S))
    for a in areas():
        ch = chapter_dir(a)
        parts.append(re.sub(r"^---\n.*?\n---\n", "", (ch / "00_capitulo.md").read_text(encoding="utf-8"), flags=re.S))
        for s in sections(a):
            if fm(s).get("status", "empty") == "empty" and not incl_empty:
                continue
            parts.append(re.sub(r"^---\n.*?\n---\n", "", s.read_text(encoding="utf-8"), flags=re.S))
    out = WB / "_build" / "relatorio.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n\n\\newpage\n\n".join(parts), encoding="utf-8")
    print(f"gerado {out.relative_to(ROOT)} ({datetime.date.today()})")


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else ""
    {"status": cmd_status, "index": cmd_index, "check": cmd_check,
     "build": lambda: cmd_build("--incluir-vazios" in sys.argv)}.get(c, lambda: print(__doc__))()
