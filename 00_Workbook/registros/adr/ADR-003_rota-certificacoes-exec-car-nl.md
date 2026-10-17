---
id: ADR-003
type: adr
title: Rota de certificações e alocação de 40 h do programa EXEC-CAR-NL-2026
status: PROPOSED
version: 0.1
date: 2026-10-17
approved:
approved_by:
macroarea_id: A02
owner: MA.PRG
scope: Programaex/workbook
source_refs: [SRC-DOC-004]
---
# ADR-003 — Rota de certificações e alocação de 40 h (EXEC-CAR-NL-2026)

Versão 0.1 · 17/10/2026 · **Estado: PROPOSED** (aguarda aprovação do owner)

## 1. Contexto

O programa de carreira EXEC-CAR-NL-2026 (módulo `WB-A02-M02`) mira o cargo de AI Transformation Manager nos Países Baixos, com início em 19/10/2026, 40 h/semana, candidaturas formais de 01/02 a 30/03/2027 e viagem-alvo em 30/04/2027. O rascunho do usuário (`SRC-DOC-004`, linhas 336+, USER_CLAIM) propunha 8 credenciais. A pesquisa de 17/10/2026 verificou 52 vagas ativas e as páginas oficiais dos emissores (`data/SOURCE_REGISTER.csv` do módulo).

## 2. Evidência

- Somente o IAPP AIGP, entre as credenciais do rascunho, é citado literalmente em vagas ativas (2 de 52). PSPO, PRINCE2, PMP, Prosci, UiPath e OCEB não aparecem.
- Neerlandês e anos de experiência são os filtros dominantes, à frente de certificações.
- PECB ISO/IEC 42001 LI sem experiência gera apenas "Provisional Implementer". Prosci custa USD 4.500+ com curso obrigatório.

## 3. Decisão proposta

| Domínio | Credencial | Papel |
|---|---|---|
| AI Governance | IAPP AIGP (BoK v2.1) | MAIN |
| AI Automation / Agents | UiPath Agentic Automation Associate | OPTIONAL |
| Product Ownership | Scrum.org PSPO I | OPTIONAL |
| Project Management | PRINCE2 v7 Foundation/Practitioner | DEFERRED |
| AI Management Systems | PECB ISO/IEC 42001 LI | DEFERRED |
| Change Management | Prosci | DEFERRED |
| Process Management | OMG BPM 2 Fundamental | DROPPED |

Neerlandês entra em ACTIVE_STUDY desde a Semana 1. Horas por fase seguem a hipótese do prompt mestre com BUFFER explícito (DEC-020…DEC-022). As datas de prova são PROPOSED e nenhuma inscrição ocorre sem G0–G5.

## 4. Consequências

- Custo do núcleo (preços oficiais na moeda original): USD 1.149, contra cerca de USD 2.628 do rascunho (`data/BUDGET.csv`).
- Credenciais adiadas são reavaliadas na revisão mensal (CONTINUE/DEFER/DROP) quando aparecerem em vagas-alvo ou quando houver lacuna demonstrada.

## 5. Referências

`00_Workbook/workbooks/A02_programa/modulos/M02_exec-car-nl-2026/data/DECISION_LOG.csv` (DEC-001…DEC-026), `CERTIFICATIONS.csv`, `EXAM_GATES.csv`, `ROADMAP_WEEKLY.csv`.
