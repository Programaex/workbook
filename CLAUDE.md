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
- **Conteúdo pode ter mais de uma área/owner** (ex.: produto + engenharia). Declare `owner` (primário, a área da fonte) e `co_owners: [..]` (demais) no front matter, e `areas: [D##, ..]` quando abranger várias. Para arquivos com blocos de donos diferentes, liste o owner de cada bloco num comentário no topo. O conteúdo é registrado no capítulo do owner primário e referenciado nos capítulos dos co-owners; nunca duplicado.
- O owner é um papel, não uma pessoa. Não preencha `person` sem informação do usuário.
- Todo arquivo de dados novo declara o owner (coluna `owner` ou front matter).

## Workbook e templates
- `00_Workbook/` é o relatório vivo (capa, índice, sumário, escopo, capítulos D01–D16 com seções S01–S06, anexos). Escreva conteúdo nas seções do capítulo da área; mantenha o front matter (`id`, `owner`, `status`, `updated`).
- `500_Copiloto_templates/` guarda templates, schemas, regras e `scripts/workbook.py`. Novos arquivos nascem de um template; mude o template, não a cópia.
- Esquemas de IDs: tabela no `README.md`.
- **Templates (`TPL-###`)**: registro único em `500_Copiloto_templates/00_CONTROLE/CROSSWALK_REPO.csv`. Próximo ID = maior existente + 1; nunca reutilize. Todo template novo entra no crosswalk e no bloco `TEMPLATES` do `00_capitulo.md` da área.
- **Papel vs. owner**: `owner_papel` (ex.: Product Manager) é a função dentro da área; o `owner` continua sendo o código `GRUPO.ÁREA` da área. Um papel nunca vira owner novo sem pedido do usuário.
- **Pacotes importados** (`00_CONTROLE/`, `areas/`, `90_REFERENCIAS/` da 500) são verbatim e verificados por `CHECKSUMS.csv` no `workbook.py check`. Não edite à mão; conflito de ID com o que já existe → renumere o lado do repositório e registre no crosswalk.
- IDs de engenharia (`ECO-`, `PROD-`, `F00`–`F02`, `ADR-`, `ENG-`) vêm da fonte e são **provisórios** até conciliar com o índice mestre. Um `ENG-NNN` (cartão de ação) que virar tarefa segue a tripla clonagem e ganha ID `<TIPO>-<OWNER>-<nº GitHub>`, guardando o `ENG-NNN` em `aliases`.

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

## Git — sempre merge na main
Regra permanente do dono do repositório (vale como autorização para criar PR e fazer merge):
1. Trabalhe na branch designada pela sessão e faça commits claros.
2. Ao concluir cada entrega, **faça merge na `main`**. Nunca deixe a entrega só na branch.
3. **Nunca use draft.** PR sempre criado pronto (não-draft) e mergeado em seguida.
4. Se a `main` ainda não existir, publique a branch como `main` (`git push origin <branch>:main`).
5. Antes do merge rode `workbook.py check`; só faça merge com `check ok`. Conflito: traga a `main` para a branch, resolva e então faça merge.
6. Depois do merge, a branch da sessão continua sendo a base de trabalho (ressincronize com a `main`).
