# 500_Copiloto_templates

Templates, schemas, regras e script reutilizáveis para organizar o workbook.

| Pasta | Conteúdo |
|---|---|
| `00_CONTROLE/` | Catálogo do pacote de templates CSV: `MASTER_INDEX.csv`, `OWNERS.csv` (papéis), `AREAS.csv`, `CAMPOS_SCHEMA_GLOBAL.csv`, `WORKBOOK_IMPORT_ORDER.csv`, `RELACOES.csv`, `MAPEAMENTO_ORIGEM.csv`, `INVENTARIO_LINHAS_ORIGEM.csv`, `VALIDACAO.csv`, `CHECKSUMS.csv`, `README_PACOTE.md` |
| `00_CONTROLE/CROSSWALK_REPO.csv` | **Ponte com o repositório**: cada `TPL-###` → área, owner `GRUPO.ÁREA`, papel, caminho e capítulo do workbook |
| `areas/D##_area/OWNER_papel/TPL-###_nome/` | Templates CSV: `template.csv`, `exemplo_origem.csv`, `schema.csv`, `schema.json`, `README.md` |
| `90_REFERENCIAS/` | Arquivos-fonte do pacote (`Untitled 2.md`, `CAPA.md`, `ID_AREA_TUTULO_OWNER.md`, mapa A4…) |
| `templates/` | `TPL-020` fichas schema ecossistema · `TPL-021` workbook universal (ADR-001) · `TPL-022` ficha CV · `TPL-023` ficha schema · tarefa · checklist de fechamento |
| `schemas/` | JSON Schema: `ids`, `workbook` (contrato ADR-001 §6), `bloco`, `ficha-cv`, `ficha-schema`, `tarefa`, `area-status` |
| `regras/` | `OPERACOES.md` (tripla clonagem) e `ACOMPANHAMENTO.md` (completude) |
| `scripts/workbook.py` | `status`, `index`, `check` (contrato, paginação, fichas, rotas, tarefas, checksums), `build --escopo` |

## Catálogo de templates

Fonte de verdade: `00_CONTROLE/CROSSWALK_REPO.csv` (23 templates; colunas `macroarea_id` e `workbook_id`).

| ID | Nome | Área | Owner | Papel |
|---|---|---|---|---|
| TPL-001 | briefing_missao | D10 | `PD.PRO` | Product Manager |
| TPL-002 | direcao_de_arte | D11 | `PD.EXP` | Direção de Arte |
| TPL-003 | biblioteca_materiais | D11 | `PD.EXP` | Artista de Materiais 3D |
| TPL-004 | ambiente_cenografia | D11 | `PD.EXP` | Designer de Ambiente 3D |
| TPL-005 | componentes_anatomicos | D09 | `PD.INO` | Especialista em Neuroanatomia 3D |
| TPL-006 | elementos_graficos_secundarios | D11 | `PD.EXP` | Motion Designer 3D |
| TPL-007 | timeline_coreografia | D11 | `PD.EXP` | Motion Designer 3D |
| TPL-008 | cameras | D11 | `PD.EXP` | Diretor de Fotografia 3D |
| TPL-009 | setup_iluminacao | D11 | `PD.EXP` | Lighting Artist 3D |
| TPL-010 | parametros_animacao | D12 | `TD.ENG` | Engenheiro de Animação 3D |
| TPL-011 | implementacao_tecnica | D12 | `TD.ENG` | Tech Lead 3D |
| TPL-012 | artefatos_exportacao | D08 | `OP.OPS` | Produtor Multimídia |
| TPL-013 | interatividade_web | D12 | `TD.ENG` | Engenheiro Frontend |
| TPL-014 | criterios_qa | D12 | `TD.ENG` | QA Engineer |
| TPL-015 | estrutura_pacote_entrega | D08 | `OP.OPS` | Gestor de Entregas |
| TPL-016 | contrato_execucao_agente | D07 | `OP.PRD` | Orquestrador de Agentes IA |
| TPL-017 | pagina_workbook_editorial | D05 | `TD.DAD` | Gestor de Conhecimento |
| TPL-018 | capa_workbook | D11 | `PD.EXP` | Designer Editorial |
| TPL-019 | registro_referencias_visuais | D09 | `PD.INO` | Pesquisador de Referências |
| TPL-020 | fichas_schema_ecossistema_executar | D12 (+D10) | `TD.ENG` (co `PD.PRO`) | — |
| TPL-021 | workbook_universal | D05 · A14 | `TD.DAD` (co `MA.TPL`) | — |
| TPL-022 | ficha_cv | D07 · A11 | `OP.PRD` (co `MA.AGT`, `PD.PRO`) | — |
| TPL-023 | ficha_schema | D07 · A11 | `OP.PRD` (co `MA.AGT`, `PD.PRO`) | — |

## Convenções do pacote
- Arquivos de `00_CONTROLE/`, `areas/` e `90_REFERENCIAS/` são importados **verbatim** (UTF-8 com BOM) e conferidos por `CHECKSUMS.csv`. Não edite: para mudar um template, gere nova versão do pacote ou crie `TPL-` novo.
- `owner_papel` é o papel funcional **dentro** da área; o owner do repositório é o código `GRUPO.ÁREA` da área (ver `CROSSWALK_REPO.csv`). `owner_pessoa` fica vazio até o usuário informar.
- `exemplo_origem.csv` é referência do briefing, não prova de execução.
- Placeholders dos templates Markdown usam `{CHAVE}`; os do `TPL-020` usam `{{CHAVE}}` (da fonte).
- `TPL-021` gera todo workbook (Geral e A01–A15). `TPL-022` + `TPL-023` são obrigatórios em par para cada agente, skill, ferramenta e produto (ADR-001.5).
