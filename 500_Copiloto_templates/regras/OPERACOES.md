# Regra de operações — GitHub Projects, hierarquia e tripla clonagem

Vale para **projects, epics, issues, sub-issues e gates** sempre que forem citados (em conversa, documento ou commit).

## Estrutura (GitHub Projects)
Todo o acompanhamento operacional vive num **GitHub Project** (Projects v2) do usuário `Programaex`. Hierarquia:

| Nível | Tipo | No GitHub | Pai obrigatório |
|---|---|---|---|
| 1 | `PJ` project | o Project (número da URL `/users/Programaex/projects/<N>`) | — |
| 2 | `EP` epic | issue com rótulo `tipo:epic`, item do Project | `PJ` |
| 3 | `IS` issue | sub-issue do epic, rótulo `tipo:issue` | `EP` |
| 4 | `SI` sub-issue | sub-issue da issue, rótulo `tipo:sub-issue` | `IS` |
| — | `GT` gate | sub-issue do epic, rótulo `tipo:gate` — ponto de decisão com data, evidência e consequência | `EP` |

O Project usa a hierarquia nativa (sub-issues + *Show hierarchy*) nas visões **Table**, **Board** (por Status) e **Roadmap** (por *Start date* → *Target date*).

## Campos obrigatórios de todo item
| Campo | GitHub | Front matter dos clones |
|---|---|---|
| Responsável | *Assignees* = `Programaex` (assigned to me), salvo indicação do usuário | `assignees: [Programaex]` |
| Início / prazo | campos do Project *Start date* / *Target date*; no corpo da issue: `**Início:** AAAA-MM-DD` e `**Prazo:** AAAA-MM-DD` | `start_date`, `due_date` (AAAA-MM-DD; `null` = pendência) |
| Owner primário | rótulo `owner:<GRUPO.ÁREA>` e campo *Owner* do Project | `owner` |
| Subtags de owner | um rótulo `co:<GRUPO.ÁREA>` por co-owner | `co_owners: [..]` |
| Macroárea | rótulo `macro:A##` | `macroarea_id` |
| Tipo | rótulo `tipo:project\|epic\|issue\|sub-issue\|gate` e campo *Tipo* do Project | `type` |
| Pai | sub-issue do pai no GitHub | `parent: <ID>` |
| Project | item do Project | `project: <ID PJ>` (ou `null` enquanto o número não for conhecido) |

A Action `.github/workflows/project-sync.yml` adiciona cada issue com rótulo `tipo:*` ao Project e copia *Início*, *Prazo*, *Owner* e *Tipo* para os campos do Project. Ela exige o segredo `PROJECT_TOKEN` (PAT com escopo `project`) e a variável `PROJECT_NUMBER`.

## Ordem obrigatória (3 clones)
1. **GitHub** — criar/localizar o item no repositório `Programaex/workbook` com rótulos, responsável, datas, pai (sub-issue) e item do Project. O número do GitHub é a chave.
2. **Pasta do owner** — `D##_*/tarefas/<ID>.md` da área dona. É o registro de tarefas do owner.
3. **Workbook** — espelho em `00_Workbook/anexos/C_registro-de-tarefas/<ID>.md`, e o ID entra na tabela do bloco **Tarefas** (`WB-A##-M##-TSK`) do módulo afetado.

Nunca crie o clone 2 sem o 1, nem o 3 sem o 2. Se o GitHub estiver inacessível, **pare e avise**; não use número provisório.

## ID
`<TIPO>-<OWNER>-<NNNN>`: `PJ` project · `EP` epic · `IS` issue · `SI` sub-issue · `GT` gate; `NNNN` = número do GitHub (issue, ou número do Project para `PJ`) com 4 dígitos. Ex.: `IS-MR.MKT-0042`, `GT-OP.OPS-0007`.
IDs de planos (`TSK-NNNN`, `GATE-NN`) ficam em `aliases`.

## Conteúdo dos clones
Os três têm o mesmo front matter (`500_Copiloto_templates/templates/tarefa.md`); o GitHub é a fonte de verdade de título, status, datas, responsável e descrição. Mudou no GitHub → atualize 2 e 3 na mesma sessão.

## Item citado sem owner claro
Pergunte a área. Não deduza.

## Verificação
`python3 500_Copiloto_templates/scripts/workbook.py check` — falha se faltar clone, se o ID não bater com o owner da área ou com `github_number`, se houver espelho sem registro do owner, se `IS`/`SI`/`GT` não tiverem `parent` registrado, se faltar `assignees`, ou se `start_date`/`due_date` estiverem fora do formato ou invertidas.
