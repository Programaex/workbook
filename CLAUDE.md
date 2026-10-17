# CLAUDE.md — workbook

Este repositório é um **dataset**. A estrutura macro D01–D16 é regra; não reorganize.

## Regras da estrutura
1. IDs `D01`–`D16` são imutáveis. Nomes de pasta seguem `D##_slug-kebab-sem-acento` (ver `MASTER_INDEX.csv`, coluna `name`).
2. Novo conteúdo entra dentro da pasta da área correta. Nunca crie pasta de primeiro nível fora de D01–D16 e `_sources/`.
3. `MASTER_INDEX.csv` e `entities.json` devem permanecer idênticos em conteúdo. Alterou um, atualize o outro.
4. Toda pasta de área tem `README.md` com front matter: `id`, `canonical_name`, `owner`, `group`, `status`.

## Owners
- Formato `<GRUPO>.<ÁREA>`, maiúsculas: GV (Governança), TD (Tecnologia e dados), OP (Operação), PD (Produto e experiência), MR (Mercado e receita).
- Mapa oficial em `OWNERS.csv`. Para criar owner novo: grupo existente + sigla de 3 letras única; registre em `OWNERS.csv`, no README da área e no índice.
- O owner é um papel, não uma pessoa. Não preencha `person` sem informação do usuário.
- Todo arquivo de dados novo declara o owner (coluna `owner` ou front matter).

## Integridade dos dados
- Não invente conteúdo, versões, responsáveis, caminhos ou relações. Sem evidência, deixe vazio ou marque `GAP`.
- `existing` = observado na fonte, não prova implementação.
- `relations.csv` só recebe relação comprovada, com `source_of_truth`.
- `SRC-FOLDER-001` permanece sem owner até o vínculo ser demonstrado.
- Formatos: CSV UTF-8 com cabeçalho, JSON indentado com 2 espaços, Markdown em pt-BR.

## Git
Desenvolva na branch designada pela sessão; não abra PR sem pedido explícito.
