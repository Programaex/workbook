---
id: TPL-001
type: template
title: Fichas Schema — Ecossistema Executar
owner: TD.ENG
co_owners: [PD.PRO]
areas: [D12, D10]
status: draft
version: 0.1.0
updated: 2026-10-17
sources: [ID_01_ENGENHARIA WORKFLOW E REGRAS]
---
<!-- Owner por bloco (primário = TD.ENG; co-owner = PD.PRO):
     F00 Ficha mestre ........ TD.ENG
     F01 Product Brief ....... PD.PRO (produto) com handoff a TD.ENG
     F02 Engineering Assessment TD.ENG
     Índice do portfólio ..... PD.PRO
     Template adoption, ADR, Quality gates, Cartão de ação, Contrato de conclusão, Estado operacional ... TD.ENG
     IDs deste documento (ECO-, PROD-, F0x, ADR-, ENG-) são provisórios até conciliar com o índice mestre. -->

# FICHAS SCHEMA — Ecossistema Executar (com placeholders)

Fonte: ID_01_ENGENHARIA WORKFLOW E REGRAS (leitura integral).
Convenções do documento: dado desconhecido = `A DEFINIR`; comportamento inferido = `HIPÓTESE`; nenhuma tecnologia é definitiva só pelo nome do produto; IDs são provisórios até conciliar com o índice mestre.

---

## F00 — FICHA MESTRE DO ECOSSISTEMA (1 por ecossistema)

| Campo | Valor |
|---|---|
| ID | {{ECO_ID}} (ex.: ECO-001) |
| Nome | {{ECOSYSTEM_NAME}} |
| Estado inicial | {{GREENFIELD \| BROWNFIELD}} — baseline {{ZERO \| ...}} |
| Organização | {{MONOREPO_MODULAR \| MULTIREPO \| A DEFINIR}} |
| Hospedagem preferencial | {{HOSTING}} |
| Linguagem | {{LANGUAGE}} |
| Gerenciamento de pacotes | {{PACKAGE_MANAGER}} |
| Orquestração de build | {{BUILD_ORCHESTRATOR}} |
| Banco de dados | {{DATABASE \| A DEFINIR}} |
| Autenticação | {{AUTH \| A DEFINIR}} |
| Design System | {{DESIGN_SYSTEM_SCOPE}} |
| Repositório de destino | {{REPO_URL \| A DEFINIR}} |
| Ambientes | {{DEV}}, {{PREVIEW}}, {{PRODUCTION}} |
| Regra de início | {{START_RULE}} (ex.: sem implementação antes do gate técnico) |
| Ferramenta de desenvolvimento assistido | {{DEV_AGENT_TOOL \| A CONFIRMAR}} |

---

## F01 — PRODUCT BRIEF (1 por produto ou capacidade funcional)

```
ID: {{PRODUCT_ID}}
VERSION: {{VERSION}}
STATUS: {{DRAFT | REVIEW | APPROVED}}
OWNER: {{OWNER | A DEFINIR}}
ECOSYSTEM: {{ECO_ID}}
```

### 1. Identificação
- Nome: {{PRODUCT_NAME}}
- Tipo: {{SITE | WEB_APP | MOBILE | SERVICE | MODULE}}
- Objetivo: {{QUAL_RESULTADO_ENTREGA}}
- Público: {{QUEM_UTILIZA}}

### 2. Comportamento funcional
- Problema: {{PROBLEMA_QUE_RESOLVE}}
- Funcionalidades essenciais: {{TOP_3_A_5}}
- Jornada principal: {{ENTRADA → AÇÃO → RESULTADO}}
- Resultado verificável: {{CRITERIO_DE_SUCESSO}}

### 3. Operação
- Acesso: {{PUBLICO | AUTENTICADO | INTERNO}}
- Dispositivos: {{WEB | MOBILE | DESKTOP}}
- Conectividade: {{ONLINE | OFFLINE | HIBRIDO}}
- Dados: {{O_QUE_PRECISA_SALVAR}}
- Integrações: {{OUTROS_PRODUTOS_OU_SERVICOS}}

