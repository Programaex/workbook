# Regra de acompanhamento e completude

## Estados de uma seção (`status` no front matter)
| Estado | Pontos | Critério |
|---|---|---|
| `empty` | 0 | Só placeholder |
| `draft` | 33 | Conteúdo parcial |
| `review` | 66 | Completo, aguardando revisão do owner |
| `done` | 100 | Revisado, com `sources` e sem pendências |

## Completude da área
`completude_pct` = média dos pontos das seções S01–S06 do capítulo.

| Estado da área | Condição |
|---|---|
| `nao_iniciada` | todas as seções `empty` |
| `em_andamento` | qualquer outro caso |
| `em_revisao` | todas as seções em `review` ou `done` |
| `concluida` | todas `done` **e** nenhuma tarefa aberta (`backlog|todo|doing|blocked`) em `D##/tarefas/` **e** pessoa definida em `OWNERS.csv` |

## Completude do workbook
`80%` média das 16 áreas + `20%` média dos documentos de abertura (capa, índice, sumário executivo, escopo e método).
O workbook está `concluido` quando as 16 áreas estão `concluida` e os 4 documentos de abertura estão `done`.

## Rotina
Ao fechar qualquer edição: `workbook.py check` → `workbook.py status` → `workbook.py index`. Commite o `COMPLETUDE.csv` atualizado.
Montagem do relatório único: `workbook.py build` (omite seções `empty`; `--incluir-vazios` para forçar).

## Cadência
Revisão de completude semanal por owner; o owner move `review → done`, não quem redigiu.
