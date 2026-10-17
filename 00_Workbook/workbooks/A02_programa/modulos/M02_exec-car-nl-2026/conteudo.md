---
id: WB-A02-M02-CNT
type: content
workbook_id: WB-A02
macroarea_id: A02
owner: MA.PRG
title: EXEC-CAR-NL-2026 · Carreira AI Transformation NL
status: draft
version: 0.1.0
updated: 2026-10-17
source_refs: [SRC-001, SRC-002, SRC-003]
---
<!-- page -->
# EXEC-CAR-NL-2026 · Carreira AI Transformation NL — Conteúdo

<!-- owner: MA.PRG (todos os blocos). Fontes: data/SOURCE_REGISTER.csv (SRC-001 contrato do anexo; SRC-002 rascunhos USER_CLAIM; SRC-003 relatório de pesquisa). -->

## Como ler
Este módulo traduz o OUTPUT CONTRACT (SRC-001, `Gtm_Profissional.md` l.269–313) em saídas gerenciais numeradas. Cada número citado vem de uma das 23 tabelas em `data/`; os IDs (`JOB-`, `CERT-`, `GAP-`, `TASK-`, `DEC-`, `RISK-`, `EVD-`) são as chaves para conferir a linha de origem. Rótulos como `NOT_VERIFIED`, `PENDING_OFFICIAL_VERIFICATION`, `ESTIMATE`, `PROPOSED` e `USER_CLAIM` são mantidos literalmente: indicam pendência, não fato.

## Resumo executivo
A amostra de 17/10/2026 tem 87 registros de vagas, dos quais 52 estão `VERIFIED_ACTIVE`. O gargalo para o alvo AI Transformation Manager não é certificação: é neerlandês (exigido explicitamente em 26/52), anos de experiência comprovados e um baseline ainda `NOT_VERIFIED`. A rota de certificação proposta é enxuta (AIGP como MAIN; UiPath AAA e PSPO I como OPTIONAL), sem nenhuma prova reservada ou paga.

## Conclusão
As decisões estruturais estão todas em estado `PROPOSED` e dependem de aprovação do usuário (`data/DECISION_LOG.csv`). Nenhuma ação externa (alterar repositórios, publicar, candidatar, pagar, contatar) é executada sem autorização explícita.

## Dados
Tabelas usadas nesta parte: `data/JOBS_VERIFIED.csv`, `data/JOB_REQUIREMENTS.csv`, `data/CAPABILITY_DICTIONARY.csv`, `data/CERTIFICATIONS.csv`, `data/COURSE_CATALOG.csv`, `data/SYLLABUS_MODULES.csv`, `data/EXAM_GATES.csv`, `data/BUDGET.csv`, `data/ROADMAP_WEEKLY.csv`, `data/EPICS_ISSUES_TASKS.csv`, `data/REPOSITORY_AUDIT.csv`, `data/PORTFOLIO_EVIDENCE.csv`, `data/GAP_BACKLOG.csv`, `data/RISK_REGISTER.csv`, `data/DECISION_LOG.csv`, `data/EXECUTIVE_DASHBOARD.csv`, `data/SOURCE_REGISTER.csv`. Índice de todos os IDs: `data/MASTER_INDEX.csv`.

## Introdução
Saídas desta parte: 1 · Executive one-page; 2 · Headhunter Market Report; 3 · Curriculum & Certification Plan; 4 · Weekly Master Schedule; 5 · Evidence Gap Report. As saídas 6–9 (Portfolio Specification, Employment & Relocation Plan, Dynamic Career Fit Dashboard e Source & Assumption Ledger) seguem em continuação deste arquivo.

## Desenvolvimento
As tabelas longas foram geradas diretamente dos CSVs, sem transcrição manual. Contagens de mercado são **contagens amostrais**, nunca totais de mercado. Textos de células preservam o idioma original do registro (em geral inglês).

## Conexão
Workbook `WB-A02` (macroárea A02, owner `MA.PRG`). Registros canônicos transversais ficam em `00_Workbook/registros/`; este módulo referencia por ID e não copia registros canônicos. O vínculo rotas↔macroáreas permanece escopo do ADR-002.

## PDCPA
Ciclo de revisão: **Planejar** pelo `data/ROADMAP_WEEKLY.csv` (40 h/semana); **Executar** pelas tarefas de `data/EPICS_ISSUES_TASKS.csv`; **Checar** no ritual semanal (TASK-0013: planejado vs. real, KPI-001..KPI-004 em `data/EXECUTIVE_DASHBOARD.csv`) e nas marcas de recálculo de FIT de 30/60/90 dias (2026-11-18, 2026-12-18, 2027-01-17); **Agir** replanejando desvios (sem escondê-los) e na revisão mensal CONTINUE/DEFER/DROP das credenciais opcionais e adiadas (EPIC-09). Riscos têm cadência própria (semanal, quinzenal ou mensal) em `data/RISK_REGISTER.csv`.

<!-- page -->
# 1 · Executive one-page

**Posição-alvo (longo prazo):** AI Transformation Manager — nas vagas reais da família pede 8+ anos de consultoria e ≥1 projeto de adoção de IA entregue (JOB-T-001) ou 5–10 anos (JOB-T-002, JOB-T-003). **Posições-ponte:** júnior de inovação/adoção, AI Project Lead/BA, trainee agentic, governança mid e freelance de automação para PMEs (SRC-003 §1). **Datas rígidas:** 2026-10-19 início · 2026-11-19 épico Emprego & Realocação (EPIC-07) · 2027-02-01 a 2027-03-30 candidaturas formais · 2027-04-30 viagem.

**Baseline:** apenas cidadania UE e inglês fluente declarados (`USER_CLAIM`). `NOT_VERIFIED`: CV, LinkedIn, histórico de trabalho, anos por função, diploma (HBO/WO), nível de neerlandês (KPI-017), certificações existentes, orçamento (KPI-018) e cidades (GAP-002; DEC-010). Evidência de portfólio: L3 em Agentic AI/Automation e Arquitetura; nenhuma L4 (KPI-009 = 0).

**Top 5 lacunas** (`data/GAP_BACKLOG.csv`):

| # | GAP | Lacuna | Prioridade | Data-alvo |
|---|---|---|---|---|
| 1 | GAP-001 | Nível de neerlandês desconhecido (explícito em 26/52) | P0 | 2026-10-23 (PROPOSED) |
| 2 | GAP-002 · GAP-006 | Baseline profissional e anos de experiência não comprovados | P0 | 2026-10-19 / 2026-10-23 (PROPOSED) |
| 3 | GAP-004 | Sem artefatos EU AI Act / ISO 42001 | P1 | 2026-11-13 (PROPOSED; v0 2026-10-23) |
| 4 | GAP-007 | Nenhuma evidência L4 / adoção por terceiros | P1 | 2027-01-29 (PROPOSED) |
| 5 | GAP-003 · GAP-005 · GAP-021 | Portfólio ainda não seguro nem em inglês; redação e atribuição | P0 / P1 | 2026-10-20 a 2026-10-25 (PROPOSED) |

**5 ações desta semana** (WK-01, 2026-10-19 a 2026-10-25):

| # | Tarefa | Ação | Horas | Autorização |
|---|---|---|---|---|
| 1 | TASK-0001 | Capture baseline: CV, LinkedIn, work history with years per role, degree + HBO/WO equivalence, Dutch level, existing certs, budget, city preferences | 2 | N |
| 2 | TASK-0004 | Recommend fixing hardcoded fallback login on live Worker and run gitleaks history scan on both repos | 4 | Y |
| 3 | TASK-0007 · TASK-0010 | AIGP BoK v2.1 + diagnóstico G1 por domínio (GATE-002) | 14 | N |
| 4 | TASK-0008 | Check Dutch level with a CEFR placement test and select a course (options NOT_VERIFIED) | 4 | N |
| 5 | TASK-0012 · TASK-0006 | Reverificar USER_CLAIM dos rascunhos e montar o pipeline com as 52 vagas | 4 | N |

**Decisões (todas `PROPOSED`, aguardando o usuário):** DEC-001 (AIGP como MAIN) · DEC-010 (baseline NOT_VERIFIED) · DEC-012/DEC-016/DEC-022 (neerlandês desde a semana 1, dentro de ACTIVE_STUDY) · DEC-013 (não aplicar à Avans, que fecha em 2026-10-20) · DEC-014 (segurança antes de qualquer URL) · DEC-020 (alocação de horas por fase) · DEC-023 (datas de prova PROPOSED, não reservadas). Pendências do usuário: orçamento (G4), autorização para alterar repositórios e publicar (G5), cidade preferida e aceite de início antes de 2027-04-30.

**Riscos principais** (`data/RISK_REGISTER.csv`, score = probabilidade × impacto):

| RISK | Descrição | Score | Mitigação |
|---|---|---|---|
| RISK-001 | Dutch-language filter excludes most roles | 25 | Weekly Dutch study inside ACTIVE_STUDY; target English-first employers; record CEFR level |
| RISK-002 | Experience-years filter blocks MID+ roles | 20 | Honest experience map; target junior/bridge roles; no inflated claims |
| RISK-003 | Baseline remains unverified | 20 | Week-1 intake task; replan if missing; keep NOT_VERIFIED labels |
| RISK-005 | Hardcoded fallback credentials on live site damage credibility | 20 | Confirm secrets or remove fallback (authorised); history scan; no URL before fix |
| RISK-008 | Schedule overload beyond 40 h/week | 16 | BUFFER carve; weekly replanning; drop lowest-ROI tasks first |
| RISK-011 | AI-agent-authored commits framed as own coding | 16 | Authorship narrative: candidate designs/specifies/governs, agent implements |
| RISK-013 | Housing cost and availability delay BRP registration | 16 | Start search by 2027-03-05; budget estimate; temporary address option |

<!-- page -->
# 2 · Headhunter Market Report

## Amostra e método
A amostra foi construída em **2026-10-17** a partir de duas notas independentes (SRC-003 §2). `data/JOBS_VERIFIED.csv` tem **87 registros**; **52 estão VERIFIED_ACTIVE** (página aberta, texto completo, sem aviso de encerramento). Todos os números abaixo são **contagens amostrais, não totais de mercado**. JOB-A-024 foi tratado como STALE e excluído da contagem ativa (DEC-015); as vagas ativas são arquétipos que tendem a expirar antes de 2027-02-01 (DEC-017).

| Amostra | VERIFIED_ACTIVE | UNVERIFIED | EXPIRED | VERIFIED_ARCHIVED | Total |
|---|---|---|---|---|---|
| T (transformação/governança) | 36 | 7 | 5 | 5 | 53 |
| A (automação/produto/processo) | 16 | 8 | 10 | 0 | 34 |
| **Total** | 52 | 15 | 15 | 5 | 87 |

## Distribuição das 52 vagas ativas — senioridade e idioma

| seniority_class | Vagas (N=52) | % |
|---|---|---|
| SENIOR | 12 | 23,1% |
| MID | 12 | 23,1% |
| ENTRY/JUNIOR | 7 | 13,5% |
| FREELANCE/CONTRACT | 7 | 13,5% |
| BRIDGE_ROLE | 5 | 9,6% |
| SENIOR/MANAGER | 3 | 5,8% |
| MID/SENIOR | 3 | 5,8% |
| ENTRY/JUNIOR–MID | 2 | 3,8% |
| SENIOR/MANAGER (Director stretch) | 1 | 1,9% |

| language_req | Vagas (N=52) | % |
|---|---|---|
| NL_REQUIRED | 26 | 50,0% |
| UNKNOWN_NL_AD | 17 | 32,7% |
| UNKNOWN_EN_AD | 4 | 7,7% |
| EN_SUFFICIENT | 4 | 7,7% |
| EN_INFERRED | 1 | 1,9% |

<!-- page -->
# 2 · Headhunter Market Report — distribuições (cont.)

## Família, timing e recomendação

| family | Vagas (N=52) | % |
|---|---|---|
| AI_GOVERNANCE_RISK | 14 | 26,9% |
| AI_TRANSFORMATION_CHANGE | 11 | 21,2% |
| AI_PROJECT_BA_JUNIOR | 11 | 21,2% |
| AUTOMATION_RPA_AGENTIC_PROCESS | 9 | 17,3% |
| FREELANCE_AI_AUTOMATION | 7 | 13,5% |

| timing_class | Vagas (N=52) | % |
|---|---|---|
| TARGET_LATER | 16 | 30,8% |
| APPLY_IN_90D | 14 | 26,9% |
| APPLY_IN_30D | 9 | 17,3% |
| NOT_ELIGIBLE_YET | 6 | 11,5% |
| APPLY_IN_60D | 4 | 7,7% |
| APPLY_NOW | 3 | 5,8% |

| recommendation | Vagas (N=52) | % |
|---|---|---|
| TARGET_LATER | 16 | 30,8% |
| BUILD_FIRST | 16 | 30,8% |
| BRIDGE | 11 | 21,2% |
| NOT_YET_ELIGIBLE | 6 | 11,5% |
| APPLY | 3 | 5,8% |

Classes de timing e recomendação são preliminares e condicionais ao baseline `NOT_VERIFIED`; não são probabilidades de contratação (DEC-010; DEC-011).

<!-- page -->
# 2 · Headhunter Market Report — contrato e modelo de trabalho

## Contrato (valor literal do anúncio; U = não informado)

