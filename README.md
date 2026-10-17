# EXECUTAR — Workbook

Repositório de **dataset** e **Workbook Geral** do Programa EXECUTAR, conforme o **ADR-001 — Arquitetura Unificada de Workbooks** (VALIDATED 2026-10-17, `00_Workbook/registros/adr/`).

Duas camadas de taxonomia:
- **Macroáreas A01–A15** (ADR-001): cada uma é um **workbook** especializado.
- **Domínios D01–D16** (foto `IMG_4287.jpeg`, `EXEC-INFO-DOMAIN-001`): pastas de owner, imutáveis.

Artefatos declaram `macroarea_id` e `dominio_id`. Não há mapeamento global D→A; relações só com fonte em `relations.csv` (hoje: `D16-DOC-PEM-001 → A08`). Mapeamento de rotas ↔ macroáreas: ADR-002 (pendente).

## Estrutura

```
workbook/
├── CLAUDE.md · README.md
├── MACROAREAS.csv     # A01–A15, owners MA.<SIG>, workbook_id
├── OWNERS.csv         # D01–D16, owners GRUPO.ÁREA
├── MASTER_INDEX.csv ≡ entities.json   # índice canônico de entidades
├── relations.csv · evidence.json
├── 00_Workbook/       # Workbook Geral: composição dos 15 workbooks + registros transversais
├── 500_Copiloto_templates/  # templates (TPL-001..023), schemas, regras, script
├── D01_… / D16_…/     # domínios: README, tarefas/ (clone 2), documentos/
└── _sources/          # fontes originais (SRC-FOLDER-001, SRC-DOC-001..003)
```

## Macroáreas e workbooks (ADR-001)

| Owner | ID | Macroárea | Workbook |
|---|---|---|---|
| `MA.GOV` | A01 | Governança | `WB-A01` · `00_Workbook/workbooks/A01_governanca/` |
| `MA.PRG` | A02 | Programa | `WB-A02` · `00_Workbook/workbooks/A02_programa/` |
| `MA.BUS` | A03 | Business | `WB-A03` · `00_Workbook/workbooks/A03_business/` |
| `MA.ECO` | A04 | Ecossistema | `WB-A04` · `00_Workbook/workbooks/A04_ecossistema/` |
| `MA.PEV` | A05 | Pesquisa e Evidências | `WB-A05` · `00_Workbook/workbooks/A05_pesquisa-evidencias/` |
| `MA.DAD` | A06 | Dados | `WB-A06` · `00_Workbook/workbooks/A06_dados/` |
| `MA.CPM` | A07 | Creator PEM | `WB-A07` · `00_Workbook/workbooks/A07_creator-pem/` |
| `MA.EDI` | A08 | Editorial | `WB-A08` · `00_Workbook/workbooks/A08_editorial/` |
| `MA.OPS` | A09 | Operações | `WB-A09` · `00_Workbook/workbooks/A09_operacoes/` |
| `MA.PRO` | A10 | Produção | `WB-A10` · `00_Workbook/workbooks/A10_producao/` |
| `MA.AGT` | A11 | Agentes | `WB-A11` · `00_Workbook/workbooks/A11_agentes/` |
| `MA.PRD` | A12 | Produtos | `WB-A12` · `00_Workbook/workbooks/A12_produtos/` |
| `MA.DSG` | A13 | Design | `WB-A13` · `00_Workbook/workbooks/A13_design/` |
| `MA.TPL` | A14 | Templates | `WB-A14` · `00_Workbook/workbooks/A14_templates/` |
| `MA.COM` | A15 | Comercial | `WB-A15` · `00_Workbook/workbooks/A15_comercial/` |

Owners `MA.<SIG>` são **propostos** (correlativos à macroárea); pessoas a definir em `MACROAREAS.csv`.

## Layout universal de cada workbook

| Bloco | Páginas | Comportamento |
|---|---|---|
| Capa | 1 | Fixa |
| Index | 1 | Fixa; overflow → continuação |
| Overview top-down | 3 | Fixo, síntese progressiva |
| Conteúdo (por módulo) | ilimitadas | Dinâmico |
| Notas (por módulo) | 3 | Fixas |
| Tarefas (por módulo) | 2 | Fixas |

Nenhuma informação é omitida: excesso vira página de continuação (`<!-- page continuation -->`).

## Domínios e owners

Código de owner: `<GRUPO>.<ÁREA>` (ex.: `MR.MKT` = Mercado e receita · Marketing).

