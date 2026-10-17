# TPL-021 · Workbook universal (ADR-001)

Layout fixo por workbook: **Capa 1 · Index 1 · Overview 3**, depois um ciclo por módulo: **Conteúdo (ilimitado) · Notas 3 · Tarefas 2**.

- Cada página começa com `<!-- page -->`. Excesso vira `<!-- page continuation -->` — nunca omita informação para caber.
- `workbook.yaml` segue o contrato mínimo do ADR-001 §6 (`schemas/workbook.schema.json`).
- Capa alinhada ao `TPL-018`; página de conteúdo alinhada ao `TPL-017`.
