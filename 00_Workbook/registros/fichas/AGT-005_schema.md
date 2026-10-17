---
id: AGT-005
type: ficha_schema
entity_type: agente
nome: blog-publisher
macroarea_id: A11
dominio_id: null
owner: MA.AGT
owner_pessoa: null
status: draft
version: 0.1.0
updated: 2026-10-17
source_refs: [Programaex/design .claude/agents/blog-publisher.md]
---
<!-- page -->
# blog-publisher · Anatomia

## 1. Gatilhos de escrita
| Gatilho | Descrição |
|---|---|
| Execução de tarefa | GAP |
| Input do usuário | GAP |
| Saída de ferramenta | GAP |
| Decisão do agente | GAP |

## 2. Armazenamentos (4 tipos)
| Tipo | Conteúdo | Backend |
|---|---|---|
| Working | estado da tarefa: GAP | GAP |
| Episodic | execuções passadas: GAP | GAP |
| Semantic | fatos e preferências: GAP | GAP |
| Procedural | fluxos aprendidos: GAP | GAP |

## 3. Decisão de contexto — cabe no orçamento? (trust + recência)
- Sim → injeta no contexto: GAP
- Não ou obsoleto → loop de busca até verificar e atualizar: GAP

## 4. Write policy (gatekeeper)
| Controle | Critério |
|---|---|
| Gate — importância / confiança | GAP |
| Trust — proveniência / rank da fonte | GAP |
| Validate → Admit | GAP |

## 5. Manutenção (clean)
| Rotina | Regra |
|---|---|
| Decay — confiança ao longo do tempo | GAP |
| Dedupe — mesclar entradas similares | GAP |
| TTL expiry — expirar registros obsoletos | GAP |

## 6. Contrato
| Entradas | Saídas | Ferramentas / permissões |
|---|---|---|
| GAP | GAP | Bash, Read, Write, Edit, Glob, Grep, mcp__github__create_pull_request, mcp__github__list_pull_requests, mcp__github__get_file_contents |

<!-- Ficha schema (TPL-023, ref. "Anatomy of memory systems"). Obrigatória junto da ficha CV. -->