| contract | Vagas (N=52) |
|---|---|
| U | 21 |
| Freelance | 6 |
| Permanent, 32–40 h | 5 |
| U, 36 h | 2 |
| U (permanent implied, not stated) | 1 |
| 'maatwerk' (custom) | 1 |
| Fixed-term 12 months → permanent intended, 36 h | 1 |
| U, 32 or 40 h | 1 |
| Permanent, 40 h | 1 |
| U (consultant placement) | 1 |
| Fixed-term 1 year, 40 h | 1 |
| 72.5% of own revenue or salary + profit share | 1 |
| Permanent | 1 |
| U (stock options) | 1 |
| 12 months → permanent prospect | 1 |
| U (13th month) | 1 |
| Fixed-term 12 months → permanent prospect | 1 |
| U, 36–40 h | 1 |
| U, 32–40 h | 1 |
| Traineeship ~6–9 months, full-time; option to join client permanently | 1 |
| Permanent (startup) | 1 |
| Freelance (fixed fee) | 1 |

## Modelo de trabalho

| work_model | Vagas (N=52) |
|---|---|
| U | 21 |
| Hybrid | 14 |
| Remote | 4 |
| Hybrid, 32/36/40 h | 1 |
| Office 3 days/week | 1 |
| Hybrid (3 days office/client) | 1 |
| Up to 4 weeks/yr from abroad | 1 |
| Hybrid, 32–36 h | 1 |
| Hybrid, 4 days at client | 1 |
| Up to 4 days WFH; Wednesday office | 1 |
| 4 days WFH; Wednesday office | 1 |
| Hybrid, usually at client | 1 |
| U (hybrid per snippet, UNVERIFIED) | 1 |
| On-site 'often' | 1 |
| In office with WFH flexibility | 1 |
| On-site | 1 |

<!-- page -->
# 2 · Headhunter Market Report — vagas VERIFIED_ACTIVE (1/3)

Fonte: `data/JOBS_VERIFIED.csv` (verified_at 2026-10-17). URL e fonte de cada vaga na própria linha do CSV.

| ID | Empresa | Cargo | Cidade | Senioridade | Idioma | Contrato | Timing | Recomendação |
|---|---|---|---|---|---|---|---|---|
| JOB-T-001 | Eraneos | (Senior) Manager AI Transformatie | Randstad (multiple cities) | SENIOR/MANAGER | NL_REQUIRED | U (permanent implied, not stated) | TARGET_LATER | TARGET_LATER |
| JOB-T-002 | Anderson MacGyver | AI Transformation Consultant | IJsselstein (Utrecht) | SENIOR | NL_REQUIRED | U | TARGET_LATER | TARGET_LATER |
| JOB-T-003 | Fellowmind | AI Transformation Consultant | Zwolle (twin posting Deventer) | SENIOR | NL_REQUIRED | U | TARGET_LATER | TARGET_LATER |
| JOB-T-004 | accelerAite | Medior AI Verandermanager | 's-Hertogenbosch | MID | UNKNOWN_NL_AD | Permanent, 32–40 h | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-005 | Frisse Blikken | Senior Transformation Lead – Mens & AI | Eindhoven | SENIOR | UNKNOWN_NL_AD | 'maatwerk' (custom) | TARGET_LATER | TARGET_LATER |
| JOB-T-006 | Accenture | Transformational Change Manager | Amsterdam | SENIOR/MANAGER | NL_REQUIRED | U | TARGET_LATER | TARGET_LATER |
| JOB-T-007 | Accenture | Junior Technology Strategy & Transformation Consultant | Amsterdam | ENTRY/JUNIOR | NL_REQUIRED | U | NOT_ELIGIBLE_YET | NOT_YET_ELIGIBLE |
| JOB-T-008 | Add Value (client: Utrecht-region digital transformation consultancy) | AI Adoptie specialist | Den Bosch (client Utrecht region) | MID | NL_REQUIRED | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-009 | DICTU (Rijksoverheid) | Senior Adviseur AI | Assen / Den Haag / Zwolle | SENIOR | UNKNOWN_NL_AD | Fixed-term 12 months → permanent intended, 36 h | TARGET_LATER | TARGET_LATER |
| JOB-T-010 | BearingPoint | Microsoft Business Transformation Consultant Data & AI | Amsterdam | SENIOR | NL_REQUIRED | U | TARGET_LATER | TARGET_LATER |
| JOB-T-011 | Corbion | Global Head of Digital, Data & AI | Amsterdam / Gorinchem | SENIOR/MANAGER (Director stretch) | UNKNOWN_EN_AD | U | TARGET_LATER | TARGET_LATER |
| JOB-T-012 | Athora Netherlands | AI Governance Specialist | Amsterdam | MID | UNKNOWN_NL_AD | U, 36 h | APPLY_IN_60D | BUILD_FIRST |
| JOB-T-013 | Deloitte | AI Risk Manager | Rotterdam | SENIOR | NL_REQUIRED | U, 32 or 40 h | TARGET_LATER | TARGET_LATER |
| JOB-T-014 | EY | Manager Privacy & Responsible AI | Amsterdam | SENIOR/MANAGER | NL_REQUIRED | Permanent, 40 h | TARGET_LATER | TARGET_LATER |
| JOB-T-015 | Everience Benelux | Responsible AI Lead | Den Haag | SENIOR | UNKNOWN_EN_AD | U (consultant placement) | APPLY_IN_60D | BRIDGE |
| JOB-T-016 | Atos | Senior AI Consultant – AI Trust & Governance | Amstelveen | SENIOR | NL_REQUIRED | U | TARGET_LATER | TARGET_LATER |
| JOB-T-017 | CGI Nederland | Senior Data & AI Governance Specialist (Retail & Consumer Products) | Amsterdam | SENIOR | NL_REQUIRED | U | NOT_ELIGIBLE_YET | NOT_YET_ELIGIBLE |
| JOB-T-018 | KPMG Nederland | Senior Consultant – Technology Assurance – AI | Rotterdam / Den Haag | MID | NL_REQUIRED | U | APPLY_IN_60D | BUILD_FIRST |

<!-- page -->
# 2 · Headhunter Market Report — vagas VERIFIED_ACTIVE (2/3)

Fonte: `data/JOBS_VERIFIED.csv` (verified_at 2026-10-17). URL e fonte de cada vaga na própria linha do CSV.

| ID | Empresa | Cargo | Cidade | Senioridade | Idioma | Contrato | Timing | Recomendação |
|---|---|---|---|---|---|---|---|---|
| JOB-T-019 | Avans University of Applied Sciences | AI Compliance Officer | Breda | BRIDGE_ROLE | UNKNOWN_NL_AD | Fixed-term 1 year, 40 h | NOT_ELIGIBLE_YET | NOT_YET_ELIGIBLE |
| JOB-T-020 | Younicorp | AI Governance Specialist | U (Arnhem area code; public-sector clients) | MID | NL_REQUIRED | 72.5% of own revenue or salary + profit share | TARGET_LATER | TARGET_LATER |
| JOB-T-021 | PwC Nederland | (Senior) Associate – Legal Tech / Responsible AI | Amsterdam | BRIDGE_ROLE | NL_REQUIRED | Permanent | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-022 | Deeploy | Partner Manager, AI Governance | Amsterdam | BRIDGE_ROLE | EN_SUFFICIENT | U (stock options) | APPLY_NOW | APPLY |
| JOB-T-023 | MIVD (Rijksoverheid) | AI management adviseur | Zoetermeer | SENIOR | NL_REQUIRED | U | NOT_ELIGIBLE_YET | NOT_YET_ELIGIBLE |
| JOB-T-024 | ABN AMRO | Strategy Advisor – Data & AI | Amstelveen | SENIOR | UNKNOWN_EN_AD | U, 36 h | APPLY_IN_60D | BRIDGE |
| JOB-T-025 | Zanders | AI Consultant – Financial Services & Risk | Utrecht | MID/SENIOR | EN_SUFFICIENT | U | TARGET_LATER | TARGET_LATER |
| JOB-T-026 | Talent&Pro | IT & AI Projectleider (Medior) | Utrecht | BRIDGE_ROLE | UNKNOWN_NL_AD | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-027 | KickstartAI | Project Manager Machine Learning & AI | Delft | MID | UNKNOWN_NL_AD | 12 months → permanent prospect | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-028 | Verwater Group | Business Analist Digitalisering & AI | Rotterdam | ENTRY/JUNIOR | NL_REQUIRED | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-029 | TADA Solutions | Business Analyst Data & AI | Eindhoven | ENTRY/JUNIOR | NL_REQUIRED | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-030 | TalentSpark by TSP | Junior AI Consultant | Rotterdam | ENTRY/JUNIOR | NL_REQUIRED | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-031 | Loyens & Loeff | Junior Innovation Advisor | Amsterdam | ENTRY/JUNIOR | EN_SUFFICIENT | U | APPLY_NOW | APPLY |
| JOB-T-032 | ING Nederland | Agentic automation & AI Consultant | Amsterdam | MID | UNKNOWN_EN_AD | U (13th month) | APPLY_IN_30D | BRIDGE |
| JOB-T-033 | Gaide | AI Consultant | Amsterdam | MID | NL_REQUIRED | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-T-034 | CGI Nederland | AI Consultant – Energie | Arnhem | MID | NL_REQUIRED | Permanent, 32–40 h | TARGET_LATER | TARGET_LATER |
| JOB-T-035 | Inspectie Leefomgeving en Transport (ILT, Rijksoverheid) | Adviseur data science en AI | Utrecht | SENIOR | NL_REQUIRED | Fixed-term 12 months → permanent prospect | NOT_ELIGIBLE_YET | NOT_YET_ELIGIBLE |
| JOB-T-036 | Bit Traineeship | Traineeship AI & Innovation (Dutch speaking) | Amsterdam area | ENTRY/JUNIOR | NL_REQUIRED | U | APPLY_IN_90D | BUILD_FIRST |

<!-- page -->
# 2 · Headhunter Market Report — vagas VERIFIED_ACTIVE (3/3)

Fonte: `data/JOBS_VERIFIED.csv` (verified_at 2026-10-17). URL e fonte de cada vaga na própria linha do CSV.

| ID | Empresa | Cargo | Cidade | Senioridade | Idioma | Contrato | Timing | Recomendação |
|---|---|---|---|---|---|---|---|---|
| JOB-A-001 | CareerValue (recruiter; unnamed Randstad client) | RPA Developer (UiPath) | Utrecht | ENTRY/JUNIOR–MID | NL_REQUIRED | Permanent, 32–40 h | APPLY_IN_90D | BUILD_FIRST |
| JOB-A-002 | CareerValue (recruiter; unnamed client) | RPA Developer (UiPath) | Rotterdam | ENTRY/JUNIOR–MID | NL_REQUIRED | Permanent, 32–40 h | APPLY_IN_90D | BUILD_FIRST |
| JOB-A-003 | PMT Groep | RPA Consultant | Gouda / Randstad clients | MID | NL_REQUIRED | U, 36–40 h | APPLY_IN_90D | BUILD_FIRST |
| JOB-A-004 | ilionx | RPA Developer (Hyperautomation team) | 's-Hertogenbosch / Amersfoort | MID/SENIOR | UNKNOWN_NL_AD | U | APPLY_IN_90D | BUILD_FIRST |
| JOB-A-005 | Itility | Power Platform Consultant/Engineer | Eindhoven / Heerlen | MID | NL_REQUIRED | U | TARGET_LATER | TARGET_LATER |
| JOB-A-006 | Alliander | Process Mining Analist | Arnhem | MID/SENIOR | UNKNOWN_NL_AD | U, 32–40 h | TARGET_LATER | TARGET_LATER |
| JOB-A-008 | Capgemini Engineering | Junior Automation Engineer | Utrecht / Eindhoven / client site | ENTRY/JUNIOR | UNKNOWN_NL_AD | Permanent, 32–40 h | NOT_ELIGIBLE_YET | NOT_YET_ELIGIBLE |
| JOB-A-009 | The Automation Group | Trainee Programme: reskill into Agentic AI Engineer or Consultant | Utrecht + client sites | BRIDGE_ROLE | EN_SUFFICIENT | Traineeship ~6–9 months, full-time; option to join client permanently | APPLY_NOW | APPLY |
| JOB-A-010 | Nanzen | AI/agents engineer | Amsterdam (also Madrid) | MID | EN_INFERRED | Permanent (startup) | APPLY_IN_30D | BRIDGE |
| JOB-A-017 | Small business | Ondersteuning bij inrichten Copilot agents en Power Automate | Delfzijl | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance | APPLY_IN_30D | BRIDGE |
| JOB-A-018 | Consultancy building client AI solutions | AI developer gezocht | Remote | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance | APPLY_IN_30D | BRIDGE |
| JOB-A-019 | AI agency for SMEs | Freelance AI-consultants en engineers | Remote | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance | APPLY_IN_30D | BRIDGE |
| JOB-A-020 | Company using Claude, ChatGPT and HeyGen | Opzetten AI-structuur en workflows op locatie | Noordwijkerhout (on-site) | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance | APPLY_IN_30D | BRIDGE |
| JOB-A-021 | AI assistants for freelancers and SMEs | Freelance developer: Hermes en n8n | Remote | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance | APPLY_IN_30D | BRIDGE |
| JOB-A-022 | Real-estate chatbot/WhatsApp startup | AI-specialist voor afronding/lancering AI-platform | Rotterdam | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance (fixed fee) | APPLY_IN_30D | BRIDGE |
| JOB-A-023 | AI 'executive operator' across Gmail/Calendar/CRM | AI specialist: Lindy opstart en integratie | Remote | FREELANCE/CONTRACT | UNKNOWN_NL_AD | Freelance | APPLY_IN_30D | BRIDGE |

