# 00_Workbook

Arquivo vivo do relatório único. Cada área D01–D16 é um **capítulo**; cada capítulo tem 6 **seções** (S01–S06).

```
00_Workbook/
├── 00_capa.md · 01_indice.md · 02_sumario-executivo.md · 03_escopo-e-metodo.md
├── capitulos/D##_*/ 00_capitulo.md · S01…S06
├── anexos/ A_glossario.md · B_ids-e-referencias.md · C_registro-de-tarefas/
├── _controle/COMPLETUDE.csv   # gerado
└── _build/relatorio.md        # gerado (não versionado)
```

Ordem do relatório final: capa → índice → sumário executivo → escopo e método → capítulos D01…D16 → anexos.
Regras: `500_Copiloto_templates/regras/`. Comandos: `python3 500_Copiloto_templates/scripts/workbook.py status|index|check|build`.
