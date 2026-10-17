# Regra de acompanhamento e completude (ADR-001)

## Unidade de acompanhamento
O **workbook A##** (macroárea). O Workbook Geral (`WB-GERAL`) é a composição dos 15.

## Estados de um bloco (`status` no front matter)
| Estado | Pontos | Critério |
|---|---|---|
| `empty` | 0 | Só placeholder |
| `draft` | 33 | Conteúdo parcial ou apenas referências |
| `review` | 66 | Completo, aguardando revisão do owner |
| `done` | 100 | Revisado, com `source_refs` e sem `GAP` |

Blocos: Capa · Index · Overview (fixos) + por módulo Conteúdo · Notas · Tarefas.

## Completude
- Workbook: média dos pontos de todos os blocos.
- Estados: `nao_iniciado` (tudo `empty`) · `em_andamento` · `em_revisao` (tudo ≥ `review`) · `concluido` (tudo `done`).
- Workbook Geral: 80% média dos 15 workbooks + 20% média de Capa/Index/Overview do Geral. `concluido` quando os 15 e o Geral estão `done`.

## Paginação (ADR-001 §2) — verificada pelo `check`
| Bloco | Páginas fixas |
|---|---|
| Capa | 1 |
| Index | 1 |
| Overview | 3 |
| Conteúdo | ≥ 1 (ilimitado) |
| Notas | 3 |
| Tarefas | 2 |

Cada página começa com `<!-- page -->`. Conteúdo que excede um bloco fixo continua em `<!-- page continuation -->` — **nunca** se corta informação. A numeração final é calculada no `build`.

## Fichas obrigatórias (ADR-001.5)
Toda entidade em `00_Workbook/registros/ENTIDADES.csv` (agente, skill, ferramenta, produto) tem `<ID>_cv.md` (TPL-022) **e** `<ID>_schema.md` (TPL-023). Faltou uma → `check` falha.

## Rotina
`workbook.py check` → `status` → `index`; commite `00_Workbook/_controle/COMPLETUDE.csv`.
Exportar: `workbook.py build --escopo GERAL|A##|A##-M##` (MD A4 + índice de páginas CSV; PDF pendente).

## Cadência
Revisão semanal por owner; só o owner move `review → done`.