<!-- page -->
# 2 · Headhunter Market Report — frequência de habilidades

Contagem de vagas ativas distintas que citam cada capacidade em `data/JOB_REQUIREMENTS.csv` (295 requisitos parafraseados), cruzada com `data/CAPABILITY_DICTIONARY.csv`. **Amostra, não mercado.** "Bloqueante" = MUST_HAVE com `blocking = Y`.

| CAP | Área | Capacidade | Vagas (N=52) | Vagas com MUST_HAVE bloqueante | Nível atual |
|---|---|---|---|---|---|
| CAP-035 | Transversal – Dutch language | Dutch language | 44 | 26 | NOT_VERIFIED |
| CAP-040 | Transversal – Eligibility/Baseline | Education level (HBO/WO/Master; transcripts) | 28 | 26 | NOT_VERIFIED |
| CAP-039 | Transversal – Eligibility/Baseline | Years of relevant professional experience | 24 | 22 | NOT_VERIFIED |
| CAP-005 | Agentic AI/Automation | Programming (TypeScript/Python/C#) | 14 | 0 | 2 |
| CAP-041 | Transversal – Eligibility/Baseline | Work authorisation, nationality, residence & location | 13 | 7 | NOT_VERIFIED |
| CAP-015 | AI Governance | EU AI Act & AI regulation literacy | 11 | 1 | 0 |
| CAP-001 | Agentic AI/Automation | Agentic AI design & orchestration | 10 | 0 | 3 |
| CAP-034 | Transversal – Professional English | Professional English | 9 | 4 | NOT_VERIFIED |
| CAP-026 | Business Transformation & Change | Change management & adoption | 8 | 0 | 1 |
| CAP-037 | Transversal – Stakeholder mgmt | Stakeholder management & executive advisory | 8 | 0 | NOT_VERIFIED |
| CAP-038 | Transversal – Consulting | Consulting / client-facing advisory experience | 7 | 3 | NOT_VERIFIED |
| CAP-004 | Agentic AI/Automation | LLM application engineering (LLM APIs, RAG, evals, production LLM) | 6 | 0 | 2 |
| CAP-006 | Agentic AI/Automation | Integrations & APIs (MCP, OAuth, webhooks, workflow tools) | 6 | 0 | 3 |
| CAP-012 | Project & Process Mgmt | Process analysis & redesign (BPMN, optimisation) | 6 | 0 | 2 |
| CAP-016 | AI Governance | AI risk & impact assessment (AIIA/DPIA, bias, explainability) | 6 | 0 | 0 |
| CAP-018 | AI Governance | AI governance framework & policy-to-controls design | 6 | 0 | 1 |
| CAP-033 | Transversal – Communication | Communication & documentation | 6 | 0 | 1 |
| CAP-042 | Transversal – Eligibility/Baseline | Regulated/sector domain experience (finance, public, energy) | 6 | 1 | NOT_VERIFIED |
| CAP-003 | Agentic AI/Automation | Microsoft low-code automation & Copilot (Power Platform, Copilot Studio, M365 Copilot) | 5 | 0 | 0 |
| CAP-027 | Business Transformation & Change | AI literacy training & workshop facilitation | 5 | 0 | NOT_VERIFIED |
| CAP-029 | Business Transformation & Change | Delivered AI adoption/transformation project | 5 | 5 | NOT_VERIFIED |
| CAP-032 | Transversal – Architecture/Cloud | Enterprise data & cloud stack (Azure, Fabric, Databricks, AWS/GCP) | 5 | 0 | 0 |

Leitura: os filtros mais frequentes são de elegibilidade (neerlandês, formação, anos, autorização/residência), não técnicos. Na subamostra T (N=36) o relatório registra ainda EU AI Act em 11/36, change/adoção em 11/36 e stack Microsoft em 9/36 (SRC-003 §2).

<!-- page -->
# 2 · Headhunter Market Report — certificações nomeadas literalmente

Linhas de `data/JOB_REQUIREMENTS.csv` com `cert_named_literally` preenchido (somente vagas ativas):

| Vaga | Classe | Certificação literal | Requisito (paráfrase) |
|---|---|---|---|
| JOB-T-007 | NICE_TO_HAVE | Cloud (Azure/AWS/GCP); SAFe; TOGAF; DAMA; FinOps; TBM | Bonus certifications named |
| JOB-T-013 | NICE_TO_HAVE | IAPP AIGP; CCLTE CAICO | Preferred certifications |
| JOB-T-014 | MUST_HAVE | CIPP/E; CIPM; CIPT; 'AI Governance'; ISO 27701 Lead Implementer | Holds certifications ('je beschikt over') |
| JOB-T-017 | MUST_HAVE | DAMA CDMP Practitioner; DCAM | At least one of DAMA CDMP Practitioner or DCAM |
| JOB-T-017 | NICE_TO_HAVE | IAPP AIGP; ISO 42001 | Strong plus certifications |
| JOB-T-018 | MUST_HAVE | RE; CISA; CISM; CIPP | RE or equivalent; candidates studying or willing to start also invited |
| JOB-A-003 | MUST_HAVE | 'relevante certificeringen' (generic; none named) | Relevant certifications in RPA/AI/hyperautomation or intention to obtain (none named) |
| JOB-A-005 | NICE_TO_HAVE | Microsoft PL-100; PL-200; PL-400 | PL certifications (preferred or aim to obtain) |

Nenhuma vaga ativa verificada nos Países Baixos cita PSPO, PRINCE2, PMP, Prosci/ADKAR, UiPath ou OCEB. Prosci obrigatório aparece só em JOB-T-048 (Emirados, OUT_OF_SCOPE); certificações UiPath aparecem apenas em anúncios fora dos Países Baixos (SRC-003 §2; `data/CERTIFICATIONS.csv`, coluna `market_mentions`).

<!-- page -->
# 2 · Headhunter Market Report — filtro de idioma e limitações

## Análise do filtro de idioma

| Classe de idioma | Vagas | IDs |
|---|---|---|
| NL_REQUIRED | 26 | (ver tabela consolidada) |
| UNKNOWN_NL_AD | 17 | (ver tabela consolidada) |
| UNKNOWN_EN_AD | 4 | JOB-T-011; JOB-T-015; JOB-T-024; JOB-T-032 |
| EN_SUFFICIENT | 4 | JOB-T-022; JOB-T-025; JOB-T-031; JOB-A-009 |
| EN_INFERRED | 1 | JOB-A-010 |

- **26/52** exigem neerlandês explicitamente (22/36 na subamostra T; 4/16 na A). Outras **17** não declaram idioma, mas o anúncio é em neerlandês, o que na prática sinaliza neerlandês.
- Apenas **4** aceitam inglês explicitamente (JOB-T-022, JOB-T-025, JOB-T-031, JOB-A-009) e **1** por inferência (JOB-A-010). Quatro anúncios em inglês sem linha de idioma (JOB-T-011, JOB-T-015, JOB-T-024, JOB-T-032) precisam de confirmação com o recrutador.
- Sem neerlandês, o pool realista cai para cerca de **5–9 das 52** vagas (SRC-003 §2, INFERENCE). Por isso o neerlandês entra desde a semana 1 dentro de ACTIVE_STUDY (DEC-012; DEC-016; DEC-022) e é o RISK-001 (score 25).

## Limitações
- Cobertura pesa para o LinkedIn (visualização pública de convidado); Indeed, Glassdoor e Werken voor Nederland renderizam via JavaScript e não puderam ser enumerados.
- 15 registros `UNVERIFIED` (snippets, fetch bloqueado, conflito de cópias, fora de escopo) e 20 `EXPIRED`/`VERIFIED_ARCHIVED` ficam fora da contagem ativa; JOB-A-007 está em conflito entre cópias.
- Requisitos são paráfrases (confiança média); JOB-T-021 (PwC) teve extração incompleta; JOB-T-020 (Younicorp) não tem data e pode ser evergreen.
- Não foram encontradas vagas ativas em organizações internacionais de Den Haag, universidades de pesquisa nem energia in-house (exceto o process mining da Alliander, só via agregador).
- A amostra fica abaixo da meta de 30–50 por família pedida no contrato, embora atenda à meta agregada. Rascunhos do usuário (SRC-002) são `USER_CLAIM` até reverificação (DEC-009; GAP-015).

<!-- page -->
# 3 · Curriculum & Certification Plan — rota de credenciais (1/3)

Regra: uma rota principal por domínio; opcionais só diante de lacuna demonstrada ou exigência recorrente nas vagas. Resultado: **1 MAIN** (CERT-15 AIGP), **2 OPTIONAL** (CERT-05 UiPath AAA; CERT-01 PSPO I), demais **DEFERRED** ou **DROPPED**. Todas em `lifecycle_state = NOT_STARTED`. Preços na moeda original; campos pendentes em `pending_fields` de `data/CERTIFICATIONS.csv`.

| CERT | Credencial | Emissor | Papel | Preço original | Formato | Pré-requisitos | Menções no mercado | Decisão |
|---|---|---|---|---|---|---|---|---|
| CERT-01 | Professional Scrum Product Owner I (PSPO I) | Scrum.org | OPTIONAL | USD 200 per attempt | 80 questions, 60 min (search extract); question types and proctoring PENDING_OFFICIAL_VERIFICATION | None; course optional | 0/52 active ads name it literally (sample count) | DEC-003 (PROPOSED) |
| CERT-02 | Professional Scrum Product Owner – AI Essentials (PSPO-AI) | Scrum.org | DEFERRED | Class price set by trainer (example listing EUR 595 excl. 21% VAT; 2-day EUR 1,295) | 20 multiple-choice questions, 30 min (search extract) | Only for students of the PSPO-AI Essentials class | 0/52 active ads name it literally (sample count) | DEC-003 (PROPOSED) |
| CERT-03 | Professional Scrum Product Owner II (PSPO II) | Scrum.org | DEFERRED | USD 250 | 40 questions (some partial credit), multiple choice + multiple answer, 60 min (search extract) | No course required; PSPO I as formal prerequisite PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally (sample count) | DEC-003 (PROPOSED) |
| CERT-04 | UiPath Certified Professional Automation Developer Associate (UiPath-ADAv1) | UiPath | DEFERRED | USD 150 + tax | EDD V1.6 (Jan 2026), product 2024.10+; 90 min; Pearson VUE test centre or OnVUE; English + Japanese (FAQ) | None | 0/52 active ads name it literally; UiPath named as tool in 5 A records (all Dutch-language); certs only in non-NL ads (sample count) | DEC-002 (PROPOSED) |
| CERT-05 | UiPath Agentic Automation Associate (UiPath-AAAv1) | UiPath | OPTIONAL | USD 150 + tax | EDD V1.1 (Aug 2025); 90 min; Pearson VUE test centre or OnVUE; English + Japanese (FAQ); for technical and non-technical roles | None | 0/52 active ads name it literally; UiPath named as tool in 5 A records (all Dutch-language); certs only in non-NL ads (sample count) | DEC-002 (PROPOSED) |
| CERT-06 | UiPath Agentic Automation Professional (UiPath-AAPv1) | UiPath | DEFERRED | USD 300 + tax | EDD V1.0 (Mar 2026), product 2025.10+; 120 min; MC + drag-and-drop/sequencing; test centre or online proctored | None stated | 0/52 active ads name it literally; UiPath named as tool in 5 A records (all Dutch-language); certs only in non-NL ads (sample count) | DEC-002 (PROPOSED) |
| CERT-07 | UiPath Agentic Automation Builder Professional (UiPath-AABPv1) | UiPath | DEFERRED | PENDING_OFFICIAL_VERIFICATION (EDD: USD 150; FAQ: USD 300 for Professional exams) | EDD V1.0 (Sep 2026); 120 min; MC + drag-and-drop/sequencing; test centre or online proctored | MQC profile: 6+ months building automations on UiPath | 0/52 active ads name it literally; UiPath named as tool in 5 A records (all Dutch-language); certs only in non-NL ads (sample count) | DEC-002 (PROPOSED) |
| CERT-08 | UiPath Automation Developer Professional | UiPath | DEFERRED | USD 300 + tax | EDD V1.1 (Jan 2026), product 2024.10+; 120 min | PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally; UiPath named as tool in 5 A records (all Dutch-language); certs only in non-NL ads (sample count) | DEC-002 (PROPOSED) |
| CERT-09 | UiPath Specialized AI Associate (UiPath-SAIAv1) | UiPath | DROPPED | USD 150 + tax | EDD v1.3 (Jan 2026); 90 min | No prerequisite exam; targets Document Understanding/Communications Mining roles | 0/52 active ads name it literally (sample count) | DEC-002 (PROPOSED) |
| CERT-10 | UiPath Specialized AI Professional | UiPath | DROPPED | USD 300 + tax (FAQ general Professional rule; credential page not extracted) | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally (sample count) | DEC-002 (PROPOSED) |
| CERT-11 | UiPath Automation Business Analyst Associate | UiPath | DEFERRED | USD 150 + tax (FAQ general Associate rule; EDD not fetched) | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally (sample count) | DEC-002 (PROPOSED) |

<!-- page -->
# 3 · Curriculum & Certification Plan — rota de credenciais (2/3)

| CERT | Credencial | Emissor | Papel | Preço original | Formato | Pré-requisitos | Menções no mercado | Decisão |
|---|---|---|---|---|---|---|---|---|
| CERT-12 | PRINCE2 Project Management Foundation (Version 7) | PeopleCert | DEFERRED | USD 701 (voucher + eBook); USD 1,029; USD 1,338 (VAT incl., US location) | 60 questions, multiple choice, 60 min, closed book; results in 2 business days | None; accredited training not required | 0/52 active ads name it literally (sample count) | DEC-004 (PROPOSED) |
| CERT-13 | PRINCE2 Project Management Practitioner (Version 7) | PeopleCert | DEFERRED | USD 778 (exam + LRK); USD 1,235; USD 1,544 (incl. free re-take + mock) | 56 questions/sub-questions (70 marks), objective testing, 150 min, open book | One of: PRINCE2 Foundation v7, PRINCE2 6th/5th ed., PMP, CAPM, PPQ, PMQ, IPMA A–D, CSPM-2/3, others PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally (sample count) | DEC-004 (PROPOSED) |
| CERT-14 | PRINCE2 Agile Practitioner (Version 2) | PeopleCert | DROPPED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally (sample count) | DEC-004 (PROPOSED) |
| CERT-15 | AIGP: Artificial Intelligence Governance Professional (BoK v2.1) | IAPP | MAIN | USD 799 non-member / USD 649 member | Multiple choice; 4 domains (BoK v2.1 eff. 2026-02-02); 15-min optional break at halfway, first half not revisitable; Pearson VUE or OnVUE; take within 1 year of purchase | None; training optional | 2/52 active ads name it literally (JOB-T-013, JOB-T-017) (sample count) | DEC-001 (PROPOSED) |
| CERT-16 | PECB ISO/IEC 42001 Lead Implementer | PECB | DEFERRED | PENDING_OFFICIAL_VERIFICATION (partner-set; exam and certification included in training fee) | 5-day course, exam on day 5; 6 exam domains (weights not published); online exams may be open book | Exam pass + Code of Ethics; title tiers: Provisional (none), Implementer (2y/1y AI/200h AIMS), Lead Implementer (5y/2y AI/300h AIMS), Senior LI (10y/7y/1,000h) | 1/52 active ads name it literally (JOB-T-017); ISO 42001 named as framework in 4 more (T-013, T-015, T-019, T-022) (sample count) | DEC-005 (PROPOSED) |
| CERT-17 | PECB ISO/IEC 42001 Foundation (Certificate Holder) | PECB | DEFERRED | PENDING_OFFICIAL_VERIFICATION (partner-set) | 2-day course, exam on day 2; scenario-based quizzes | None | 1/52 active ads name it literally (JOB-T-017); ISO 42001 named as framework in 4 more (T-013, T-015, T-019, T-022) (sample count) | DEC-005 (PROPOSED) |
| CERT-18 | Prosci Change Management Certification Program (Prosci Certified Change Practitioner) | Prosci | DEFERRED | USD 4,500 online / USD 4,850 in person | 3–5 days; knowledge checks days 1–2, presentations day 3; applied to own live project; no separate proctored exam | Own live project | 0/52 active ads name it literally; only Prosci-mandatory ad found is UAE (JOB-T-048, out of scope) (sample count) | DEC-006 (PROPOSED) |
| CERT-19 | OMG BPM 2 Fundamental (formerly OCEB 2 Fundamental) | Object Management Group (OMG) | DROPPED | USD 350 + taxes | 90 questions multiple choice; 90 min (120 min outside native-English countries); Pearson VUE test centre or online | None | 0/52 active ads name it literally (sample count) | DEC-007 (PROPOSED) |
| CERT-20 | TOGAF Enterprise Architecture Foundation (OGEA-101) | The Open Group | DEFERRED | PENDING_OFFICIAL_VERIFICATION (3rd-party: USD 405) | 40 questions, 60 min, closed book (search extract) | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-007) (sample count) | DEC-019 (PROPOSED) |
| CERT-21 | PMP (Project Management Professional) | PMI | DEFERRED | PENDING_OFFICIAL_VERIFICATION (3rd-party: ~USD 675 non-member) | PENDING_OFFICIAL_VERIFICATION (3rd-party: new exam Jul 2026, 240 min, 180/185 q) | PENDING_OFFICIAL_VERIFICATION | 0/52 active ads name it literally (sample count) | DEC-004 (PROPOSED) |
| CERT-22 | IPMA certification Level D / C (via IPMA-NL) | IPMA (national Member Association IPMA-NL) | DEFERRED | PENDING_OFFICIAL_VERIFICATION (varies by national body) | Competence-based, ICB4; 4 levels A–D | Level C aimed at 3–5 yrs experience | 0/52 active ads name it literally (sample count) | DEC-004 (PROPOSED) |

