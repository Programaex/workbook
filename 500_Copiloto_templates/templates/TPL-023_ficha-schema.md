---
id: {EID}
type: {FTYPE}
entity_type: {ETYPE}
nome: {NOME}
macroarea_id: {AREA_ID}
dominio_id: {DOM}
owner: {OWNER}
owner_pessoa: null
status: {STATUS}
version: 0.1.0
updated: {DATE}
source_refs: {SOURCE_REFS}
---
<!-- page -->
# {NOME} · Anatomia

## 1. Gatilhos de escrita
| Gatilho | Descrição |
|---|---|
| Execução de tarefa | {G_TAREFA} |
| Input do usuário | {G_INPUT} |
| Saída de ferramenta | {G_TOOL} |
| Decisão do agente | {G_DECISAO} |

## 2. Armazenamentos (4 tipos)
| Tipo | Conteúdo | Backend |
|---|---|---|
| Working | estado da tarefa: {M_WORKING} | {B_WORKING} |
| Episodic | execuções passadas: {M_EPISODIC} | {B_EPISODIC} |
| Semantic | fatos e preferências: {M_SEMANTIC} | {B_SEMANTIC} |
| Procedural | fluxos aprendidos: {M_PROCEDURAL} | {B_PROCEDURAL} |

## 3. Decisão de contexto — cabe no orçamento? (trust + recência)
- Sim → injeta no contexto: {CTX_SIM}
- Não ou obsoleto → loop de busca até verificar e atualizar: {CTX_NAO}

## 4. Write policy (gatekeeper)
| Controle | Critério |
|---|---|
| Gate — importância / confiança | {WP_GATE} |
| Trust — proveniência / rank da fonte | {WP_TRUST} |
| Validate → Admit | {WP_ADMIT} |

## 5. Manutenção (clean)
| Rotina | Regra |
|---|---|
| Decay — confiança ao longo do tempo | {MN_DECAY} |
| Dedupe — mesclar entradas similares | {MN_DEDUPE} |
| TTL expiry — expirar registros obsoletos | {MN_TTL} |

## 6. Contrato
| Entradas | Saídas | Ferramentas / permissões |
|---|---|---|
| {C_IN} | {C_OUT} | {C_TOOLS} |

<!-- Ficha schema (TPL-023, ref. "Anatomy of memory systems"). Obrigatória junto da ficha CV. -->
