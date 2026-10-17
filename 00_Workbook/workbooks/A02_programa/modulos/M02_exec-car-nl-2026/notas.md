---
id: WB-A02-M02-NOT
type: notes
workbook_id: WB-A02
macroarea_id: A02
owner: MA.PRG
title: Notas
status: draft
version: 0.1.0
updated: 2026-10-17
source_refs: [SRC-001, SRC-002, SRC-003, SRC-009, SRC-010]
---
<!-- page -->
# Notas · 1/3 — Decisões e observações

Todas as decisões abaixo estão PROPOSED e exigem aprovação do usuário (owner do papel MA.PRG).

| DEC | Decisão | Estado |
|---|---|---|
| DEC-001 | AI Governance route: IAPP AIGP as MAIN | PROPOSED |
| DEC-002 | AI Automation route: UiPath AAA OPTIONAL; ADA/AAP/AABP/ADP DEFERRED; Specialized AI DROPPED | PROPOSED |
| DEC-003 | Product Ownership route: PSPO I OPTIONAL; PSPO-AI and PSPO II DEFERRED | PROPOSED |
| DEC-004 | Project Management route: PRINCE2 v7 F/P DEFERRED; PRINCE2 Agile DROPPED; PMP/IPMA DEFERRED as alternatives | PROPOSED |
| DEC-005 | AI Management Systems: PECB ISO/IEC 42001 DEFERRED | PROPOSED |
| DEC-006 | Change Management: Prosci DEFERRED | PROPOSED |
| DEC-007 | Process Management: OMG BPM 2 Fundamental DROPPED | PROPOSED |
| DEC-008 | Market-named credentials outside the plan DEFERRED | PROPOSED |
| DEC-009 | Treat draft data (Gtm_Profissional.md lines 336+) as USER_CLAIM | PROPOSED |
| DEC-010 | Baseline NOT_VERIFIED handling | PROPOSED |
| DEC-011 | Scoring weights MUST 60 / NICE 25 / DIFF 15 (renormalised) | PROPOSED |
| DEC-012 | Include Dutch-language study from week 1 | PROPOSED |
| DEC-013 | Do not apply to Avans AI Compliance Officer (JOB-T-019) | PROPOSED |
| DEC-014 | Security fix before sharing any URL | PROPOSED |
| DEC-015 | JOB-A-024 treated as STALE; 52 VERIFIED_ACTIVE | PROPOSED |
| DEC-016 | Assume no functional Dutch until proven | PROPOSED |
| DEC-017 | Active jobs are archetypes | PROPOSED |
| DEC-018 | Authorship narrative for AI-assisted work | PROPOSED |
| DEC-019 | TOGAF EA Foundation DEFERRED | PROPOSED |
| DEC-020 | Time allocation per phase (40 h/week, BUFFER carved) | PROPOSED |
| DEC-021 | BUFFER content and holiday handling | PROPOSED |
| DEC-022 | Dutch study inside ACTIVE_STUDY | PROPOSED |
| DEC-023 | Keep Part 1 PROPOSED exam dates (feasibility checked) | PROPOSED |
| DEC-024 | Roadmap granularity and horizon | PROPOSED |
| DEC-025 | Week-1 class mapping follows the report | PROPOSED |
| DEC-026 | Pipeline segmentation and CV variants | PROPOSED |

<!-- page -->
# Notas · 2/3 — Lacunas e premissas

**Baseline NOT_VERIFIED:** CV, LinkedIn, histórico com anos por função, diploma e equivalência HBO/WO, nível de neerlandês, certificações existentes, orçamento, cidades preferidas, permissão de divulgação de trabalhos anteriores.

**Fora do escopo auditado (GAP/NOT_VERIFIED):** EXECUTAR SaaS em outros repositórios, Clean Sea, Frankswaching, landing page, publicações.

**Premissas (ASSUMPTION):** 40 h/semana contínuas inclusive após a mudança; feriados BR/NL tratados como BUFFER; horas planejadas de estudo e de lacunas são ESTIMATE; datas de prova PROPOSED.

**Lacunas:** GAP-001 (P0), GAP-002 (P0), GAP-003 (P0), GAP-004 (P1), GAP-005 (P1), GAP-006 (P0), GAP-007 (P1), GAP-008 (P2), GAP-009 (P2), GAP-010 (P1), GAP-011 (P1), GAP-012 (P3), GAP-013 (P2), GAP-014 (P3), GAP-015 (P1), GAP-016 (P2), GAP-017 (P3), GAP-018 (P3), GAP-019 (P3), GAP-020 (P3), GAP-021 (P1).

**Capacidades sem avaliação possível (NOT_VERIFIED):** CAP-014, CAP-024, CAP-027, CAP-029, CAP-035, CAP-036, CAP-037, CAP-038, CAP-039, CAP-040, CAP-042.

<!-- page continuation -->
**Conflitos de fonte registrados:** preço do UiPath AABP (EDD vs FAQ); regra 27% para quem iniciou em 2024–2026; multas DBA em 2026; status da Wet VBAR; contagem de gigs freelance no texto vs tabela da nota de automação.

<!-- page -->
# Notas · 3/3 — Revisão e histórico

| Data | Evento |
|---|---|
| 2026-10-17 | Pesquisa paralela (vagas ×2, certificações, auditoria de repositórios, contexto NL) e relatório `SRC-003`. |
| 2026-10-17 | Camada de dados (23 CSVs) gerada e validada (referências, horas, marcos, privacidade). |
| 2026-10-17 | Documentos do módulo gerados a partir dos CSVs. |

**Ledger resumido:** 219 fontes; 52 vagas VERIFIED_ACTIVE; 16 credenciais com campos PENDING_OFFICIAL_VERIFICATION.

**Autoavaliação Q8 (0–2):** Fidelidade 2 (datas, 40 h, regras de evidência preservadas) · Completude 2 (9 saídas e 23 tabelas) · Grounding 2 (fonte e data por vaga/cert, rótulos onde falta) · Executabilidade 2 (Semana 1 com 40 h e critérios SMART) · Eficiência 1 (volume alto; requer curadoria quinzenal) · Formato 2 (layout ADR-001, CSV UTF-8) = **11/12**. Ponto fraco: FIT com base de requisitos pequena em várias vagas (LOW BASE) e baseline ausente.

**Q1–Q7:** Q1 cobertura EPIC 00–09 em `data/EPICS_ISSUES_TASKS.csv` · Q2 todas as semanas somam 40 h (validador) · Q3 fontes/datas ou NOT_VERIFIED · Q4 rota sem redundância com justificativa de ROI · Q5 simulados ≠ exames oficiais, casos sem clientes fictícios · Q6 shortlist 0/30/60/90 · Q7 nenhum segredo, contato privado ou nome pessoal publicado.