<!-- page -->
# 3 · Curriculum & Certification Plan — rota de credenciais (3/3)

| CERT | Credencial | Emissor | Papel | Preço original | Formato | Pré-requisitos | Menções no mercado | Decisão |
|---|---|---|---|---|---|---|---|---|
| CERT-23 | DAMA CDMP Practitioner / DCAM (either) | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-017) (sample count) | DEC-008 (PROPOSED) |
| CERT-24 | CIPP/E (and generic CIPP) | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 2/52 active ads name it literally (JOB-T-014, JOB-T-018) (sample count) | DEC-008 (PROPOSED) |
| CERT-25 | CIPM | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-014) (sample count) | DEC-008 (PROPOSED) |
| CERT-26 | CIPT | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-014) (sample count) | DEC-008 (PROPOSED) |
| CERT-27 | ISO 27701 Lead Implementer | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-014) (sample count) | DEC-008 (PROPOSED) |
| CERT-28 | RE / CISA / CISM (audit) | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-018) (sample count) | DEC-008 (PROPOSED) |
| CERT-29 | CCLTE CAICO | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-013) (sample count) | DEC-008 (PROPOSED) |
| CERT-30 | Microsoft PL-100 / PL-200 / PL-400 (as named in ad) | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-A-005) (sample count) | DEC-008 (PROPOSED) |
| CERT-31 | SAFe / Cloud (Azure/AWS/GCP) / FinOps / TBM (bonus list) | PENDING_OFFICIAL_VERIFICATION (named in job ad only) | DEFERRED | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | PENDING_OFFICIAL_VERIFICATION | 1/52 active ads name it literally (JOB-T-007) (sample count) | DEC-008 (PROPOSED) |

<!-- page -->
# 3 · Curriculum & Certification Plan — CERT-15 · IAPP AIGP (MAIN)

**Papel:** MAIN · **Emissor:** IAPP · **Preço:** USD 799 non-member / USD 649 member · **Decisão:** DEC-001 (PROPOSED) · **Pendências oficiais:** total question count; duration; retake fee; CPE hours per term

**Data de prova:** 2027-01-29 (PROPOSED; not booked). Nenhuma reserva nem pagamento foi feito; G4 e G5 seguem `BLOCKED`.

## Cursos (`data/COURSE_CATALOG.csv`)

| CRS | Título | Provedor | Custo | Horas oficiais | Horas planejadas | Nota |
|---|---|---|---|---|---|---|
| CRS-001 | AIGP self-study: BoK v2.1 + Candidate Handbook + free AIGP study guide (main official course) | IAPP | 0 (free; study guide via request form) | PENDING_OFFICIAL_VERIFICATION | 72 (ESTIMATE) | Official training (USD 1,195) not selected: optional, no market evidence it is needed. |
| CRS-002 | AIGP practice exam (digital) — complementary | IAPP | USD 60 | N/A | 6 (ESTIMATE) | Justified: legitimate question bank for G3 MOCKS; does not replace official cut score 300/500. |

## Módulos do syllabus (`data/SYLLABUS_MODULES.csv`) — total planejado 72 h (ESTIMATE)

| MOD | Domínio | Peso | Horas planejadas | Lab / entregável | Critério de prontidão |
|---|---|---|---|---|---|
| MOD-001 | AIGP I. Foundations of AI governance | 16–20 questions (BoK v2.1) | 14 (ESTIMATE) | Responsible-AI principles mapped to the 6 EXECUTAR agents (one-page, English) | Domain diagnostic ≥85% in 2 independent timed mocks (internal target, not official cut score); P0 gaps closed |
| MOD-002 | AIGP II. Laws, standards and frameworks (EU AI Act, NIST AI RMF, ISO 22989/42001) | 19–23 questions (BoK v2.1) | 22 (ESTIMATE) | EU AI Act applicability assessment for the 6 agents (assessed, not presumed) + ISO 42001 control-mapping skeleton | Domain diagnostic ≥85% in 2 independent timed mocks (internal target, not official cut score); P0 gaps closed |
| MOD-003 | AIGP III. Governing AI development | 21–25 questions (BoK v2.1) | 18 (ESTIMATE) | AI risk & impact assessment + incident/issue/risk log for apps/workflow | Domain diagnostic ≥85% in 2 independent timed mocks (internal target, not official cut score); P0 gaps closed |
| MOD-004 | AIGP IV. Governing AI deployment and use | 21–25 questions (BoK v2.1) | 18 (ESTIMATE) | Deployment-control note: human gates G01/G04/G06, API token requirement, monitoring; fix fallback credentials first (GAP-003) | Domain diagnostic ≥85% in 2 independent timed mocks (internal target, not official cut score); P0 gaps closed |

## Gates G0–G5 (`data/EXAM_GATES.csv`)

| GATE | Gate | Critério | Status atual | Evidência | Data-alvo |
|---|---|---|---|---|---|
| GATE-001 | G0 OFFICIAL | Exam active, issuer link, price, language, eligibility and validity verified on official source | BLOCKED | Pending: total question count; duration; retake fee; CPE hours per term (source SRC-137) | — |
| GATE-002 | G1 KNOWLEDGE | 100% of mandatory blueprint domains covered in diagnostic; P0 gaps treated | OPEN | No diagnostic yet; lifecycle NOT_STARTED. First diagnostic PROPOSED in week 19–25/10/2026 | — |
| GATE-003 | G2 PRACTICE | Reproducible, tested, documented lab/deliverable where credential assesses applied competence | OPEN | Partial base: EVD-D-001 human gates, EVD-W-003 agent registry (L1–L2); governance kit GAP-004 not started | — |
| GATE-004 | G3 MOCKS | Two independent timed mocks with legitimate question bank, ≥85% each (internal target), error review by domain | OPEN | Official practice exam USD 60 (CRS-002) not purchased; official cut is 300/500 | — |
| GATE-005 | G4 ECONOMIC | Budget approved, retake cost known, exam best value vs other actions | BLOCKED | Budget NOT_VERIFIED; BUDGET rows NOT_APPROVED; retake fee PENDING | — |
| GATE-006 | G5 AUTHORIZATION | User explicitly authorises booking/payment; otherwise max state READY_TO_BOOK | BLOCKED | No authorisation; no exam booked; target date PROPOSED | 2027-01-29 (PROPOSED; not booked) |

## Orçamento (`data/BUDGET.csv`)

| BUD | Item | Valor | Moeda | Base de preço | Papel | Aprovação | Classe | Notas |
|---|---|---|---|---|---|---|---|---|
| BUD-001 | AIGP exam (non-member) | 799 | USD | Official store price | MAIN | NOT_APPROVED | FACT | Membership status NOT_VERIFIED; member price USD 649 |
| BUD-002 | AIGP exam (member price, alternative) | 649 | USD | Official store price | MAIN | NOT_APPROVED | FACT | Only with IAPP membership (BUD-005) |
| BUD-003 | AIGP practice exam (digital) | 60 | USD | Official store price | MAIN | NOT_APPROVED | FACT | For G3 MOCKS (CRS-002) |
| BUD-004 | AIGP official online training (not recommended) | 1195 | USD | Official store price | MAIN | NOT_APPROVED | FACT | Optional; not in lean route |
| BUD-005 | IAPP professional membership (annual) | 295 | USD | Official store price | MAIN | NOT_APPROVED | FACT | Optional; covers CMF |
| BUD-006 | AIGP Certification Maintenance Fee at recertification (non-member) | 250 | USD | Official store page | MAIN | NOT_APPROVED | FACT | Future cost |
| BUD-007 | AIGP retake fee | PENDING_OFFICIAL_VERIFICATION | USD | PENDING_OFFICIAL_VERIFICATION | MAIN | NOT_APPROVED | NOT_VERIFIED | 3rd-party cites USD 475/625 (Apr 2024) — not used |
| BUD-023 | TOTAL lean route first attempts (AIGP non-member + AAA + PSPO I) | 1149 | USD | Sum of BUD-001 + BUD-008 + BUD-010 | MAIN+OPTIONAL | NOT_APPROVED | INFERENCE | Computed; excludes Dutch course (PENDING) and retakes |
| BUD-024 | REFERENCE draft core route (PSPO I + AAA + PRINCE2 F+P + AIGP non-member) — not proposed | 2628 | USD | Sum of official prices | REFERENCE | NOT_APPROVED | INFERENCE | Excludes PECB and Prosci |