### 4. Entrega inicial
- MVP: {{O_QUE_ENTRA_NA_V1}}
- Fora do escopo: {{O_QUE_FICA_PARA_DEPOIS}}
- Restrições obrigatórias: {{REQUISITOS_NAO_NEGOCIAVEIS}}
- Referências: {{LINKS_OU_ARQUIVOS_OPCIONAIS}}

```
DEPENDS_ON: {{IDS | A DEFINIR}}
BLOCKS: {{IDS | A DEFINIR}}
AUTOMATION_LEVEL: {{A1 — Preparação | ...}}
HANDOFF: {{Engenharia / F02}}
```

### 5. (Opcional) Extração de repositório legado — Repository Discovery
Regra: extrair o comportamento do produto, não reproduzir a arquitetura técnica. Código original não é modificado.

| Informação | Tratamento | Valor |
|---|---|---|
| Funcionalidades identificadas | Registrar na F01 | {{FEATURES}} |
| Jornada e navegação | Registrar na F01 | {{JOURNEY}} |
| Dados e integrações observadas | Requisito candidato | {{DATA_INTEGRATIONS}} |
| Design System encontrado | Catalogar separadamente | {{DESIGN_SYSTEM_FOUND}} |
| Framework antigo | Inventário técnico AS-IS, fora da decisão F01 | {{LEGACY_STACK}} |
| Código reutilizável | Candidato à avaliação futura | {{REUSABLE_CODE}} |
| Funcionalidade não identificada | A DEFINIR | {{UNKNOWN}} |
| Comportamento inferido | HIPÓTESE | {{HYPOTHESES}} |
| Evidência | Repositório, caminho, arquivo, commit | {{REPO}} / {{PATH}} / {{FILE}} / {{COMMIT}} |

Saídas: F01 Product Brief, AS-IS Technical Inventory, Evidence Index, Gap Report.

---

## F02 — ENGINEERING ASSESSMENT (1 por aplicação ou serviço candidato; preenchida pela engenharia a partir de F00 + F01)

```yaml
id: {{F02_ID}}
product_id: {{PRODUCT_ID}}
ecosystem_id: {{ECO_ID}}
status: {{PROPOSED | VALIDATED | REJECTED | BLOCKED}}
application_boundary: {{ROTA | MODULO | PACKAGE | APP | SERVICO}}
framework: {{FRAMEWORK}}
rendering_strategy: {{ESTATICO | SSR | SPA | HIBRIDO}}
runtime: {{NAVEGADOR | WORKERS | NODE | MOBILE_NATIVO}}
data_strategy: {{O_QUE_PERSISTE_E_ONDE}}
authentication: {{QUEM_ACESSA_E_ALTERA}}
integrations: {{CONTRATOS_COM_OUTROS_SISTEMAS}}
cloudflare_services: {{WORKERS | D1 | R2 | KV | QUEUES | WORKFLOWS | NENHUM}}
template_candidates: {{LISTA}}
quality_requirements: {{PERFORMANCE | SEGURANCA | ACESSIBILIDADE | TESTES}}
dependencies: {{O_QUE_PRECISA_EXISTIR_ANTES}}
verification: {{COMO_COMPROVAR}}
decision_justification: {{JUSTIFICATIVA}}
decision_source: {{FONTE}}
```

### Teste de separação (rota/módulo vs. app) — 5 perguntas
| Fronteira | Pergunta | Resposta |
|---|---|---|
| Deploy | Precisa ser publicada/revertida sem republicar a Web? | {{S/N}} |
| Infraestrutura | Exige runtime, servidor, worker ou build muito diferente? | {{S/N}} |
| Segurança | Possui permissões, credenciais ou superfície própria? | {{S/N}} |
| Operacional | Precisa escalar CPU, memória ou filas separadamente? | {{S/N}} |
| Manutenção | Ciclo de desenvolvimento e testes independente? | {{S/N}} |

