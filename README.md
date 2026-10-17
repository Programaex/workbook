# EXECUTAR — Workbook

Repositório de **dataset** da estrutura macro do Programa EXECUTAR: 16 áreas (D01–D16), cada uma com um owner correlativo. Fonte: `IMG_4287.jpeg` (infográfico `EXEC-INFO-DOMAIN-001` v1.0.0).

## Estrutura

```
workbook/
├── CLAUDE.md          # regras para agentes
├── README.md
├── MASTER_INDEX.csv   # índice canônico (17 entidades)
├── OWNERS.csv         # registro de owners
├── entities.json      # mesmo índice em JSON
├── relations.csv      # relações entre entidades (vazio: nenhuma comprovada)
├── evidence.json      # evidência da fonte
├── D01_gestao-empresarial/ … D16_midias-sociais-distribuicao-digital/
└── _sources/SRC-FOLDER-001/   # pasta adicional observada, vínculo não confirmado
```

## Áreas e owners

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

## Como usar como dataset

- `MASTER_INDEX.csv` e `entities.json` são a fonte de verdade de IDs, nomes e owners.
- Cada pasta de área tem um `README.md` com front matter YAML (`id`, `owner`, `group`, `status`).
- `status: existing` = observado na fonte; **não** comprova implementação.

## Limitações conhecidas

- Conteúdo interno das áreas não inspecionado (a fonte indica 7 itens por área, não individualizados).
- Versões e pessoas responsáveis permanecem vazias.
- `SRC-FOLDER-001` não tem owner nem relação com D01–D16.