Viabilidade (DEC-023, PROPOSED): estudo de 90 h ≥ 72 h de curso planejado e 60 h de exam prep ≥ 18 h antes de 2027-01-29. O simulado oficial (CRS-002, USD 60) não substitui o corte oficial de 300/500; a meta interna de ≥85% em dois simulados é KPI-004.

<!-- page -->
# 3 · Curriculum & Certification Plan — CERT-05 · UiPath Agentic Automation Associate (OPTIONAL)

**Papel:** OPTIONAL · **Emissor:** UiPath · **Preço:** USD 150 + tax · **Decisão:** DEC-002 (PROPOSED) · **Pendências oficiais:** question count (3rd-party claims 60)

**Data de prova:** 2026-12-18 (PROPOSED; not booked). Nenhuma reserva nem pagamento foi feito; G4 e G5 seguem `BLOCKED`.

## Cursos (`data/COURSE_CATALOG.csv`)

| CRS | Título | Provedor | Custo | Horas oficiais | Horas planejadas | Nota |
|---|---|---|---|---|---|---|
| CRS-003 | UiPath Academy 'Agentic Automation Training' learning plan + free practice test (main official course) | UiPath Academy | 0 | PENDING_OFFICIAL_VERIFICATION | 20 (ESTIMATE) | Hour estimates shown inside Academy, not extracted. |
| CRS-004 | UiPath Academy 'Introduction to Agentic Automation' — complementary | UiPath Academy | 0 | PENDING_OFFICIAL_VERIFICATION | 4 (ESTIMATE) | Justified: officially recommended together with the AAA learning plan. |

## Módulos do syllabus (`data/SYLLABUS_MODULES.csv`) — total planejado 24 h (ESTIMATE)

| MOD | Domínio | Peso | Horas planejadas | Lab / entregável | Critério de prontidão |
|---|---|---|---|---|---|
| MOD-005 | AAA: Agentic AI concepts | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 2 (ESTIMATE) | Glossary mapped to apps/workflow | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-006 | AAA: Agentic discovery | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 2 (ESTIMATE) | Discovery canvas for one EXECUTAR process | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-007 | AAA: Agent blueprint design | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 3 (ESTIMATE) | Blueprint of one subagent (inputs, tools, escalation) | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-008 | AAA: Context Grounding | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 2 (ESTIMATE) | Note on grounding sources used by agents | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-009 | AAA: Escalations | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 2 (ESTIMATE) | Escalation matrix from gates G01/G04/G06 | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-010 | AAA: Agentic evaluations | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 3 (ESTIMATE) | Re-run plugin eval with logged results (GAP-011) | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-011 | AAA: Prompt engineering | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 2 (ESTIMATE) | Prompt patterns from agent definitions | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-012 | AAA: Platform components and integrations | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 3 (ESTIMATE) | Map UiPath components vs Workers/MCP stack | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-013 | AAA: Maestro orchestration | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 3 (ESTIMATE) | Compare Maestro with 8-phase workflow | Free official practice test ≥85% twice (internal target; official pass 70%) |
| MOD-014 | AAA: Autopilot for everyone | PENDING_OFFICIAL_VERIFICATION (weights not published in EDD extract) | 2 (ESTIMATE) | Hands-on in free Academy lab | Free official practice test ≥85% twice (internal target; official pass 70%) |

## Gates G0–G5 (`data/EXAM_GATES.csv`)

| GATE | Gate | Critério | Status atual | Evidência | Data-alvo |
|---|---|---|---|---|---|
| GATE-007 | G0 OFFICIAL | Exam active, issuer link, price, language, eligibility and validity verified on official source | BLOCKED | Pending: question count (3rd-party claims 60) (source SRC-118) | — |
| GATE-008 | G1 KNOWLEDGE | 100% of mandatory blueprint domains covered in diagnostic; P0 gaps treated | OPEN | No diagnostic yet; lifecycle NOT_STARTED. First diagnostic PROPOSED in week 19–25/10/2026 | — |
| GATE-009 | G2 PRACTICE | Reproducible, tested, documented lab/deliverable where credential assesses applied competence | OPEN | Partial base: EVD-D-001 (L3), EVD-D-005, EVD-D-007 (eval self-reported) | — |
| GATE-010 | G3 MOCKS | Two independent timed mocks with legitimate question bank, ≥85% each (internal target), error review by domain | OPEN | Free official practice test available; not taken | — |
| GATE-011 | G4 ECONOMIC | Budget approved, retake cost known, exam best value vs other actions | BLOCKED | Budget NOT_VERIFIED; BUDGET rows NOT_APPROVED | — |
| GATE-012 | G5 AUTHORIZATION | User explicitly authorises booking/payment; otherwise max state READY_TO_BOOK | BLOCKED | No authorisation; no exam booked; target date PROPOSED | 2026-12-18 (PROPOSED; not booked) |

## Orçamento (`data/BUDGET.csv`)

| BUD | Item | Valor | Moeda | Base de preço | Papel | Aprovação | Classe | Notas |
|---|---|---|---|---|---|---|---|---|
| BUD-008 | UiPath Agentic Automation Associate exam | 150 | USD | Official EDD/FAQ (+ tax) | OPTIONAL | NOT_APPROVED | FACT | — |
| BUD-009 | UiPath retake (full fee per attempt, contingency) | 150 | USD | Official FAQ/policies | OPTIONAL | NOT_APPROVED | FACT | — |
| BUD-023 | TOTAL lean route first attempts (AIGP non-member + AAA + PSPO I) | 1149 | USD | Sum of BUD-001 + BUD-008 + BUD-010 | MAIN+OPTIONAL | NOT_APPROVED | INFERENCE | Computed; excludes Dutch course (PENDING) and retakes |
| BUD-024 | REFERENCE draft core route (PSPO I + AAA + PRINCE2 F+P + AIGP non-member) — not proposed | 2628 | USD | Sum of official prices | REFERENCE | NOT_APPROVED | INFERENCE | Excludes PECB and Prosci |

Viabilidade (DEC-023, PROPOSED): estudo de 24 h ≥ 24 h de curso planejado e 15 h de exam prep ≥ 6 h antes de 2026-12-18. Compra só depois de G4/G5 (DEC-002); a prova prática gratuita entra como diagnóstico na WK-01 (TASK-0011).

<!-- page -->
# 3 · Curriculum & Certification Plan — CERT-01 · Scrum.org PSPO I (OPTIONAL)

**Papel:** OPTIONAL · **Emissor:** Scrum.org · **Preço:** USD 200 per attempt · **Decisão:** DEC-003 (PROPOSED) · **Pendências oficiais:** all fields (scrum.org HTTP 403; search extract only); question types; proctoring; language; validity; Product Owner Open URL

**Data de prova:** 2027-03-12 (PROPOSED; not booked). Nenhuma reserva nem pagamento foi feito; G4 e G5 seguem `BLOCKED`.

## Cursos (`data/COURSE_CATALOG.csv`)

| CRS | Título | Provedor | Custo | Horas oficiais | Horas planejadas | Nota |
|---|---|---|---|---|---|---|
| CRS-005 | Scrum Guide + Product Owner Open + 'How to Pass PSPO I' (self-study, main official) | Scrum.org | 0 | PENDING_OFFICIAL_VERIFICATION | 16 (ESTIMATE) | Product Owner Open URL and Scrum Guide current edition PENDING. |

## Módulos do syllabus (`data/SYLLABUS_MODULES.csv`) — total planejado 16 h (ESTIMATE)

| MOD | Domínio | Peso | Horas planejadas | Lab / entregável | Critério de prontidão |
|---|---|---|---|---|---|
| MOD-015 | PSPO I focus areas — PENDING_OFFICIAL_VERIFICATION (scrum.org HTTP 403) | PENDING_OFFICIAL_VERIFICATION | 16 (ESTIMATE) | Backlog + product goal for Scroll Task prototype (EVD-D-013) | Product Owner Open ≥85% twice (internal target; official pass 85%) |

## Gates G0–G5 (`data/EXAM_GATES.csv`)

| GATE | Gate | Critério | Status atual | Evidência | Data-alvo |
|---|---|---|---|---|---|
| GATE-013 | G0 OFFICIAL | Exam active, issuer link, price, language, eligibility and validity verified on official source | BLOCKED | Pending: all fields (scrum.org HTTP 403; search extract only); question types; proctoring; language; validity; Product Owner Open URL (source SRC-103) | — |
| GATE-014 | G1 KNOWLEDGE | 100% of mandatory blueprint domains covered in diagnostic; P0 gaps treated | OPEN | No diagnostic yet; blueprint PENDING (scrum.org 403) | — |
| GATE-015 | G2 PRACTICE | Reproducible, tested, documented lab/deliverable where credential assesses applied competence | OPEN | Partial base: EVD-D-013 PRD→prototype (L2) | — |
| GATE-016 | G3 MOCKS | Two independent timed mocks with legitimate question bank, ≥85% each (internal target), error review by domain | OPEN | Product Owner Open free; URL PENDING | — |
| GATE-017 | G4 ECONOMIC | Budget approved, retake cost known, exam best value vs other actions | BLOCKED | Budget NOT_VERIFIED; BUDGET rows NOT_APPROVED; retake fee PENDING | — |
| GATE-018 | G5 AUTHORIZATION | User explicitly authorises booking/payment; otherwise max state READY_TO_BOOK | BLOCKED | No authorisation; no exam booked; target date PROPOSED | 2027-03-12 (PROPOSED; not booked) |

## Orçamento (`data/BUDGET.csv`)

| BUD | Item | Valor | Moeda | Base de preço | Papel | Aprovação | Classe | Notas |
|---|---|---|---|---|---|---|---|---|
| BUD-010 | Scrum.org PSPO I assessment | 200 | USD | Search extract of official page | OPTIONAL | NOT_APPROVED | FACT | PENDING_OFFICIAL_VERIFICATION (403) |
| BUD-023 | TOTAL lean route first attempts (AIGP non-member + AAA + PSPO I) | 1149 | USD | Sum of BUD-001 + BUD-008 + BUD-010 | MAIN+OPTIONAL | NOT_APPROVED | INFERENCE | Computed; excludes Dutch course (PENDING) and retakes |
| BUD-024 | REFERENCE draft core route (PSPO I + AAA + PRINCE2 F+P + AIGP non-member) — not proposed | 2628 | USD | Sum of official prices | REFERENCE | NOT_APPROVED | INFERENCE | Excludes PECB and Prosci |

Viabilidade (DEC-023, PROPOSED): estudo de 24 h ≥ 16 h de curso planejado e 10 h de exam prep ≥ 6 h antes de 2027-03-12. Todo o Scrum.org está `PENDING_OFFICIAL_VERIFICATION` (HTTP 403; somente extrato de busca). GAP-018 cita "BUD-009" como linha de custo do PSPO I, mas a linha correspondente em `data/BUDGET.csv` é BUD-010 (BUD-009 é o retake UiPath); a divergência fica registrada aqui, sem alterar o CSV.

<!-- page -->
# 3 · Curriculum & Certification Plan — sobreposições e orçamento total

## Análise de sobreposição (SRC-003 §3; INFERENCE a partir dos syllabi — nenhum emissor publica cross-mapping oficial)

| Par | Sobreposição | Consequência no plano |
|---|---|---|
| AIGP (CERT-15) × ISO 42001 (CERT-16/17) | Alta: o domínio II do BoK v2.1 cobre NIST AI RMF e normas ISO de IA (22989, 42001); risco de IA reaparece nos domínios I–IV | PECB DEFERRED (DEC-005); 42001 coberta via MOD-002 + mapeamento de controles no portfólio (GAP-004) |
| PSPO (CERT-01/03) × PRINCE2 (CERT-12/13) | Cobrem papéis, valor e entrega por paradigmas opostos; PRINCE2 Agile seria redundante com os dois | PRINCE2 DEFERRED; PRINCE2 Agile DROPPED (DEC-004) |
| Prosci (CERT-18) × PRINCE2 v7 | Parcial: a v7 incluiu o "human element" | Prosci DEFERRED; ADKAR aplicado num plano de mudança (GAP-008; DEC-006) |
| UiPath AAA (CERT-05) × AIGP | Mínima, via AI Trust Layer e evals; complementares | Ambas mantidas (OPTIONAL + MAIN) |
| PMP (CERT-21) / IPMA (CERT-22) × PRINCE2 | Alternativas, não complementos: escolhe-se uma | Todas DEFERRED (DEC-004); PMP com todos os campos `PENDING_OFFICIAL_VERIFICATION` |

## Orçamento consolidado

| BUD | Item | Valor | Moeda | Base | Aprovação | Classe | Notas |
|---|---|---|---|---|---|---|---|
| BUD-023 | TOTAL lean route first attempts (AIGP non-member + AAA + PSPO I) | 1149 | USD | Sum of BUD-001 + BUD-008 + BUD-010 | NOT_APPROVED | INFERENCE | Computed; excludes Dutch course (PENDING) and retakes |
| BUD-024 | REFERENCE draft core route (PSPO I + AAA + PRINCE2 F+P + AIGP non-member) — not proposed | 2628 | USD | Sum of official prices | NOT_APPROVED | INFERENCE | Excludes PECB and Prosci |

A rota enxuta custa **USD 1149** nas primeiras tentativas (BUD-023), contra **USD 2628** da rota "core" do rascunho (BUD-024, referência não proposta). O curso de neerlandês (BUD-011) tem provedor e preço `PENDING_OFFICIAL_VERIFICATION`.