Ferramenta de triagem, não regra automática.

---

## ÍNDICE DO PORTFÓLIO (inventário F01)

| ID proposto | Produto / capacidade | Requisitos iniciais conhecidos | Situação | Prioridade |
|---|---|---|---|---|
| {{PROD-00X}} | {{NOME}} | {{REQUISITOS}} | {{Parcial \| Lacunas \| Validado}} | {{P0–P4}} |

---

## ADOÇÃO DE TEMPLATE (obrigatório antes de importar)

| Campo | Valor |
|---|---|
| Template | {{TEMPLATE_NAME}} |
| Repositório de origem | {{SOURCE_REPO}} |
| Commit ou versão | {{COMMIT_OR_VERSION}} |
| Licença | {{LICENSE}} |
| Dependências | {{DEPENDENCIES}} |
| Compatibilidade (ambiente) | {{COMPATIBILITY}} |
| Vulnerabilidades conhecidas | {{VULNERABILITIES}} |
| Alterações pós-importação | {{CHANGES}} |

---

## ADR (derivado de F02)

```
ADR-{{AREA}}-{{NNN}} · VERSION {{V}} · STATUS: {{PROPOSED | VALIDATED | REJECTED | BLOCKED}}
Título: {{TITLE}}
Decisão: {{DECISION}}
Justificativa: {{JUSTIFICATION}}
Fonte: {{SOURCE}}
Aceite pendente: {{PENDING_ACCEPTANCE}}
```

---

## QUALITY GATES

| Gate | Evidência necessária | Libera | Estado |
|---|---|---|---|
| G00 Portfólio | Produtos e relações identificados | Fichas F01 | {{ESTADO}} |
| G01 Requisitos | F01 com lacunas críticas resolvidas | Assessment | {{ESTADO}} |
| G02 Arquitetura | F02, dependências e restrições | Busca de templates | {{ESTADO}} |
| G03 Template | Origem, licença, compatibilidade e testes | ADR | {{ESTADO}} |
| G04 Decisão | ADR aprovado e registrado | Importação | {{ESTADO}} |
| G05 Engenharia | Build, testes, estrutura e preview válidos | Desenvolvimento | {{ESTADO}} |
| G06 Release | Critérios de aceite e evidências | Produção | {{ESTADO}} |

---

## CARTÃO DE AÇÃO EXECUTÁVEL

```
{{ENG-NNN}} · {{TITLE}}                       STATUS: {{NOT STARTED | IN PROGRESS | DONE}}
Objetivo: {{OBJECTIVE}}
Você: {{USER_RESPONSIBILITY}}
Claude Code: {{AGENT_RESPONSIBILITY}}
Evidência de aceite: {{ACCEPTANCE_EVIDENCE}}
Próxima tarefa desbloqueada: {{NEXT_TASK}}
```

## CONTRATO DE CONCLUSÃO (relatório do agente)

```
STATUS: {{STATUS}}
DELIVERABLES: {{DELIVERABLES}}
EVIDENCE: {{EVIDENCE}}
VALIDATION: {{VALIDATION}}
BLOCKERS: {{BLOCKERS}}
NEXT_ACTION: {{NEXT_ACTION}}
```

## ESTADO OPERACIONAL

| Controle | Estado |
|---|---|
| WORKFLOW | {{WORKFLOW_NAME}} |
| VERSION | {{VERSION}} |
| BASELINE | {{BASELINE}} |
| PRODUCT_INVENTORY | {{N}} candidatos |
| F00 / F01 / F02 | {{ESTADO}} |
| ADR | {{ESTADO}} |
| REPOSITORY_IMPORT | {{ESTADO}} |
| DEPLOY | {{ESTADO}} |
| AUTOMATION_LEVEL | {{NIVEL}} |
| NEXT_WORKFLOW | {{NEXT_WORKFLOW}} |
