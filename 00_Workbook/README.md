# 00_Workbook — Workbook Geral (ADR-001)

Camada de **composição e navegação**. Não é um documento monolítico: agrega 15 workbooks especializados (macroáreas A01–A15), cada um exportável sozinho.

```
00_Workbook/
├── workbook.yaml · 00_capa.md · 01_index.md · 02_overview.md     # WB-GERAL (1 · 1 · 3 páginas)
├── workbooks/A##_slug/
│   ├── workbook.yaml                                              # contrato ADR-001 §6
│   ├── 00_capa.md · 01_index.md · 02_overview.md                  # 1 · 1 · 3 páginas
│   └── modulos/M##_slug/ conteudo.md · notas.md · tarefas.md      # ilimitado · 3 · 2 páginas
├── registros/      # transversais e canônicos: ROTAS, ADRS, ENTIDADES, FONTES, DOCUMENTOS, EVIDENCIAS, DEPENDENCIAS
│   ├── adr/        # ADR-001 (VALIDATED)
│   └── fichas/     # <ID>_cv.md + <ID>_schema.md por entidade
├── anexos/         # A glossário · B IDs · C registro de tarefas (clone 3)
├── _controle/COMPLETUDE.csv   # gerado
└── _build/                    # gerado, não versionado
```

- **Paginação:** cada página começa com `<!-- page -->`; excesso em bloco fixo → `<!-- page continuation -->`. Nada é omitido.
- **Registro canônico único:** workbooks referenciam registros e documentos de domínio por ID; nunca copiam.
- **Novo módulo:** copie `500_Copiloto_templates/templates/TPL-021_workbook-universal/modulo/` para `modulos/M##_slug/` e registre em `modules:` do `workbook.yaml`.
- **Comandos:** `python3 500_Copiloto_templates/scripts/workbook.py check | status | index | build --escopo GERAL|A##|A##-M##`.