**Declaração:** nenhuma prova está reservada e nada foi pago. Todas as linhas de `data/BUDGET.csv` estão `NOT_APPROVED`; G4 ECONOMIC e G5 AUTHORIZATION estão `BLOCKED` para CERT-15, CERT-05 e CERT-01, e o estado máximo sem ordem explícita do usuário é READY_TO_BOOK (KPI-007; KPI-018).

<!-- page -->
# 4 · Weekly Master Schedule

Capacidade de **40 h por semana cheia** (KPI-001). Alocação por fase conforme DEC-020 (PROPOSED): P1 16/8/10/4/0 + BUFFER 2; P2 14/6/8/4/6 + BUFFER 2; P3 10/6/6/4/12 + BUFFER 2; P4 5/2/2/2/14 + RELOCATION_ADMIN 12 + BUFFER 3; P5 mai–ago 12/4/6/4/8 + REL 4 + BUFFER 2; P5 set–out 14/4/6/4/10 + BUFFER 2 (ordem ACTIVE_STUDY/EXAM_PREP/APPLIED_BUILD/PUBLIC_PORTFOLIO/CAREER_SEARCH). Semanas de transição são rateadas por dia útil. O neerlandês fica dentro de ACTIVE_STUDY (DEC-022: P1 4 h, P2 5 h, P3 5 h, P4 3 h, P5 6 h por semana cheia). Feriados (`ASSUMPTION`) movem as 8 h do dia para BUFFER (DEC-021). Linhas mensais a partir de maio/2027 usam dias úteis × 8 (DEC-024, ASSUMPTION).

## Alocação por fase (horas e % do disponível; soma de `data/ROADMAP_WEEKLY.csv`)

| Fase | Períodos | Nº | Disponível (h) | ACTIVE_STUDY | EXAM_PREP | APPLIED_BUILD | PUBLIC_PORTFOLIO | CAREER_SEARCH | BUFFER | RELOCATION_ADMIN |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 diagnóstico | WK-01..WK-04 | 4 | 160 | 64 (40%) | 32 (20%) | 40 (25%) | 16 (10%) | 0 (0%) | 8 (5%) | 0 (0%) |
| P1 diagnóstico/P2 posicionamento | WK-05..WK-05 | 1 | 40 | 15 (38%) | 7 (18%) | 9 (22%) | 4 (10%) | 3 (8%) | 2 (5%) | 0 (0%) |
| P2 posicionamento | WK-06..WK-15 | 10 | 400 | 134 (34%) | 58 (14%) | 76 (19%) | 38 (10%) | 58 (14%) | 36 (9%) | 0 (0%) |
| P3 candidaturas | WK-16..WK-23 | 8 | 320 | 80 (25%) | 48 (15%) | 48 (15%) | 32 (10%) | 96 (30%) | 16 (5%) | 0 (0%) |
| P3 candidaturas/P4 entrevistas+realocação | WK-24..WK-24 | 1 | 40 | 7 (18%) | 4 (10%) | 4 (10%) | 3 (8%) | 13 (32%) | 2 (5%) | 7 (18%) |
| P4 entrevistas+realocação | WK-25..WK-28 | 4 | 160 | 20 (12%) | 8 (5%) | 8 (5%) | 8 (5%) | 56 (35%) | 12 (8%) | 48 (30%) |
| P5 continuidade | MON-2027-05..MON-2027-10 | 6 | 968 | 301 (31%) | 97 (10%) | 141 (15%) | 95 (10%) | 203 (21%) | 65 (7%) | 66 (7%) |
| **Total** | WK-01..MON-2027-10 | 34 | 2088 | 621 (30%) | 254 (12%) | 326 (16%) | 196 (9%) | 429 (21%) | 141 (7%) | 121 (6%) |

Verificação: em todos os 34 períodos a soma das classes é igual a `available_hours`.

<!-- page -->
# 4 · Weekly Master Schedule — ROADMAP_WEEKLY (1/2)

Legenda: AS = ACTIVE_STUDY · EP = EXAM_PREP · AB = APPLIED_BUILD · PP = PUBLIC_PORTFOLIO · CS = CAREER_SEARCH · BF = BUFFER · RA = RELOCATION_ADMIN. Status de todas as linhas: PLANNED.

| Período | Início | Fim | Fase | Disp. | AS | EP | AB | PP | CS | BF | RA | Marcos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WK-01 | 2026-10-19 | 2026-10-25 | P1 diagnóstico | 40 | 16 | 8 | 10 | 4 | 0 | 2 | 0 | 2026-10-19 Program start (40 h/week); 2026-10-20 Avans ad closes — recommendation: do not apply (DEC-013) |
| WK-02 | 2026-10-26 | 2026-11-01 | P1 diagnóstico | 40 | 16 | 8 | 10 | 4 | 0 | 2 | 0 | 2026-10-27 ILT ad closes (NOT_YET_ELIGIBLE) |
| WK-03 | 2026-11-02 | 2026-11-08 | P1 diagnóstico | 40 | 16 | 8 | 10 | 4 | 0 | 2 | 0 | — |
| WK-04 | 2026-11-09 | 2026-11-15 | P1 diagnóstico | 40 | 16 | 8 | 10 | 4 | 0 | 2 | 0 | — |
| WK-05 | 2026-11-16 | 2026-11-22 | P1 diagnóstico/P2 posicionamento | 40 | 15 | 7 | 9 | 4 | 3 | 2 | 0 | 2026-11-18 30-day FIT recalculation mark; 2026-11-19 Employment & Relocation epic start (EPIC-07) |
| WK-06 | 2026-11-23 | 2026-11-29 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | — |
| WK-07 | 2026-11-30 | 2026-12-06 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | 2026-11-30 Alliander ad closes |
| WK-08 | 2026-12-07 | 2026-12-13 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | — |
| WK-09 | 2026-12-14 | 2026-12-20 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | 2026-12-18 UiPath AAA exam PROPOSED (CERT-05; not booked; G4/G5 BLOCKED) + 60-day FIT mark |
| WK-10 | 2026-12-21 | 2026-12-27 | P2 posicionamento | 40 | 11 | 5 | 6 | 3 | 5 | 10 | 0 | — |
| WK-11 | 2026-12-28 | 2027-01-03 | P2 posicionamento | 40 | 11 | 5 | 6 | 3 | 5 | 10 | 0 | 2026-12-31 DICTU ad deadline (TARGET_LATER) |
| WK-12 | 2027-01-04 | 2027-01-10 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | — |
| WK-13 | 2027-01-11 | 2027-01-17 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | 2027-01-17 90-day FIT recalculation mark |
| WK-14 | 2027-01-18 | 2027-01-24 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | — |
| WK-15 | 2027-01-25 | 2027-01-31 | P2 posicionamento | 40 | 14 | 6 | 8 | 4 | 6 | 2 | 0 | 2027-01-29 AIGP exam PROPOSED (CERT-15; not booked; G4/G5 BLOCKED) |
| WK-16 | 2027-02-01 | 2027-02-07 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | 2027-02-01 Formal application window opens |
| WK-17 | 2027-02-08 | 2027-02-14 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | — |

<!-- page -->
# 4 · Weekly Master Schedule — ROADMAP_WEEKLY (2/2)

Legenda: AS = ACTIVE_STUDY · EP = EXAM_PREP · AB = APPLIED_BUILD · PP = PUBLIC_PORTFOLIO · CS = CAREER_SEARCH · BF = BUFFER · RA = RELOCATION_ADMIN. Status de todas as linhas: PLANNED.

| Período | Início | Fim | Fase | Disp. | AS | EP | AB | PP | CS | BF | RA | Marcos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WK-18 | 2027-02-15 | 2027-02-21 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | — |
| WK-19 | 2027-02-22 | 2027-02-28 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | — |
| WK-20 | 2027-03-01 | 2027-03-07 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | — |
| WK-21 | 2027-03-08 | 2027-03-14 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | 2027-03-12 PSPO I assessment PROPOSED (CERT-01; not booked; G4/G5 BLOCKED) |
| WK-22 | 2027-03-15 | 2027-03-21 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | — |
| WK-23 | 2027-03-22 | 2027-03-28 | P3 candidaturas | 40 | 10 | 6 | 6 | 4 | 12 | 2 | 0 | — |
| WK-24 | 2027-03-29 | 2027-04-04 | P3 candidaturas/P4 entrevistas+realocação | 40 | 7 | 4 | 4 | 3 | 13 | 2 | 7 | 2027-03-30 Formal application window closes |
| WK-25 | 2027-04-05 | 2027-04-11 | P4 entrevistas+realocação | 40 | 5 | 2 | 2 | 2 | 14 | 3 | 12 | — |
| WK-26 | 2027-04-12 | 2027-04-18 | P4 entrevistas+realocação | 40 | 5 | 2 | 2 | 2 | 14 | 3 | 12 | — |
| WK-27 | 2027-04-19 | 2027-04-25 | P4 entrevistas+realocação | 40 | 5 | 2 | 2 | 2 | 14 | 3 | 12 | — |
| WK-28 | 2027-04-26 | 2027-05-02 | P4 entrevistas+realocação | 40 | 5 | 2 | 2 | 2 | 14 | 3 | 12 | 2027-04-30 Travel target date (Europe/Amsterdam) |
| MON-2027-05 | 2027-05-03 | 2027-05-31 | P5 continuidade | 168 | 46 | 15 | 23 | 15 | 30 | 24 | 15 | — |
| MON-2027-06 | 2027-06-01 | 2027-06-30 | P5 continuidade | 176 | 53 | 18 | 26 | 18 | 35 | 9 | 17 | — |
| MON-2027-07 | 2027-07-01 | 2027-07-31 | P5 continuidade | 176 | 53 | 18 | 26 | 18 | 35 | 9 | 17 | — |
| MON-2027-08 | 2027-08-01 | 2027-08-31 | P5 continuidade | 176 | 53 | 18 | 26 | 18 | 35 | 9 | 17 | ~2027-08-30 Latest date for Dutch basic health insurance (4 months after arrival; REL-012) |
| MON-2027-09 | 2027-09-01 | 2027-09-30 | P5 continuidade | 176 | 62 | 18 | 26 | 17 | 44 | 9 | 0 | — |
| MON-2027-10 | 2027-10-01 | 2027-10-18 | P5 continuidade | 96 | 34 | 10 | 14 | 9 | 24 | 5 | 0 | 2027-10-18 End of 12-month program horizon |

<!-- page -->
# 4 · Weekly Master Schedule — foco WK-01..WK-12 (1/2)

Foco, metas de certificação e tarefas com `week_id` exato em `data/EPICS_ISSUES_TASKS.csv` (tarefas de janelas multi-semana, como `WK-01..WK-12`, ficam na tabela de origem). Coluna "Autorização" = tarefas com `external_action_requires_authorization = Y`.

| Semana | Datas | Foco | Metas de certificação | TASKs | Autorização |
|---|---|---|---|---|---|
| WK-01 | 2026-10-19 → 2026-10-25 | Baseline intake; security recommendation + secret scan; AIGP diagnostic; Dutch placement; governance kit v0; UiPath AAA free practice test; re-verify drafts; pipeline set-up; EN one-pager \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-15 G1 diagnostic (GATE-002); CERT-05 practice test (GATE-010); G0 checks (GATE-001;GATE-007;GATE-013) | TASK-0001; TASK-0004; TASK-0012; TASK-0006; TASK-0007; TASK-0009; TASK-0008; TASK-0010; TASK-0011; TASK-0005; TASK-0003; TASK-0002; TASK-0013 | TASK-0004 |
| WK-02 | 2026-10-26 → 2026-11-01 | Re-optimise allocation after baseline; AIGP domain I; G0 verification; governance kit v0 finish; experience map \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-15 G0 pending fields (GATE-001); CERT-05 learning | TASK-0022; TASK-0023; TASK-0025; TASK-0014; TASK-0015; TASK-0017; TASK-0016; TASK-0027; TASK-0018; TASK-0019; TASK-0020; TASK-0021; TASK-0024; TASK-0026; TASK-0028 | TASK-0022 |
| WK-03 | 2026-11-02 → 2026-11-08 | AIGP domain II (EU AI Act + Omnibus, ISO 42001); risk & impact template; eval re-run; CV ATS base \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-15 domain II; CERT-05 learning | TASK-0036; TASK-0029; TASK-0031; TASK-0030; TASK-0032; TASK-0034; TASK-0033; TASK-0035; TASK-0037; TASK-0038; TASK-0039 | TASK-0036 |
| WK-04 | 2026-11-09 → 2026-11-15 | AIGP domain III; ISO 42001 control mapping; PII policy; live demo (with authorisation); LinkedIn + README drafts \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-15 domain III mock; CERT-05 learning | TASK-0040; TASK-0042; TASK-0041; TASK-0043; TASK-0044; TASK-0045; TASK-0046; TASK-0047; TASK-0048; TASK-0050; TASK-0049; TASK-0051 | TASK-0048 |
| WK-05 | 2026-11-16 → 2026-11-22 | AIGP domain IV; 30-day FIT recalculation; networking target map v0; CV variants; OUT-001 draft \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-15 domain IV; CERT-05 learning | TASK-0052; TASK-0054; TASK-0053; TASK-0055; TASK-0056; TASK-0057; TASK-0059; TASK-0060; TASK-0058; TASK-0061; TASK-0062; TASK-0064; TASK-0063; TASK-0065 | — |
| WK-06 | 2026-11-23 → 2026-11-29 | AIGP weak domains; UiPath timed mock #1; ADKAR change plan; business case; pipeline refresh \| Dutch ≈5 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-05 G3 mock #1 (GATE-010) | TASK-0066; TASK-0068; TASK-0067; TASK-0070; TASK-0069; TASK-0071; TASK-0072; TASK-0073; TASK-0074; TASK-0076; TASK-0075; TASK-0077 | — |

