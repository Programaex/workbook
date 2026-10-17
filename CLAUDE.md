# CLAUDE.md — workbook

Este repositório é um **dataset**. A estrutura macro D01–D16 é regra; não reorganize.

## Regras da estrutura
1. IDs `D01`–`D16` são imutáveis. Nomes de pasta seguem `D##_slug-kebab-sem-acento` (ver `MASTER_INDEX.csv`, coluna `name`).
2. Novo conteúdo entra dentro da pasta da área correta. Nunca crie pasta de primeiro nível fora de D01–D16, `00_Workbook/`, `500_Copiloto_templates/` e `_sources/`.
3. `MASTER_INDEX.csv` e `entities.json` devem permanecer idênticos em conteúdo. Alterou um, atualize o outro.
4. Toda pasta de área tem `README.md` com front matter: `id`, `canonical_name`, `owner`, `group`, `status`.

## Owners
- Formato `<GRUPO>.<ÁREA>`, maiúsculas: GV (Governança), TD (Tecnologia e dados), OP (Operação), PD (Produto e experiência), MR (Mercado e receita).
- Mapa oficial em `OWNERS.csv`. Para criar owner novo: grupo existente + sigla de 3 letras única; registre em `OWNERS.csv`, no README da área e no índice.
- O owner é um papel, não uma pessoa. Não preencha `person` sem informação do usuário.
- Todo arquivo de dados novo declara o owner (coluna `owner` ou front matter).

## Workbook e templates
- `00_Workbook/` é o relatório vivo (capa, índice, sumário, escopo, capítulos D01–D16 com seções S01–S06, anexos). Escreva conteúdo nas seções do capítulo da área; mantenha o front matter (`id`, `owner`, `status`, `updated`).
- `500_Copiloto_templates/` guarda templates, schemas, regras e `scripts/workbook.py`. Novos arquivos nascem de um template; mude o template, não a cópia.
- Esquemas de IDs: tabela no `README.md`.

## Regra de operações (tarefas)
Epic, project, issue ou sub-issue citado = **tripla clonagem, nesta ordem**: 1) GitHub, 2) `D##_*/tarefas/<ID>.md` do owner, 3) `00_Workbook/anexos/C_registro-de-tarefas/<ID>.md`. ID `<TIPO>-<OWNER>-<nº GitHub 4 dígitos>`. Sem acesso ao GitHub: pare e avise. Detalhes: `500_Copiloto_templates/regras/OPERACOES.md`.

## Regra de acompanhamento e completude
Ao editar o workbook ou tarefas rode `workbook.py check`, `status` e `index`, e commite `00_Workbook/_controle/COMPLETUDE.csv`. Nunca marque `done` sem fontes e revisão do owner. Critérios: `500_Copiloto_templates/regras/ACOMPANHAMENTO.md`.

## Integridade dos dados
- Não invente conteúdo, versões, responsáveis, caminhos ou relações. Sem evidência, deixe vazio ou marque `GAP`.
- `existing` = observado na fonte, não prova implementação.
- `relations.csv` só recebe relação comprovada, com `source_of_truth`.
- `SRC-FOLDER-001` permanece sem owner até o vínculo ser demonstrado.
- Formatos: CSV UTF-8 com cabeçalho, JSON indentado com 2 espaços, Markdown em pt-BR.

## Git
Desenvolva na branch designada pela sessão; não abra PR sem pedido explícito.
