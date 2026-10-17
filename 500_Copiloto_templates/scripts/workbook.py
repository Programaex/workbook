#!/usr/bin/env python3
"""Utilitário do workbook (ADR-001): status | index | check | build.

Uso: python3 500_Copiloto_templates/scripts/workbook.py <comando> [opções]
  status                         completude por workbook A## → 00_Workbook/_controle/COMPLETUDE.csv
  index                          regenera o Index do Workbook Geral e de cada workbook
  check                          valida contrato, paginação, fichas, rotas, tarefas e checksums
  build [--escopo GERAL|A##|A##-M##] [--incluir-vazios]
                                 monta o relatório A4 em 00_Workbook/_build/
"""
import csv, json, re, sys, pathlib, hashlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
WB = ROOT / "00_Workbook"
REG = WB / "registros"
SCORE = {"empty": 0, "draft": 33, "review": 66, "done": 100}
ID_RE = re.compile(r"^(EP|PJ|IS|SI)-([A-Z]{2}\.[A-Z]{3})-(\d{4})$")
OPEN_STATES = {"backlog", "todo", "doing", "blocked"}
PAGE, CONT = "<!-- page -->", "<!-- page continuation -->"
FIXED = [("00_capa.md", "cover", 1), ("01_index.md", "index", 1), ("02_overview.md", "overview", 3)]
CYCLE = [("conteudo.md", "content", None), ("notas.md", "notes", 3), ("tarefas.md", "tasks", 2)]
LAYOUT = {"cover_pages": 1, "index_pages": 1, "overview_pages": 3, "content_pages": "unlimited",
          "notes_pages": 3, "tasks_pages": 2, "repeat_scope": "module"}
WB_KEYS = ["id", "title", "area_id", "subarea_id", "owner_role", "owner_person", "status", "version",
           "parent_workbook_id", "source_refs", "related_workbook_ids", "route_refs", "layout", "references", "export"]
INDEX_LINES_PER_PAGE = 40


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


def body(path):
    return re.sub(r"^---\n.*?\n---\n", "", path.read_text(encoding="utf-8"), flags=re.S)


def pages(path):
    lines = [l.strip() for l in body(path).splitlines()]
    return lines.count(PAGE), lines.count(CONT)


def rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def macroareas():
    return rows(ROOT / "MACROAREAS.csv")


def wb_dir(m):
    return ROOT / m["path"].rstrip("/")


def load_yaml(p):
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def modules(d):
    meta = load_yaml(d / "workbook.yaml").get("workbook", {})
    return [(mod["id"], d / mod["path"].rstrip("/"), mod.get("title", "")) for mod in meta.get("modules") or []]


def blocks(d):
    """Lista ordenada (arquivo, tipo, páginas_fixas) do workbook em d."""
    out = [(d / f, t, n) for f, t, n in FIXED]
    for _, md, _ in modules(d):
        out += [(md / f, t, n) for f, t, n in CYCLE]
    return out


def area_dirs():
    return [(m, wb_dir(m)) for m in macroareas()]


# ------------------------------------------------------------------ status
def wb_state(d):
    st = [fm(p).get("status", "empty") for p, _, _ in blocks(d) if p.exists()]
    pct = round(sum(SCORE.get(s, 0) for s in st) / len(st)) if st else 0
    if all(s == "empty" for s in st):
        state = "nao_iniciado"
    elif all(s == "done" for s in st):
        state = "concluido"
    elif all(s in ("review", "done") for s in st):
        state = "em_revisao"
    else:
        state = "em_andamento"
    return pct, state, len(modules(d))


def cmd_status():
    out_rows, pcts = [], []
    for m, d in area_dirs():
        pct, state, nm = wb_state(d)
        pcts.append(pct)
        out_rows.append([m["workbook_id"], m["macroarea_id"], m["owner_code"], m["owner_pessoa"], nm, pct, state])
    gen = [SCORE.get(fm(WB / f).get("status", "empty"), 0) for f, _, _ in FIXED]
    overall = round(0.8 * sum(pcts) / len(pcts) + 0.2 * sum(gen) / len(gen))
    done = all(r[6] == "concluido" for r in out_rows) and all(x == 100 for x in gen)
    out = WB / "_controle" / "COMPLETUDE.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["workbook_id", "macroarea_id", "owner", "pessoa", "modulos", "completude_pct", "estado"])
        w.writerows(out_rows)
        w.writerow(["WB-GERAL", "", "MA.GOV", "", "", overall, "concluido" if done else "em_andamento"])
    for r in out_rows:
        print(f"{r[0]:7} {r[2]:7} {r[5]:>3}%  {r[6]}")
    print(f"WB-GERAL {overall}% {'concluido' if done else 'em_andamento'}  ({out.relative_to(ROOT)})")