<!-- page -->
# 4 · Weekly Master Schedule — foco WK-01..WK-12 (2/2)

Foco, metas de certificação e tarefas com `week_id` exato em `data/EPICS_ISSUES_TASKS.csv` (tarefas de janelas multi-semana, como `WK-01..WK-12`, ficam na tabela de origem). Coluna "Autorização" = tarefas com `external_action_requires_authorization = Y`.

| Semana | Datas | Foco | Metas de certificação | TASKs | Autorização |
|---|---|---|---|---|---|
| WK-07 | 2026-11-30 → 2026-12-06 | UiPath timed mock #2 + READY_TO_BOOK dossier; change plan + business case finish; recruiter shortlist; freelance feasibility \| Dutch ≈5 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-05 G3 mock #2 (GATE-010); G4 dossier (GATE-011) | TASK-0078; TASK-0079; TASK-0081; TASK-0080; TASK-0084; TASK-0082; TASK-0083; TASK-0085; TASK-0086; TASK-0087; TASK-0088; TASK-0089; TASK-0090; TASK-0091; TASK-0092 | — |
| WK-08 | 2026-12-07 → 2026-12-13 | UiPath error review; AIGP mock; Copilot Studio/Power Automate lab set-up; incident/risk log \| Dutch ≈5 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-05 error review; CERT-15 mock | TASK-0093; TASK-0095; TASK-0094; TASK-0097; TASK-0096; TASK-0099; TASK-0098; TASK-0101; TASK-0100; TASK-0102; TASK-0103; TASK-0104 | — |
| WK-09 | 2026-12-14 → 2026-12-20 | UiPath AAA exam window (only if G0–G5 passed); 60-day FIT recalculation; Copilot lab; case page \| Dutch ≈5 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-05 exam 2026-12-18 PROPOSED (GATE-012 BLOCKED until authorisation) | TASK-0105; TASK-0107; TASK-0106; TASK-0110; TASK-0108; TASK-0109; TASK-0112; TASK-0111; TASK-0113; TASK-0114; TASK-0117; TASK-0116; TASK-0115; TASK-0118 | TASK-0109 |
| WK-10 | 2026-12-21 → 2026-12-27 | Holiday week (25 Dec → BUFFER); AIGP timed practice; L4 pilot design; DICTU decision; application templates \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency \| holiday hours moved to BUFFER: 2026-12-25 Christmas Day (ASSUMPTION; candidate location NOT_VERIFIED) | CERT-15 timed practice | TASK-0119; TASK-0120; TASK-0121; TASK-0122; TASK-0123; TASK-0124; TASK-0125; TASK-0126 | — |
| WK-11 | 2026-12-28 → 2027-01-03 | Holiday week (1 Jan → BUFFER); AIGP practice exam #1 (purchase needs authorisation); 2027 event calendars \| Dutch ≈4 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency \| holiday hours moved to BUFFER: 2027-01-01 New Year's Day (ASSUMPTION; candidate location NOT_VERIFIED) | CERT-15 G3 mock #1 (GATE-004) | TASK-0127; TASK-0128; TASK-0129; TASK-0130; TASK-0131; TASK-0132; TASK-0134; TASK-0133; TASK-0135; TASK-0136; TASK-0137 | TASK-0129; TASK-0132 |
| WK-12 | 2027-01-04 → 2027-01-10 | AIGP mock #2; Copilot lab finish; L4 pilot week 1 (authorised); Feb shortlist; pre-move start-date policy \| Dutch ≈5 h inside ACTIVE_STUDY \| BUFFER = 1 h weekly review + contingency | CERT-15 G3 mock #2 (GATE-004); CERT-01 reading | TASK-0138; TASK-0139; TASK-0141; TASK-0142; TASK-0143; TASK-0144; TASK-0145; TASK-0146; TASK-0149; TASK-0147; TASK-0148; TASK-0150; TASK-0140 | TASK-0144 |

<!-- page -->
# 4 · Weekly Master Schedule — estrutura e método de revisão

## Estrutura de trabalho (`data/EPICS_ISSUES_TASKS.csv`)
289 itens: 1 PROGRAM, 8 AREA, 10 EPIC, 114 ISSUE, 150 TASK, 6 SUBTASK.

| EPIC | Título | Horas estimadas | Início | Fim |
|---|---|---|---|---|
| EPIC-00 | Diagnose baseline and govern evidence (EPIC 00) | 17 | 2026-10-19 | 2027-10-18 |
| EPIC-01 | Run headhunter wide search of NL opportunities (EPIC 01) | 4 | 2026-10-19 | 2027-10-18 |
| EPIC-02 | Study competence-oriented courses (EPIC 02) | 621 | 2026-10-19 | 2027-10-18 |
| EPIC-03 | Schedule weekly capacity and granular plan (EPIC 03) | 1 | 2026-10-19 | 2027-10-18 |
| EPIC-04 | Pass certification gates with mocks (EPIC 04) | 252 | 2026-10-19 | 2027-10-18 |
| EPIC-05 | Build portfolio/showroom and audit risks (EPIC 05) | 312 | 2026-10-19 | 2027-10-18 |
| EPIC-06 | Build professional brand and communication (EPIC 06) | 190.5 | 2026-10-19 | 2027-10-18 |
| EPIC-07 | Secure employment and relocate (EPIC 07) | 544.5 | 2026-11-19 | 2027-10-18 |
| EPIC-08 | Maintain dynamic fit matrix (EPIC 08) | 6 | 2026-10-19 | 2027-10-18 |
| EPIC-09 | Review executive results and optimise return (EPIC 09) | 51 | 2026-10-19 | 2027-10-18 |

Cada TASK tem critério SMART (`smart_criterion`), entregável, gate e lacunas vinculadas; o responsável é o papel "candidato como program owner", e o owner de dados é `MA.PRG`.

## Método de revisão (planejado vs. real)
- **Semanal** (TASK-0013, 1 h dentro do BUFFER, até domingo): horas planejadas vs. executadas por classe (KPI-001/KPI-002, meta ±10%% PROPOSED), velocity = horas concluídas / planejadas (KPI-003, meta ≥0,8), prontidão por credencial (KPI-004..KPI-006), novas vagas, bloqueios (KPI-013) e consumo de BUFFER (KPI-022). Desvios são replanejados, não escondidos.
- **Gatilhos de replanejamento:** horas reais >40 ou velocity <0,8 duas semanas seguidas (RISK-008); duas revisões perdidas ou >45 h (RISK-014); mais de 3 issues por classe abertas na semana (RISK-010).
- **Quinzenal/mensal:** gates por credencial (KPI-007), evidências adicionadas (KPI-008), riscos abertos (KPI-014), recálculo de FIT nas marcas 2026-11-18, 2026-12-18 e 2027-01-17 (KPI-010) e revisão CONTINUE/DEFER/DROP a partir de MON-2027-05.

<!-- page -->
# 5 · Evidence Gap Report

## Auditoria de repositórios (`data/REPOSITORY_AUDIT.csv`)
Apenas clones locais de REPO-001 e REPO-002 foram auditados (somente leitura, testes executados localmente em 2026-10-17). Os demais estão `NOT_VERIFIED` ou `GAP`.

| REPO | Nome | HEAD SHA | Commits | Período | Contribuidores | Testes | Deploy | Classe |
|---|---|---|---|---|---|---|---|---|
| REPO-001 | programaex/design | 6f6b66f1ca281c34ff2b3df91a7ffedcfa38ebe4 | 18 | 2026-10-15 → 2026-10-16 | 2 (14 commits agent 'Claude'; 4 merges owner) | apps/workflow 64/64 (vitest); apps/site 15/15 (vitest) + 17/17 (node:test) — local run 2026-10-17 | Worker 'design' live (302 → /login; URL REDACTED pending decision); workflows-starter-template URL 404 (no live demo); hub-executar react-router app behind Cloudflare Access (code not in repo) | FACT |
| REPO-002 | programaex/workbook | cffe5907c6511b2830010c7c9520ad32c6c5608d | 8 | 2026-10-17 → 2026-10-17 | 2 (6 agent 'Claude'; 2 owner) | No test suite; python3 -I workbook.py check → 'check ok' (local, read-only) | N/A | FACT |
| REPO-003 | EXECUTAR SaaS / app mobile / miniapps PWA | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED |
| REPO-004 | Clean Sea solution | GAP | GAP | GAP | GAP | GAP | GAP | NOT_VERIFIED |
| REPO-005 | Risco Cognitivo blog (apps/blog) | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | Blog URL behind Cloudflare Access (NOT_VERIFIED) | NOT_VERIFIED |
| REPO-006 | Frankswaching editorial line | GAP | GAP | GAP | GAP | GAP | GAP | NOT_VERIFIED |

Autoria: 14 dos 18 commits de REPO-001 e 6 dos 8 de REPO-002 são do agente; há conteúdo anterior ao primeiro commit (importação em bloco). Narrativa obrigatória: o candidato desenha, especifica, governa e revisa; o agente implementa (DEC-018; RISK-011). O `main` remoto do design (`fc45fce`) e outras branches não foram auditados.

<!-- page -->
# 5 · Evidence Gap Report — PORTFOLIO_EVIDENCE (1/2)

Maturidade L0–L4 conforme `data/PORTFOLIO_EVIDENCE.csv` (SHA e `proof_url` na linha de origem). "Testado" e "Deploy" reproduzem o registro; `NOT_RUN` = não executado na auditoria.

| EVD | Path | Área / relevância para papéis | Maturidade | Testado | Deploy | Public-safe | Confiança |
|---|---|---|---|---|---|---|---|
| EVD-D-001 | apps/workflow/ | Agentic AI/Automation (strong); Architecture/Cloud (strong); Project & Process; AI Governance (HITL gates) | L3 | Y: 8 files, 64/64 pass (npx vitest run, local) | PARTIAL: wrangler config + bootstrap; deploy URL returns 404 (no live demo) | REDACT | HIGH |
| EVD-D-002 | apps/workflow/examples/cadeia/aikb-0001/ | Product & Value; Project & Process (dependency mapping, optimisation); Agentic AI | L2 | NOT_RUN (no own tests) | N/A | PUBLIC after content review | MEDIUM |
| EVD-D-003 | apps/site/ | Product & Value; Project & Process; Architecture/Cloud; Change (single hub) | L3 | Y: worker.test.js 15/15; node tests 17/17 (local) | YES (partial): live Worker 302 → /login; SHA match not provable | REDACT/SECURITY | HIGH |
| EVD-D-004 | .github/workflows/deploy-site.yml | Architecture/Cloud; AI Management Systems (gated pipeline) | L2 | N/A | Config only; Actions runs NOT_VERIFIED | PUBLIC | HIGH |
| EVD-D-005 | .claude/agents/ | Agentic AI (strong); AI Governance (tool/evidence restrictions per agent) | L2 | NOT_RUN | Bind to Worker via env vars (not versioned) | PUBLIC (REDACT name) | HIGH |
| EVD-D-006 | .claude/skills/ | AI Governance + AI Management Systems (traceability, ISO anchoring); Project & Process; Agentic AI | L2 | NOT_RUN (validators exist, not executed) | N/A | PUBLIC (check intake form first) | MEDIUM |
| EVD-D-007 | plugins/executar-cop/ | Agentic AI (strong: ablation eval); AI Management Systems (evaluation); Product & Value | L2 | PARTIAL: eval self-reported, NOT_RUN | N/A | NEEDS ATTRIBUTION | MEDIUM |
| EVD-D-008 | plugins/agent-handoff/ | Agentic AI (method adoption) | n/a (vendored) | NOT_RUN | N/A | THIRD-PARTY (MIT, WillowRyu) — use/adoption only | HIGH |
| EVD-D-009 | packages/design-system/ | Product & Value (UX); Communication | L2 | NOT_RUN | Served by Worker 'design' behind login | PUBLIC (without Apple captures) | MEDIUM |
| EVD-D-010 | apps/site/cms/src/views/storybook.jsx | Product/Design | L2 | Indirect | With site | PUBLIC | HIGH |

<!-- page -->
# 5 · Evidence Gap Report — PORTFOLIO_EVIDENCE (2/2)

Maturidade L0–L4 conforme `data/PORTFOLIO_EVIDENCE.csv` (SHA e `proof_url` na linha de origem). "Testado" e "Deploy" reproduzem o registro; `NOT_RUN` = não executado na auditoria.