| Owner | ID | Área | Pasta |
|---|---|---|---|
| `GV.GES` | D01 | Gestão empresarial | `D01_gestao-empresarial/` |
| `GV.JUR` | D02 | Jurídico, riscos e conformidade | `D02_juridico-riscos-conformidade/` |
| `GV.FIN` | D03 | Finanças | `D03_financas/` |
| `GV.PES` | D04 | Pessoas e recursos humanos | `D04_pessoas-recursos-humanos/` |
| `TD.DAD` | D05 | Dados | `D05_dados/` |
| `TD.CON` | D06 | Conhecimento e busca corporativa | `D06_conhecimento-busca-corporativa/` |
| `OP.PRD` | D07 | Produtividade e execução | `D07_produtividade-execucao/` |
| `OP.OPS` | D08 | Operações | `D08_operacoes/` |
| `PD.INO` | D09 | Pesquisa e inovação | `D09_pesquisa-inovacao/` |
| `PD.PRO` | D10 | Gestão de produto | `D10_gestao-produto/` |
| `PD.EXP` | D11 | Experiência e projeto | `D11_experiencia-projeto/` |
| `TD.ENG` | D12 | Engenharia | `D12_engenharia/` |
| `MR.MKT` | D13 | Mercado e geração de demanda | `D13_mercado-geracao-demanda/` |
| `MR.VEN` | D14 | Vendas | `D14_vendas/` |
| `MR.CSU` | D15 | Atendimento e sucesso do cliente | `D15_atendimento-sucesso-cliente/` |
| `MR.MID` | D16 | Mídias sociais e distribuição digital | `D16_midias-sociais-distribuicao-digital/` |

Grupos:

| Grupo | Nome |
|---|---|
| `GV` | Governança |
| `TD` | Tecnologia e dados |
| `OP` | Operação |
| `PD` | Produto e experiência |
| `MR` | Mercado e receita |

O código identifica o **papel/função** dona da área. A pessoa responsável fica em `OWNERS.csv` (coluna `person`), vazia até ser definida.

## Schemas de IDs

| Objeto | Formato | Exemplo | Schema (`ids.schema.json#/…`) |
|---|---|---|---|
| Macroárea | `A##` (01–15) | `A08` | `macroarea` |
| Owner de macroárea | `MA.<SIG>` | `MA.EDI` | `owner_macroarea` |
| Domínio | `D##` (01–16) | `D13` | `area` |
| Owner de domínio | `GRUPO.ÁREA` | `MR.MKT` | `owner` |
| Workbook | `WB-GERAL`, `WB-A##` | `WB-A08` | `workbook` |
| Bloco | `WB-A##-CAPA\|IDX\|OVR`, `WB-A##-M##-CNT\|NOT\|TSK` | `WB-A08-M01-CNT` | `bloco` |
| Entidade (fichas obrigatórias) | `AGT-###`, `SKL-###`, `FER-###`, `PROD-###` | `AGT-002` | `entidade` |
| ADR | `ADR-###` | `ADR-001` | `adr` |
| Documento de domínio | `D##-DOC-<TIPO>-###` | `D16-DOC-PEM-001` | `documento_dominio` |
| Epic / Project / Issue / Sub-issue | `EP\|PJ\|IS\|SI-<OWNER>-<NNNN>` (nº GitHub) | `IS-MR.MKT-0042` | `tarefa` |
| Template | `TPL-###` (`00_CONTROLE/CROSSWALK_REPO.csv`) | `TPL-021` | `template` |
| Fonte | `SRC-DOC-###`, `SRC-FOLDER-###` | `SRC-DOC-003` | `fonte` |
| IDs de engenharia (provisórios) | `ECO-`, `F0x`, `ENG-` | `ECO-001` | — |

Um conteúdo pode ter vários donos: `owner` primário + `co_owners`. Ver `CLAUDE.md`.

## Registros transversais (`00_Workbook/registros/`)

`ROTAS.csv` (78 rotas, verbatim de `SRC-DOC-003` + colunas de vínculo) · `ADRS.csv` · `ENTIDADES.csv` · `FONTES.csv` · `DOCUMENTOS.csv` · `EVIDENCIAS.csv` · `DEPENDENCIAS.csv` · `fichas/`.

Toda entidade (agente, skill, ferramenta, produto) tem **ficha CV** (`TPL-022`) e **ficha schema** (`TPL-023`).

## Regras operacionais

- **Tarefas (tripla clonagem):** GitHub → `D##_*/tarefas/` → `00_Workbook/anexos/C_registro-de-tarefas/`. Ver `500_Copiloto_templates/regras/OPERACOES.md`.
- **Acompanhamento e completude:** blocos `empty → draft → review → done`, por workbook. Ver `500_Copiloto_templates/regras/ACOMPANHAMENTO.md`.
- **Comandos:** `python3 500_Copiloto_templates/scripts/workbook.py check | status | index | build --escopo GERAL|A##|A##-M##`.

## Limitações conhecidas

- IDs A01–A15 e owners `MA.*` são provisórios (ADR-001 §3); pessoas não atribuídas.
- Rotas ainda sem vínculo com macroárea/workbook/entidade (ADR-002).
- Exportação gera MD A4 + índice de páginas; PDF pendente.
- `SRC-FOLDER-001` sem owner nem relação comprovada.
