---
id: FER-001
type: ficha_schema
entity_type: ferramenta
nome: painel-gestao
macroarea_id: A09
dominio_id: D08
owner: MA.OPS
owner_pessoa: null
status: draft
version: 0.1.0
updated: 2026-10-17
source_refs: [Programaex/design apps/gestao/README.md, EP-OP.OPS-0003, EP-OP.OPS-0005]
---
<!-- page -->
# painel-gestao · Anatomia

## 1. Gatilhos de escrita
| Gatilho | Descrição |
|---|---|
| Execução de tarefa | `npm run snapshot -w apps/gestao` regrava `data/snapshot.json` a partir do workbook |
| Input do usuário | Nenhuma escrita: o painel é somente leitura (botões Atualizar, Pré-visualizar e Imprimir) |
| Saída de ferramenta | Resposta da API do GitHub gravada no Cache API do Worker por 10 min (sem `GITHUB_TOKEN` o limite anônimo é de 60 chamadas/hora por IP; um 403 faz o painel usar o snapshot) |
| Decisão do agente | Não se aplica (sem agente) |

## 2. Armazenamentos (4 tipos)
| Tipo | Conteúdo | Backend |
|---|---|---|
| Working | estado da tarefa: dados mesclados do épico na sessão do navegador | memória do navegador |
| Episodic | execuções passadas: GAP (sem histórico de consultas) | — |
| Semantic | fatos e preferências: snapshot das 93 tarefas e modelo do PDF | `apps/gestao/data/*.json` (versionado) |
| Procedural | fluxos aprendidos: regras dos KPIs e agrupamentos | `apps/gestao/lib/kpis.mjs`, `lib/views.mjs` |

## 3. Decisão de contexto — cabe no orçamento? (trust + recência)
- Sim → injeta no contexto: GitHub respondeu (≤ 10 min) — o GitHub sobrepõe estado, datas, checklist e rótulos do snapshot
- Não ou obsoleto → loop de busca até verificar e atualizar: GitHub indisponível — usa o snapshot e exibe aviso; "Atualizar do GitHub" força nova consulta

## 4. Write policy (gatekeeper)
| Controle | Critério |
|---|---|
| Gate — importância / confiança | Só lê; não escreve no GitHub nem no workbook |
| Trust — proveniência / rank da fonte | GitHub (fonte de verdade) > snapshot do workbook > plano operacional |
| Validate → Admit | Itens só do GitHub entram marcados "fora do snapshot"; ausentes no GitHub geram aviso |

## 5. Manutenção (clean)
| Rotina | Regra |
|---|---|
| Decay — confiança ao longo do tempo | Selo de fonte mostra a idade dos dados (minutos do GitHub ou data do snapshot) |
| Dedupe — mesclar entradas similares | Mescla por número da issue |
| TTL expiry — expirar registros obsoletos | Cache do GitHub expira em 10 min; snapshot regerado a cada mudança no workbook |

## 6. Contrato
| Entradas | Saídas | Ferramentas / permissões |
|---|---|---|
| Clones do workbook, registro de tarefas do plano, issues #3/#5 do GitHub, modelo do PDF | 2 views do painel e 2 PDFs de uma página | Worker com sessão; leitura pública do GitHub (`GITHUB_TOKEN` opcional, só leitura) |

<!-- Ficha schema (TPL-023, ref. "Anatomy of memory systems"). Obrigatória junto da ficha CV. -->
