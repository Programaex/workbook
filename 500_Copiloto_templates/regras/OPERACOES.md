# Regra de operações — tarefas em tripla clonagem

Vale para **epics, projects, issues e sub-issues** sempre que forem citados (em conversa, documento ou commit).

## Ordem obrigatória (3 clones)
1. **GitHub** — criar/localizar o item no repositório `Programaex/workbook` (issue/sub-issue; project e epic conforme a convenção do GitHub Projects). O número do GitHub é a chave.
2. **Pasta do owner** — `D##_*/tarefas/<ID>.md` da área dona. É o registro de tarefas do owner.
3. **Workbook** — espelho em `00_Workbook/anexos/C_registro-de-tarefas/<ID>.md`, e o ID entra em `tasks:` das seções `WB-…` afetadas.

Nunca crie o clone 2 sem o 1, nem o 3 sem o 2. Se o GitHub estiver inacessível, **pare e avise**; não use número provisório.

## ID
`<TIPO>-<OWNER>-<NNNN>`: `EP` epic · `PJ` project · `IS` issue · `SI` sub-issue; `NNNN` = número do GitHub com 4 dígitos. Ex.: `IS-MR.MKT-0042`.
Sub-issue declara `parent` (ID do pai). Hierarquia: PJ → EP → IS → SI.

## Conteúdo dos clones
Os três têm o mesmo front matter (`500_Copiloto_templates/templates/tarefa.md`); o GitHub é a fonte de verdade de título, status e descrição. Mudou no GitHub → atualize 2 e 3 na mesma sessão.

## Item citado sem owner claro
Pergunte a área. Não deduza.

## Verificação
`python3 500_Copiloto_templates/scripts/workbook.py check` — falha se faltar clone, se o ID não bater com o owner da área ou com `github_number`, ou se houver espelho sem registro do owner.