# ------------------------------------------------------------------ index
def paginate(lines):
    out = []
    for i, l in enumerate(lines):
        if i and i % INDEX_LINES_PER_PAGE == 0:
            out += ["", CONT, ""]
        out.append(l)
    return out


def write_index(p, lines):
    block = "<!-- INDEX:INICIO -->\n" + "\n".join(paginate(lines)) + "\n<!-- INDEX:FIM -->"
    txt = p.read_text(encoding="utf-8")
    txt = re.sub(r"<!-- INDEX:INICIO -->.*?<!-- INDEX:FIM -->", lambda _: block, txt, flags=re.S)
    p.write_text(txt, encoding="utf-8")


def wb_lines(d, wid, indent=""):
    lines = [f"{indent}- Capa · Index · Overview (`{wid}-CAPA`, `{wid}-IDX`, `{wid}-OVR`)"]
    for mid, md, title in modules(d):
        st = fm(md / "conteudo.md").get("status", "empty") if (md / "conteudo.md").exists() else "ausente"
        lines.append(f"{indent}- {mid} · {title} _({st})_ — Conteúdo · Notas · Tarefas")
    return lines


def cmd_index():
    g = ["## Workbooks"]
    for m, d in area_dirs():
        pct, state, _ = wb_state(d)
        g.append(f"- **{m['workbook_id']} · {m['nome']}** — owner `{m['owner_code']}` · {pct}% {state}")
        g += wb_lines(d, m["workbook_id"], "  ")
        write_index(d / "01_index.md", wb_lines(d, m["workbook_id"]))
    g += ["", "## Registros transversais"]
    for f in sorted(REG.glob("*.csv")):
        g.append(f"- `{f.name}` — {len(rows(f))} registros")
    g.append(f"- ADRs: " + ", ".join(f"`{r['adr_id']}` {r['status']}" for r in rows(REG / "ADRS.csv")))
    write_index(WB / "01_index.md", g)
    print("index atualizado")


# ------------------------------------------------------------------ check
def check_block(p, t, n, wid, errs):
    if not p.exists():
        errs.append(f"{p}: bloco ausente"); return
    m = fm(p)
    if m.get("type") != t:
        errs.append(f"{p}: type '{m.get('type')}' ≠ '{t}'")
    if m.get("workbook_id") != wid:
        errs.append(f"{p}: workbook_id '{m.get('workbook_id')}' ≠ '{wid}'")
    if m.get("status") not in SCORE:
        errs.append(f"{p}: status inválido '{m.get('status')}'")
    if not m.get("owner"):
        errs.append(f"{p}: sem owner")
    b = body(p).lstrip()
    if not b.startswith(PAGE):
        errs.append(f"{p}: deve começar com {PAGE}")
    np_, _ = pages(p)
    if n is None and np_ < 1:
        errs.append(f"{p}: conteúdo sem página")
    elif n is not None and np_ != n:
        errs.append(f"{p}: {np_} páginas fixas, esperado {n} (excesso → {CONT})")


def check_contract(d, wid, area, errs):
    y = d / "workbook.yaml"
    if not y.exists():
        errs.append(f"{y}: ausente"); return
    doc = load_yaml(y)
    if doc.get("schema_version") != "1.0" or doc.get("adr_id") != "ADR-001":
        errs.append(f"{y}: schema_version/adr_id inválidos")
    meta = doc.get("workbook") or {}
    for k in WB_KEYS:
        if k not in meta:
            errs.append(f"{y}: campo obrigatório ausente workbook.{k}")
    if meta.get("id") != wid:
        errs.append(f"{y}: id '{meta.get('id')}' ≠ '{wid}'")
    if meta.get("area_id") != area:
        errs.append(f"{y}: area_id '{meta.get('area_id')}' ≠ '{area}'")
    if (meta.get("layout") or {}) != LAYOUT:
        errs.append(f"{y}: layout difere do ADR-001")
    ex = meta.get("export") or {}
    if ex.get("page_size") != "A4" or ex.get("overflow_policy") != "continuation":
        errs.append(f"{y}: export deve ser A4 com overflow continuation")
    for k in ("template_id", "schema_id", "adr_ids", "evidence_ids"):
        if k not in (meta.get("references") or {}):
            errs.append(f"{y}: campo obrigatório ausente workbook.references.{k}")


def check_tasks(errs):
    owners = rows(ROOT / "OWNERS.csv")
    for a in owners:
        d = ROOT / a["path"].rstrip("/") / "tarefas"
        for p in sorted(d.glob("*.md")) if d.exists() else []:
            if p.name == "README.md":
                continue
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
        if p.name != "README.md" and not any((ROOT / a["path"].rstrip("/") / "tarefas" / p.name).exists() for a in owners):
            errs.append(f"{p}: clone 3 sem clone 2 na pasta do owner")