| EVD | Path | Área / relevância para papéis | Maturidade | Testado | Deploy | Public-safe | Confiança |
|---|---|---|---|---|---|---|---|
| EVD-D-011 | EXECUTAR_Claude_Design/ | Architecture; Product & Value | L1 | N/A | N/A | PUBLIC without Apple captures | HIGH |
| EVD-D-012 | docs/adr/ADR-CENTRAL-CONTROLE-CMS.md; docs/prd/; docs/migrations/; docs/AGENT-RUNBOOK.md | Product & Value; Project & Process; Change | L1 | N/A | N/A | PUBLIC (AlsoAsked CSVs NEEDS_PERMISSION) | MEDIUM |
| EVD-D-013 | apps/scroll-task/ | Product & Value (PRD → prototype) | L2 | NOT_RUN | N/A | PUBLIC | HIGH |
| EVD-D-014 | apps/site/content/articles/ | Communication; Change | L1 | N/A | Preview inside CMS behind login; apps/blog absent | PUBLIC (review) | MEDIUM |
| EVD-W-001 | 00_Workbook/registros/adr/ADR-001_arquitetura-unificada-workbooks.md | AI Governance / AI Management Systems (traceability); Architecture (information architecture) | L1 | N/A | N/A | PUBLIC | HIGH |
| EVD-W-002 | 500_Copiloto_templates/scripts/workbook.py | AI Management Systems (controls, completeness, evidence); Project & Process; AI Governance | L2 | PARTIAL: no test suite; 'check ok' (local) | N/A (no CI) | PUBLIC | HIGH |
| EVD-W-003 | 00_Workbook/registros/ENTIDADES.csv; registros/fichas/AGT-001..006 | AI Governance (agent registry / AI inventory, central for AI Act/ISO 42001); Agentic AI | L1–L2 | via check | N/A | PUBLIC | HIGH |
| EVD-W-004 | D01–D16 + MACROAREAS.csv + OWNERS.csv + MASTER_INDEX.csv/entities.json + workbooks/A##/workbook.yaml + TPL-001..023 | Change / operating model; Project & Process; AI Management Systems | L1 | via check | N/A | PUBLIC | HIGH |
| EVD-W-005 | _sources/SRC-DOC-001..003 | Product & Value; Process | L1 | N/A | N/A | NEEDS_PERMISSION/REVIEW | MEDIUM |

<!-- page -->
# 5 · Evidence Gap Report — maturidade por família e bandeiras

## Maturidade por família de vaga (SRC-003 §4)

| Família | Nível | Evidências principais | O que falta para subir |
|---|---|---|---|
| Agentic AI / Automation | **L3** | EVD-D-001 (64/64 testes; deploy 404, sem demo viva); EVD-D-005/EVD-D-006 (6 subagentes, fila WIP=1); EVD-D-007 (eval 4/4 com vs. 0/4 sem, auto-relatada, NOT_RUN) | Demo pública viva, logs de execução, custo e taxa de sucesso por agente, reexecução da eval (GAP-011) |
| Arquitetura / Cloud (transversal) | **L3** | EVD-D-001; EVD-D-003; CI EVD-D-004 (pula silenciosamente sem secrets; runs NOT_VERIFIED) | Evidência de runs de CI; diagrama C4 em inglês (GAP-014) |
| Product & Value | **L2–L3** | EVD-D-003 (15/15 + 17/17 testes; Worker vivo atrás de login); EVD-D-013 (PRD → protótipo, L2); EVD-D-012 (L1) | Discovery com usuários; métricas de adoção e outcome (GAP-007) |
| Project & Process Mgmt | **L2** | EVD-D-001 (gates G01/G04/G06); EVD-D-003 (Gantt, DAG); EVD-D-002 (cadeia AIKB-0001); EVD-W-002 | Projeto entregue a terceiros; planejado vs. real |
| AI Management Systems | **L2** | EVD-W-002 ("check ok", checksums, completude); EVD-D-006 (ancoragem ISO 9001/10005/10006/21502/31000/10075-2) | AIMS ISO 42001 explícito; auditoria e indicadores de controle (GAP-004) |
| AI Governance | **L1–L2** | Gates humanos; política "sem evidência = GAP"; registro de 6 agentes EVD-W-003 (draft); ADR-001 EVD-W-001. Busca por EU AI Act/42001 nos repositórios: zero ocorrências relevantes | Classificação de risco pelo AI Act, avaliação de impacto, mapeamento 42001, política de dados/PII (GAP-004; GAP-013) |
| Change Management | **L1** | Apenas indireto: EVD-D-012 (ADR do hub, ritual semanal); EVD-W-004 | Adoção por terceiros; plano ADKAR com indicadores (GAP-007; GAP-008) |
| Comunicação (transversal) | **L1** | EVD-D-014 (4 artigos MDX), READMEs e ADRs, quase tudo em pt-BR | Versões em inglês (GAP-005) |

## Bandeiras de segurança e privacidade
| Item | Classificação | Ação | Vínculo |
|---|---|---|---|
| Credenciais de fallback hardcoded no Worker vivo do CMS (EVD-D-003; commit `52c34d6`) | SECURITY (P0) | Confirmar os secrets ou remover o fallback antes de compartilhar qualquer URL, só com autorização | GAP-003; DEC-014; RISK-005; KPI-023 |
| Histórico git não varrido por scanner de segredos | SECURITY | gitleaks/trufflehog nos dois repositórios | TASK-0004; GAP-003 |
| API do workflow pública por padrão sem `API_TOKEN` (EVD-D-001) | SECURITY | Exigir token em produção | GAP-003 |
| Nome pessoal como owner de gates (EVD-D-001, EVD-D-005) | REDACT | Substituir por papel | GAP-021; RISK-006 |
| IDs de KV e subdomínio derivado da conta (EVD-D-001, EVD-D-003) | REDACT (baixo risco) | Decidir exposição | GAP-021 |
| Plugins e skills de terceiros MIT/Apache-2.0 (EVD-D-006, EVD-D-007, EVD-D-008) | PUBLIC com atribuição | Nunca apresentar como autoria própria | DEC-018 |
| Capturas de páginas de terceiros (EVD-D-009, EVD-D-011) | PRIVATE | Não publicar | RISK-006 |
| CSVs AlsoAsked (EVD-D-012); `_sources/SRC-DOC-001..003` (EVD-W-005) | NEEDS_PERMISSION / REVIEW | Conferir termos; não publicar sem revisão | GAP-021 |

## Clean Sea, Frankswaching e demais iniciativas
**Clean Sea (REPO-004) e Frankswaching (REPO-006) são `GAP`/`NOT_VERIFIED`**: zero ocorrências nos dois repositórios auditados; nenhuma linha de CV ou portfólio pode citá-los sem outra fonte. EXECUTAR SaaS/app mobile/miniapps (REPO-003) e o blog `apps/blog` (REPO-005) existem só como nomes de branch ou referência e estão `NOT_VERIFIED`.

<!-- page -->
# 5 · Evidence Gap Report — GAP_BACKLOG priorizado (1/2)

Ordenado por prioridade (P0 → P3) e ID. Fonte: `data/GAP_BACKLOG.csv`; justificativa, recurso oficial, artefato de prova, dependências e vagas afetadas na linha de origem.

| GAP | Lacuna | Capacidades | Prioridade | Horas | Custo | Data-alvo | Ganho esperado | Status |
|---|---|---|---|---|---|---|---|---|
| GAP-001 | Dutch language level unknown | CAP-035 | P0 | 4 (week 1) then recurring (ESTIMATE) | PENDING_OFFICIAL_VERIFICATION | 2026-10-23 (PROPOSED) | ESTIMATE: eligibility effect (not FIT): may change blocker status on up to 44 active jobs; no index gain claimed | PROPOSED |
| GAP-002 | Professional baseline not verified | CAP-039;CAP-040;CAP-034;CAP-041;CAP-038;CAP-037;CAP-036;CAP-029;CAP-014;CAP-024;CAP-042;CAP-027 | P0 | 2 (ESTIMATE) | 0 | 2026-10-19 (PROPOSED) | ESTIMATE: eligibility effect (not FIT): may change blocker status on up to 51 active jobs; no index gain claimed | PROPOSED |
| GAP-003 | Security fix before any public sharing | CAP-031;CAP-017 | P0 | 4 (ESTIMATE) | 0 | 2026-10-20 (PROPOSED) | ESTIMATE: no direct FIT index gain (risk control; protects credibility on 5 active jobs) | PROPOSED |
| GAP-006 | Years-of-experience framing | CAP-039 | P0 | 3 (ESTIMATE) | 0 | 2026-10-23 (PROPOSED) | ESTIMATE: eligibility effect (not FIT): may change blocker status on up to 24 active jobs; no index gain claimed | PROPOSED |
| GAP-004 | No EU AI Act / ISO 42001 artefacts | CAP-015;CAP-016;CAP-018;CAP-021;CAP-022 | P1 | 6 (v0) + 14 (v1) (ESTIMATE) | 0 | 2026-11-13 (PROPOSED; v0 by 2026-10-23) | ESTIMATE: +43.2 pts mean FIT index over 13 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-005 | English portfolio and anchor case | CAP-033;CAP-034 | P1 | 1.5 + 6 (ESTIMATE) | 0 | 2026-10-25 (PROPOSED) | ESTIMATE: +5.5 pts mean FIT index over 14 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-007 | No L4 evidence / third-party adoption | CAP-026;CAP-008;CAP-029 | P1 | 20 (ESTIMATE) | 0 | 2027-01-29 (PROPOSED) | ESTIMATE: +11.1 pts mean FIT index over 12 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-010 | AIGP knowledge diagnostic | CAP-015;CAP-016;CAP-018 | P1 | 10 study + 4 mocks (week 1, ESTIMATE) | 0 (diagnostic) | 2026-10-22 (PROPOSED) | ESTIMATE: +19.8 pts mean FIT index over 13 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-011 | Live demo and re-run evals | CAP-001;CAP-004;CAP-023 | P1 | 16 (ESTIMATE) | 0 | 2026-11-20 (PROPOSED) | ESTIMATE: +7.1 pts mean FIT index over 17 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-015 | Re-verify USER_CLAIM drafts and pending official fields | — | P1 | 2 (ESTIMATE) | 0 | 2026-10-23 (PROPOSED) | ESTIMATE: no direct FIT index gain (enabler/risk control) | PROPOSED |
| GAP-021 | Redaction and attribution | CAP-017;CAP-033 | P1 | 3 (ESTIMATE) | 0 | 2026-10-21 (PROPOSED) | ESTIMATE: no direct FIT index gain (enabler/risk control) | PROPOSED |

<!-- page -->
# 5 · Evidence Gap Report — GAP_BACKLOG priorizado (2/2)

Ordenado por prioridade (P0 → P3) e ID. Fonte: `data/GAP_BACKLOG.csv`; justificativa, recurso oficial, artefato de prova, dependências e vagas afetadas na linha de origem.

| GAP | Lacuna | Capacidades | Prioridade | Horas | Custo | Data-alvo | Ganho esperado | Status |
|---|---|---|---|---|---|---|---|---|
| GAP-008 | Change plan with indicators | CAP-026 | P2 | 8 (ESTIMATE) | 0 | 2026-12-18 (PROPOSED) | ESTIMATE: +15.2 pts mean FIT index over 8 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-009 | Microsoft stack absent | CAP-003;CAP-032 | P2 | 12 (ESTIMATE) | PENDING_OFFICIAL_VERIFICATION | 2027-01-15 (PROPOSED) | ESTIMATE: +14.6 pts mean FIT index over 10 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-013 | Privacy safeguards | CAP-019 | P2 | 8 (ESTIMATE) | 0 | 2026-12-04 (PROPOSED) | ESTIMATE: +8.3 pts mean FIT index over 3 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-016 | Business case and roadmap artefact | CAP-009;CAP-028 | P2 | 8 (ESTIMATE) | 0 | 2026-12-11 (PROPOSED) | ESTIMATE: +19.3 pts mean FIT index over 3 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-012 | UiPath platform knowledge | CAP-002 | P3 | 2 study + 2 mock (ESTIMATE) | 0 | 2026-10-22 (PROPOSED) | ESTIMATE: +20.0 pts mean FIT index over 4 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-014 | CI evidence and documentation discrepancies | CAP-031 | P3 | 3 (ESTIMATE) | 0 | 2026-11-06 (PROPOSED) | ESTIMATE: no direct FIT index gain (enabler/risk control) | PROPOSED |
| GAP-017 | Process mining (deferred) | CAP-013 | P3 | N/A (DEFERRED) | 0 | 2027-03-31 (PROPOSED, DEFERRED) | ESTIMATE: no direct FIT index gain (enabler/risk control) | PROPOSED |
| GAP-018 | Product ownership (optional) | CAP-010;CAP-007 | P3 | 16 (ESTIMATE) | USD 200 if exam (BUD-009, NOT_APPROVED) | 2027-02-26 (PROPOSED) | ESTIMATE: +7.7 pts mean FIT index over 6 active jobs (projected levels, not evidence) | PROPOSED |
| GAP-019 | Hands-on coding ownership (technical track only) | CAP-005 | P3 | N/A (DEFERRED) | 0 | TBD (PROPOSED) | ESTIMATE: no direct FIT index gain (enabler/risk control) | PROPOSED |
| GAP-020 | Data governance literacy (deferred) | CAP-025 | P3 | N/A (DEFERRED) | PENDING_OFFICIAL_VERIFICATION | TBD (PROPOSED) | ESTIMATE: no direct FIT index gain (enabler/risk control) | PROPOSED |

Ganhos `ESTIMATE` usam níveis projetados, não evidência, e não são probabilidade de contratação. Itens com dependência de autorização (GAP-003, GAP-007, GAP-011, GAP-014, GAP-021) não avançam sem ordem explícita do usuário.