def cmd_check():
    errs = []
    check_contract(WB, "WB-GERAL", None, errs)
    for f, t, n in FIXED:
        check_block(WB / f, t, n, "WB-GERAL", errs)
    for m, d in area_dirs():
        wid = m["workbook_id"]
        check_contract(d, wid, m["macroarea_id"], errs)
        mods = modules(d)
        if not mods:
            errs.append(f"{d}: workbook sem módulo")
        for p, t, n in blocks(d):
            check_block(p, t, n, wid, errs)
    # fichas obrigatórias (ADR-001.5)
    for e in rows(REG / "ENTIDADES.csv"):
        for col, t in (("ficha_cv", "ficha_cv"), ("ficha_schema", "ficha_schema")):
            p = ROOT / e[col] if e[col] else None
            if not p or not p.exists():
                errs.append(f"{e['entity_id']}: {t} ausente"); continue
            m = fm(p)
            if m.get("id") != e["entity_id"] or m.get("type") != t:
                errs.append(f"{p}: id/type não batem com {e['entity_id']}/{t}")
    # rotas
    rotas = rows(REG / "ROTAS.csv")
    ids = [r["id"] for r in rotas]
    if len(ids) != len(set(ids)):
        errs.append("ROTAS.csv: ids duplicados")
    for r in rotas:
        if r["parent_id"] and r["parent_id"] not in ids:
            errs.append(f"ROTAS.csv: {r['id']} com parent_id inexistente '{r['parent_id']}'")
    # MASTER_INDEX ≡ entities.json
    mi = {r["id"] for r in rows(ROOT / "MASTER_INDEX.csv")}
    ej = {e["id"] for e in json.loads((ROOT / "entities.json").read_text(encoding="utf-8"))}
    if mi != ej:
        errs.append(f"MASTER_INDEX.csv ≠ entities.json: {sorted(mi ^ ej)}")
    check_tasks(errs)
    # checksums do pacote importado
    ck = ROOT / "500_Copiloto_templates" / "00_CONTROLE" / "CHECKSUMS.csv"
    if ck.exists():
        for r in rows(ck):
            rel = "00_CONTROLE/README_PACOTE.md" if r["caminho"] == "README.md" else r["caminho"]
            p = ROOT / "500_Copiloto_templates" / rel
            if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != r["sha256"]:
                errs.append(f"{p}: checksum do pacote divergente ou arquivo ausente")
    print("\n".join(errs) if errs else "check ok")
    sys.exit(1 if errs else 0)


# ------------------------------------------------------------------ build
def cmd_build(escopo, incl_empty):
    if escopo == "GERAL":
        seq = [("WB-GERAL", WB / f) for f, _, _ in FIXED]
        for m, d in area_dirs():
            seq += [(m["workbook_id"], p) for p, _, _ in blocks(d)]
    else:
        area, _, mod = escopo.partition("-")
        m, d = next(((m, d) for m, d in area_dirs() if m["macroarea_id"] == area), (None, None))
        if not m:
            sys.exit(f"escopo desconhecido: {escopo}")
        seq = [(m["workbook_id"], d / f) for f, _, _ in FIXED]
        for mid, md, _ in modules(d):
            if not mod or mid == mod:
                seq += [(m["workbook_id"], md / f) for f, _, _ in CYCLE]
    parts, idx, pno = [], [], 0
    for wid, p in seq:
        meta = fm(p)
        if meta.get("type") == "content" and meta.get("status") == "empty" and not incl_empty:
            continue
        for line in body(p).splitlines():
            s = line.strip()
            if s in (PAGE, CONT):
                pno += 1
                idx.append([pno, wid, meta.get("id", ""), "sim" if s == CONT else "nao", p.relative_to(ROOT)])
                parts.append('\n<div style="page-break-before: always"></div>\n\\newpage\n' if pno > 1 else "")
            else:
                parts.append(line)
    out = WB / "_build" / f"relatorio_{escopo}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    with open(out.with_suffix(".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pagina", "workbook_id", "bloco_id", "continuacao", "arquivo"])
        w.writerows(idx)
    print(f"gerado {out.relative_to(ROOT)} ({pno} páginas A4) + índice de páginas .csv")


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else ""
    esc = sys.argv[sys.argv.index("--escopo") + 1] if "--escopo" in sys.argv else "GERAL"
    {"status": cmd_status, "index": cmd_index, "check": cmd_check,
     "build": lambda: cmd_build(esc, "--incluir-vazios" in sys.argv)}.get(c, lambda: print(__doc__))()
