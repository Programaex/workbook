# Neerlandês e anos comprovados abrem portas; certificados, não

**BLUF.** Em 17/10/2026 o mercado neerlandês tem demanda real e verificável nas seis famílias-alvo: **52 vagas VERIFIED_ACTIVE** nas duas amostras (36 em transformação/governança e 16 em automação/produto/processo). Para este candidato, porém, o gargalo **não é certificação**. São três bloqueios que nenhum curso resolve. O primeiro é o **neerlandês**, exigido explicitamente em **26 das 52 vagas** e provável em outras 17 escritas só em neerlandês. O segundo são os **anos de experiência comprovados**: 5–15 anos nos cargos de manager. O terceiro é um **baseline ainda NOT_VERIFIED** (CV, LinkedIn, histórico, diploma e nível de neerlandês). Os certificados aparecem pouco nos anúncios. **IAPP AIGP** é a credencial do plano mais citada (2 de 36, como preferencial). **PSPO, PRINCE2, Prosci, UiPath e OCEB têm zero menções** nas vagas ativas verificadas, então a rota paga deve ser enxuta: AIGP como exame principal, UiPath Agentic Automation Associate e PSPO I como baratos e opcionais, e o resto adiado. Os repositórios `programaex/design` e `programaex/workbook` sustentam evidência **L3 em Agentic AI/Automation e Arquitetura** (96 testes passando localmente e um Worker vivo). Governança de IA fica em L1–L2 e change management em L1, e **nada chega a L4**. Há uma credencial padrão hardcoded num site vivo, que deve ser corrigida antes de qualquer divulgação. As portas abertas agora (APPLY) são poucas e condicionadas: Loyens & Loeff, The Automation Group e, se houver histórico comercial, Deeploy. Em 30–90 dias a rota é BRIDGE: inglês-first corporativo, freelance PME e governança em nível mid. AI Transformation Manager é TARGET_LATER. Na primeira semana (19–25/10/2026), o trabalho é fechar o baseline, corrigir a segurança, iniciar o diagnóstico AIGP e o neerlandês, e reconfirmar as alegações dos rascunhos.

---

## 1. Executive one-page: o alvo é viável, mas o atalho é ponte e não título

| Campo | Situação em 17/10/2026 |
|---|---|
| Posição-alvo (longo prazo) | AI Transformation Manager. As vagas reais dessa família pedem 8+ anos de consultoria e ≥1 projeto de adoção de IA entregue (Eraneos), ou 5–10 anos (Anderson MacGyver, Fellowmind). |
| Posições-ponte realistas | Junior Innovation/Adoption, AI Project Lead/BA, Agentic AI trainee/consultant, AI Governance/Compliance (mid), freelance de automação para PMEs |
| Baseline verificado | **Somente** cidadania UE e inglês fluente (USER_CLAIM declarado). CV, LinkedIn, histórico de trabalho, anos de experiência, diploma (HBO/WO), nível de neerlandês, certificações existentes e orçamento: **NOT_VERIFIED** |
| Evidência de portfólio | L3: Agentic AI/Automation e Arquitetura/Cloud. L2–L3: Product. L2: Project/Process e AI Management Systems. L1–L2: AI Governance. L1: Change. L4: nenhuma. Clean Sea e Frankswaching: **GAP** |
| Datas rígidas | 19/10/2026 início (40 h/semana) · 19/11/2026 épico Emprego & Realocação · 01/02–30/03/2027 candidaturas formais · 30/04/2027 viagem |

**Top 5 lacunas**, na ordem em que bloqueiam:

1. Nível de neerlandês desconhecido. É gate em 26/52 vagas.
2. Anos e tipo de experiência não comprovados. É gate em todas as vagas MID+.
3. Ausência de artefatos de EU AI Act e ISO 42001 no portfólio. O AI Act aparece em 11/36 vagas.
4. Nenhuma evidência L4: sem usuários, métricas ou adoção por terceiros. Change/adoção aparece em 11/36.
5. Portfólio público ainda não seguro nem em inglês: credencial padrão no site vivo, documentação só em pt-BR, material de terceiros sem distinção de autoria e lacuna de stack Microsoft (9/36).

**Cinco ações desta semana:**

1. Fechar o baseline (CV, LinkedIn, anos, diploma, nível CEFR de neerlandês).
2. Decidir sobre o fallback `000/003` do CMS e rodar um scanner de segredos no histórico. Nos dois casos, o usuário precisa autorizar a mudança.
3. Fazer o diagnóstico AIGP BoK v2.1 por domínio (G1).
4. Começar o neerlandês com teste de nivelamento.
5. Reverificar as vagas e certificações dos rascunhos marcadas como USER_CLAIM e montar o pipeline com as 52 vagas.

**Decisões pendentes do usuário:**

- Orçamento de certificações (G4).
- Autorização para alterar repositórios e publicar (G5 e regra 7 do prompt).
- Cidade preferida.
- Aceitar ou não papéis-ponte com início antes de 30/04/2027, o que esbarra em seguridade social e trabalho remoto.

**Riscos principais:**

- As vagas ativas hoje expiram antes da janela de fevereiro. Avans fecha em 20/10 e ILT em 27/10.
- O DBA restringe o freelance corporativo.
- Com 27% em vez de 30% a partir de 2027, o líquido fica menor.
- O histórico de commits é curto e majoritariamente do agente, o que exige uma narrativa honesta de autoria.

---

## 2. Headhunter Market Report: 52 vagas ativas, 26 exigem neerlandês

### Amostra real e método

A amostra foi construída em **17/10/2026** a partir de duas notas independentes, e os números abaixo são **contagens amostrais, não totais de mercado**. A nota de transformação/governança reúne **36 vagas distintas VERIFIED_ACTIVE**, com página aberta (HTTP 200), texto completo e sem aviso de encerramento. A cobertura pesa para o LinkedIn, lido pela visualização pública de convidado. A nota de automação/produto/processo reúne **24 registros**: **16 VERIFIED_ACTIVE** (9 empregos/traineeships e 7 freelance), **1 em conflito** (Capgemini Invent, A-007) e **7 UNVERIFIED**, só por snippet ou com fetch bloqueado (ING, ABN AMRO, Workwize, KLM, Ahold Delhaize, Nanzen FDA e mais um). Essa nota tem uma inconsistência interna: o texto lista **8** gigs freelance como ativos (A-017 a A-024), mas o resumo conta 7. O provável excedente é o A-024, publicado há cerca de 3 meses, que aqui é tratado como **STALE, a reconfirmar**. O total combinado é **52 VERIFIED_ACTIVE**. Fica abaixo da meta de 30–50 por família pedida no prompt, mas dentro da meta agregada. Não há freelance de governança/transformação ativo: os dois encontrados, EZK/Sogeti a €105/h e Stedin, já estavam fechados ([GreenPepper](https://greenpepper.nl/vacatures/senior-adviseur-ai-beleid-ezk-rc152208/); [Freep](https://www.freep.nl/opdracht/epic-owner-ai-governance)).

Várias vagas citadas nos rascunhos do usuário estão **encerradas**. Booking.com "Change Manager – Data & AI Governance" dá HTTP 404 ([Booking](https://jobs.booking.com/booking/jobs/29913?lang=en-us)). Adyen "AI Transformation Manager – Finance" está arquivada ([The Muse](https://www.themuse.com/jobs/adyen/ai-transformation-manager-finance)). A página da Miro diz "no longer advertised" ([Miro](https://miro.com/careers/vacancy/8307077002/?gh_jid=8307077002)). Philips devolve 410 ([Philips](https://www.careers.philips.com/global/en/job/586396/AI-Transformation-Agentic-Platforms-Senior-Leader)). A vaga UiPath RPA Consultant da DICTU via HeadFirst também devolve 410 ([select.hr](https://select.hr/opdrachten/ministerie-van-economische-zaken-en-klimaat-dictu/uipath-rpa-consultant/52cd7667-6239-43ea-a831-a6c6df80b62f)), e era justamente a vaga que o rascunho usava para justificar a certificação UiPath Agentic Automation Professional. Randstad "Senior PM/PO AI Agents" também está em 410 ([Randstad Enterprise](https://www.randstadenterprise.com/careers/join-our-team/senior-product-manager-product-owner-ai-agents_diemen_47185186/)).

### Tabela consolidada das vagas VERIFIED_ACTIVE

Legenda de idioma: NL_REQ = neerlandês exigido explicitamente; EN = inglês suficiente explícito; UNK(NL)/UNK(EN) = não declarado, com anúncio em neerlandês ou inglês. U = não informado. Todas as vagas estão VERIFIED_ACTIVE em 17/10/2026, salvo nota em contrário.

**A. AI Transformation / mudança e adoção com IA**

| ID | Empregador | Título | Cidade | Senioridade | Idioma | Contrato | MUST_HAVE-chave |
|---|---|---|---|---|---|---|---|
| JOB-T-001 | Eraneos | [(Senior) Manager AI Transformatie](https://nl.linkedin.com/jobs/view/senior-manager-ai-transformatie-at-eraneos-4478419892) | Randstad (várias) | SENIOR/MANAGER | NL_REQ | U (permanente implícito), híbrido | WO; 8+ anos consultoria (Mgr) / 15+ (Sr Mgr); ≥1 projeto de adoção de IA; €6.238–10.166/mês |
| JOB-T-002 | Anderson MacGyver | [AI Transformation Consultant](https://nl.linkedin.com/jobs/view/ai-transformation-consultant-at-anderson-macgyver-4471445573) | IJsselstein | SENIOR | NL_REQ | U, híbrido | Master; 5–10 anos; entrega de soluções de IA; €5.000–7.500 |
| JOB-T-003 | Fellowmind | [AI Transformation Consultant](https://nl.linkedin.com/jobs/view/ai-transformation-consultant-at-fellowmind-4474279975) | Zwolle (gêmea em Deventer) | SENIOR | NL_REQ | U | 5–10 anos consultoria; plataforma Microsoft/Copilot Studio; conversas com board |
| JOB-T-004 | accelerAite | [Medior AI Verandermanager](https://nl.linkedin.com/jobs/view/medior-ai-verandermanager-bij-acceleraite-32-%E2%80%93-40-uur-at-acceleraite-4479805924) | 's-Hertogenbosch | MID | UNK(NL) | Permanente, 32–40 h | 3 anos de mudança/PM + 2 anos implementando IA; €4.750–5.750 |
| JOB-T-005 | Frisse Blikken | [Senior Transformation Lead – Mens & AI](https://nl.linkedin.com/jobs/view/senior-transformation-lead-mens-ai-at-frisse-blikken-4474698399) | Eindhoven | SENIOR | UNK(NL) | "maatwerk" | Transformações de IA org-wide; adoção/comportamento; coaching |
| JOB-T-006 | Accenture | [Transformational Change Manager](https://nl.linkedin.com/jobs/view/transformational-change-manager-at-accenture-the-netherlands-4478468786) | Amsterdam | SENIOR/MANAGER | NL_REQ | U | Master; 5+ anos incl. PM; mudança organizacional/HR |
| JOB-T-007 | Accenture | [Junior Technology Strategy & Transformation Consultant](https://nl.linkedin.com/jobs/view/junior-technology-strategy-transformation-consultant-at-accenture-the-netherlands-4477284689) | Amsterdam | ENTRY/JUNIOR | NL_REQ | U | Master concluído; notas WO/VWO excelentes; histórico escolar anexado |
| JOB-T-008 | Add Value (cliente na região de Utrecht) | [AI Adoptie specialist](https://www.add-value.nl/vacatures/ai-adoptieconsultant-amsterdam) | Den Bosch/Utrecht | MID | NL_REQ | U | Formação em AI/CS/DS; mudança/psicologia; €4.000–6.500 |
| JOB-T-009 | DICTU (Rijksoverheid) | [Senior Adviseur AI](https://www.werkenvoornederland.nl/vacatures/senior-adviseur-ai-DICT-2026-1315) | Assen/Den Haag/Zwolle | SENIOR | UNK(NL) | 12 meses → permanente, 36 h | HBO/WO; GenAI/RAG/agentic; experiência "ruime" em consultoria; prazo 31/12/2026 |
| JOB-T-010 | BearingPoint | [Microsoft Business Transformation Consultant Data & AI](https://nl.linkedin.com/jobs/view/microsoft-business-transformation-consultant-data-ai-at-bearingpoint-4469687910) | Amsterdam | SENIOR | NL_REQ | U | 8+ anos; business cases/roadmaps; Azure/Fabric/Copilot |
| JOB-T-011 | Corbion | [Global Head of Digital, Data & AI](https://nl.linkedin.com/jobs/view/global-head-of-digital-data-ai-at-corbion-4472323460) | Amsterdam/Gorinchem | SENIOR/MANAGER (Director) | UNK(EN) | U, 3 dias no escritório | Liderança de transformações enterprise em escala |

**B. AI Governance / Risk / Responsible AI / Compliance**

| ID | Empregador | Título | Cidade | Senioridade | Idioma | Contrato | MUST_HAVE-chave |
|---|---|---|---|---|---|---|---|
| JOB-T-012 | Athora NL | [AI Governance Specialist](https://nl.linkedin.com/jobs/view/ai-governance-specialist-at-athora-netherlands-4476040608) | Amsterdam | MID | UNK(NL) | U, híbrido, 36 h | WO; 3+ anos; EU AI Act/AVG; governança de GenAI/agentes; €5.082–6.776 |
| JOB-T-013 | Deloitte | [AI Risk Manager](https://nl.linkedin.com/jobs/view/ai-risk-manager-at-deloitte-4470178422) | Rotterdam | SENIOR | NL_REQ | U, híbrido | 5 anos; EU AI Act "absolute vereiste"; ISO 42001/27001; AIGP preferencial |
| JOB-T-014 | EY | [Manager Privacy & Responsible AI](https://nl.linkedin.com/jobs/view/admin-manager-privacy-responsible-ai-cyber-security-1-at-ey-4465534935) | Amsterdam | SENIOR/MANAGER | NL_REQ | Permanente, 40 h | Master; 5+ anos; AVG/AI Act/Data Act; CIPP/E, CIPM, CIPT |
| JOB-T-015 | Everience Benelux | [Responsible AI Lead](https://nl.linkedin.com/jobs/view/responsible-ai-lead-m-f-d-at-everience-benelux-4479379465) | Den Haag | SENIOR | UNK(EN) | U | 8–12+ anos; risco de IA; política→controles; NIST AI RMF/42001 |
| JOB-T-016 | Atos | [Senior AI Consultant – AI Trust & Governance](https://nl.linkedin.com/jobs/view/senior-ai-consultant-ai-trust-governance-at-atos-4418781842) | Amstelveen | SENIOR | NL_REQ | U | 6–10+ anos; Responsible AI; GenAI/arquitetura |
| JOB-T-017 | CGI | [Senior Data & AI Governance Specialist](https://nl.linkedin.com/jobs/view/senior-data-ai-governance-specialist-retail-consumer-products-at-cgi-nederland-4462054258) | Amsterdam | SENIOR | NL_REQ (C1+, nativo/quase nativo) | U, híbrido | 7+ anos; **DAMA CDMP ou DCAM obrigatório** |
| JOB-T-018 | KPMG | [Senior Consultant – Technology Assurance – AI](https://nl.linkedin.com/jobs/view/senior-consultant-technology-assurance-ai-at-kpmg-nederland-4474695396) | Rotterdam/Den Haag | MID | NL_REQ ("harde eis") | U, híbrido | 3+ anos de audit/risk; RE/CISA/CISM/CIPP (ou em curso); €3.965–4.500 |
| JOB-T-019 | Avans | [AI Compliance Officer](https://nl.linkedin.com/jobs/view/ai-compliance-officer-at-avans-university-of-applied-sciences-4476747466) | Breda | BRIDGE_ROLE | UNK(NL) | Temporário de 1 ano, 40 h | HBO; experiência em compliance/risk/privacy; **fecha 20/10/2026**; €3.826–5.699 |
| JOB-T-020 | Younicorp | [AI Governance Specialist](https://younicorp.com/vacature/ai-governance-specialist/) | U | MID | NL_REQ | % da receita ou salário | 4 anos no setor público; AVG/AI Act. Página sem data, possivelmente evergreen |
| JOB-T-021 | PwC | [(Senior) Associate – Legal Tech / Responsible AI](https://nl.linkedin.com/jobs/view/senior-associate%E2%80%AF-legal-tech%E2%80%AF-responsible-ai-at-pwc-nederland-4472520996) | Amsterdam | BRIDGE_ROLE | NL_REQ | Permanente | U (extração incompleta) |
| JOB-T-022 | Deeploy | [Partner Manager, AI Governance](https://nl.linkedin.com/jobs/view/partner-manager-ai-governance-at-deeploy-4473536341) | Amsterdam | BRIDGE_ROLE | **EN** | U, híbrido, stock options | 3+ anos em parcerias/vendas enterprise; case de 3 h |
| JOB-T-023 | MIVD | [AI management adviseur](https://nl.linkedin.com/jobs/view/de-rijksoverheid-zoekt-ai-management-adviseur-4471886475) | Zoetermeer | SENIOR | NL_REQ | U | **Nacionalidade neerlandesa** + ~10 anos de residência: inelegível |
| JOB-T-024 | ABN AMRO | [Strategy Advisor – Data & AI](https://nl.linkedin.com/jobs/view/strategy-advisor-data-ai-at-abn-amro-bank-n-v-4477800789) | Amstelveen | SENIOR | UNK(EN) | U, 36 h | Experiência "significant" em consultoria; Master; DAMA-DMBOK/AI Act |
| JOB-T-025 | Zanders | [AI Consultant – Financial Services & Risk](https://nl.linkedin.com/jobs/view/ai-consultant-%E2%80%93-financial-services-risk-at-zanders-4454984805) | Utrecht | MID/SENIOR | **EN** | U | Python forte; Azure/Databricks; 3–6 anos; setor financeiro |

**C. Coordenação de projetos de IA / BA / consultoria júnior**

| ID | Empregador | Título | Cidade | Senioridade | Idioma | Contrato | MUST_HAVE-chave |
|---|---|---|---|---|---|---|---|
| JOB-T-026 | Talent&Pro | [IT & AI Projectleider (Medior)](https://nl.linkedin.com/jobs/view/it-ai-projectleider-medior-at-talent-pro-4401404356) | Utrecht | BRIDGE_ROLE | UNK(NL) | U | HBO; 2–4 anos em projetos de TI; Copilot/Claude; €3.200–4.900 |
| JOB-T-027 | KickstartAI | [Project Manager Machine Learning & AI](https://nl.linkedin.com/jobs/view/project-manager-machine-learning-ai-at-kickstartai-4479819500) | Delft | MID | UNK(NL) | 12 meses → permanente | 3+ anos de PM em ML/AI; até €5.100 |
| JOB-T-028 | Verwater Group | [Business Analist Digitalisering & AI](https://nl.linkedin.com/jobs/view/business-analist-digitalisering-ai-at-verwater-group-b-v-4476450170) | Rotterdam | ENTRY/JUNIOR | NL_REQ | U | HBO; sem experiência exigida |
| JOB-T-029 | TADA Solutions | [Business Analyst Data & AI](https://nl.linkedin.com/jobs/view/business-analyst-data-ai-at-tada-solutions-4470282882) | Eindhoven | ENTRY/JUNIOR | NL_REQ | U | HBO/WO; consultoria/dados; €45–65 mil/ano |
| JOB-T-030 | TalentSpark by TSP | [Junior AI Consultant](https://nl.linkedin.com/jobs/view/junior-ai-consultant-at-talentspark-by-tsp-4478534983) | Rotterdam | ENTRY/JUNIOR | NL_REQ | U | HBO/WO; Python/JS básico |
| JOB-T-031 | Loyens & Loeff | [Junior Innovation Advisor](https://nl.linkedin.com/jobs/view/junior-innovation-advisor-at-loyens-loeff-4479557718) | Amsterdam | ENTRY/JUNIOR | **EN** | U, híbrido | Bacharel/mestre; autorização de trabalho NL (cidadão UE atende); a partir de €4.500 |
| JOB-T-032 | ING | [Agentic automation & AI Consultant](https://nl.linkedin.com/jobs/view/agentic-automation-ai-consultant-at-ing-nederland-4474404795) | Amsterdam | MID | UNK(EN) | U, híbrido, 13º salário | Consultoria em agentic automation/BA; squads ágeis; M365 Copilot/Copilot Studio/Power Platform |
| JOB-T-033 | Gaide | [AI Consultant](https://nl.linkedin.com/jobs/view/ai-consultant-at-gaide-4479538819) | Amsterdam | MID | NL_REQ | U | 3–5 anos client-facing |
| JOB-T-034 | CGI | [AI Consultant – Energie](https://nl.linkedin.com/jobs/view/ai-consultant-energie-at-cgi-nederland-4475022625) | Arnhem | MID | NL_REQ | Permanente, 32–40 h | 4+ anos; Python; cloud; IA em produção |
| JOB-T-035 | ILT (Rijksoverheid) | [Adviseur data science en AI](https://www.werkenvoornederland.nl/vacatures/adviseur-data-science-en-ai-ILT-2026-8099) | Utrecht | SENIOR | NL_REQ (C1) | 12 meses → permanente | WO; PhD preferido; VOG; **fecha 27/10/2026** |
| JOB-T-036 | Bit Traineeship | [Traineeship AI & Innovation (Dutch speaking)](https://nl.linkedin.com/jobs/view/traineeship-ai-innovation-dutch-speaking-at-bit-traineeship-4471705315) | Região de Amsterdam | ENTRY/JUNIOR | NL_REQ | U, híbrido | Master em IA/área quantitativa; Python |

**D. Automação / RPA / Agentic / Processo (emprego e trainee)**

| ID | Empregador | Título | Cidade | Senioridade | Idioma | Contrato | MUST_HAVE-chave |
|---|---|---|---|---|---|---|---|
| JOB-A-001 | CareerValue (cliente na Randstad) | [RPA Developer (UiPath)](https://www.careervalue.nl/vacatures/overige-ict-functies/vacature-in-utrecht-rpa-developer-uipath/) | Utrecht | ENTRY/JUNIOR–MID | NL_REQ | Permanente, 32–40 h | HBO; UiPath ou RPA similar; €2.800–5.800 |
| JOB-A-002 | CareerValue | [RPA Developer (UiPath)](https://www.careervalue.nl/vacatures/overige-ict-functies/vacature-in-rotterdam-rpa-developer-uipath/) | Rotterdam | ENTRY/JUNIOR–MID | NL_REQ | Permanente | Igual à A-001; provável template duplicado |
| JOB-A-003 | PMT Groep | [RPA Consultant](https://pmtgroep.nl/werken-bij-pmt/vacature-rpa-developer/) | Gouda / clientes na Randstad | MID | NL_REQ | U, 36–40 h | 3 anos de RPA (UiPath); HBO/WO; Agile; €3.500–5.500 |
| JOB-A-004 | ilionx | [RPA Developer (Hyperautomation)](https://www.consultancy.nl/vacatures/236948/ilionx/rpa-developer) | 's-Hertogenbosch/Amersfoort | MID/SENIOR | UNK(NL) | U, híbrido | 2 anos de programação; UiPath; C#/.NET; WO |
| JOB-A-005 | Itility | [Power Platform Consultant/Engineer](https://careers.itility.nl/o/power-platform-engineer) | Eindhoven/Heerlen | MID | NL_REQ | U, híbrido | 2+ anos de Power Platform; HBO/WO; PL-100/200/400 preferidos |
| JOB-A-006 | Alliander | [Process Mining Analist](https://freehire.me/jobs/process-mining-analist-4ojutpaf) ([EURES](https://europa.eu/eures/portal/jv-se/jv-details/NWNiZmEzYjQtMzQ1My1lZWRiLWUwNjMtNjg5M2IyMGFmY2RmIDQy?lang=en)) | Arnhem | MID/SENIOR | UNK(NL) | U, 32–40 h | Celonis; 4 anos segundo snippet (UNVERIFIED); fecha 30/11/2026. Ativa apenas na cópia do agregador |
| JOB-A-008 | Capgemini Engineering | [Junior Automation Engineer](https://careers.capgemini.com/job/Utrecht-Junior-Automation-Engineer/1197654001/) | Utrecht/Eindhoven | ENTRY/JUNIOR | UNK(NL) | Permanente | Engenharia elétrica / automação industrial. Fora do perfil |
| JOB-A-009 | The Automation Group | [Trainee: Agentic AI Engineer/Consultant](https://theautomationgroup.nl/en/careers/ai-trainees) | Utrecht | BRIDGE_ROLE | **EN** ("Dutch or English") | Traineeship de 6–9 meses, coortes trimestrais | **5 anos de experiência de negócio**; projetos próprios de agentes/automações |
| JOB-A-010 | Nanzen | [AI/agents engineer](https://wellfound.com/jobs/4574455-ai-agents-engineer) | Amsterdam | MID | EN (inferido) | Permanente | 2 anos; LLM em produção; evals; €70–130 mil + equity |

**E. Freelance/ZZP no Freelancer.nl (anúncios em neerlandês; idioma UNKNOWN; horas e duração não publicadas)**

| ID | Cliente | Título | Local | Termos | Stack |
|---|---|---|---|---|---|
| JOB-A-017 | Pequena empresa | [Copilot agents + Power Automate](https://freelancer.nl/opdrachten/delfzijl/python-ervaring-power-automate-ai-copilot/ondersteuning-bij-inrichten-copilot-agents-en-power-automate-8e1b8cb2) | Delfzijl | Taxa negociável | Power Automate, Copilot Studio, Python |
| JOB-A-018 | Consultoria | [AI developer gezocht](https://freelancer.nl/opdrachten/ai-n8n-claude-ai-codex-openai-api-rag-ai-agents-python-docker-n8n-developer-ai%20automation/ai-developer-gezocht-3f5ce288) | Remoto | Negociável | n8n, Claude, OpenAI, RAG, Python, Docker |
| JOB-A-019 | Agência de IA para PMEs | [Freelance AI-consultants en engineers](https://freelancer.nl/opdrachten/ai-ai-consultant-ai-training-consultancy/freelance-ai-consultants-en-engineers-gezocht-voor-groeiend-ai-bureau-voor-het-mkb-50653145) | Remoto | Negociável | Agentes, treinamento em IA, Exact/AFAS/M365 |
| JOB-A-020 | Empresa que usa Claude/ChatGPT/HeyGen | [Opzetten AI-structuur en workflows](https://freelancer.nl/opdrachten/noordwijkerhout/ai-automation-claude-gpt-proces%20optimalisatie/opzetten-ai-structuur-en-workflows-op-locatie-b5d9fe8d) | Noordwijkerhout (presencial) | **€40–60/h** | Claude, GPT, processos |
| JOB-A-021 | Assistentes de IA para PMEs | [Hermes en n8n](https://freelancer.nl/opdrachten/ai-automation-n8n/freelance-developer-gezocht-hermes-en-n8n-51a75b72) | Remoto | Negociável | Hermes Agent, n8n, APIs |
| JOB-A-022 | Startup imobiliária | [Afronding AI-platform](https://freelancer.nl/opdrachten/rotterdam/python-ai-development-software-development/ai-specialist-gezocht-voor-technische-afronding-en-lancering-bestaand-ai-platform-92c52e6a) | Rotterdam | **Fixo €500–1.000** | Python, IA |
| JOB-A-023 | "Executive operator" | [Lindy opstart en integratie](https://freelancer.nl/opdrachten/ai-ai-agents-automation-ai-workflows/ai-specialist-gezocht-lindy-opstart-en-integratie-62110f51) | Remoto | Negociável | Lindy, agentes |
| JOB-A-024 | Empresa de alimentos | [AI/Airtable/n8n specialist](https://freelancer.nl/opdrachten/continuous-improvement-ai-n8n-make-automation/ai-airtable-n8n-specialist-gezocht-voor-business-dashboard-en-mailbox-automatisatie-db047724) | Remoto | Negociável | Airtable, n8n/Make. **STALE?** (~3 meses) |

Os registros UNVERIFIED ou em conflito ficam fora da contagem. São eles: Capgemini Invent Junior Intelligent Process & Performance, em conflito entre a cópia [banken.nl](https://www.banken.nl/vacatures/34335/capgemini-invent/junior-consultant-intelligent-process-performance) e a cópia fechada no [consultancy.nl](https://www.consultancy.nl/vacatures/230618/capgemini-invent/junior-consultant-intelligent-process-and-performance); Nanzen Forward Deployed Analyst ([Wellfound](https://wellfound.com/role/l/ai-engineer/amsterdam)); ING Senior AI Engineer Agentic ([snippet](https://agentic-engineering-jobs.com/jobs/ing-senior-ai-engineer-agentic-ai-1He8rt)); ABN AMRO ML & Agentic AI Engineer ([Glassdoor](https://www.glassdoor.com/Job/netherlands-artificial-intelligence-engineer-jobs-SRCH_IL.0,11_IN178_KO12,44.htm)); Workwize AI Product Manager ([WTTJ](https://www.welcometothejungle.com/en/companies/workwize/jobs/ai-product-manager_amsterdam_f4swp4xd)); e KLM e Ahold Delhaize RPA ([Glassdoor](https://www.glassdoor.nl/Vacature/nederland-rpa-developer-vacatures-SRCH_IL.0,9_IN178_KO10,23.htm)). **Nenhuma vaga de Product Owner AI com PSPO foi verificada ativa nos Países Baixos.** NS e Brainbay estão encerradas ([freep.nl](https://www.freep.nl/opdracht/product-owner-ai)).

### Frequência de habilidades (contagens da amostra, não do mercado)

Na amostra de transformação/governança (N=36), os requisitos recorrentes não são técnicos. Eles mostram um perfil de **consultor sênior bilíngue que traduz regulação e adoção em prática**.

| Requisito | Vagas (N=36) |
|---|---|
| Neerlandês exigido explicitamente | 22 |
| Stakeholders seniores / aconselhamento executivo | 12 |
| Experiência prévia em consultoria | 12 |
| EU AI Act (M ou N) | 11 |
| Change management / adoção / comportamento | 11 |
| HBO/WO ou bacharel aceito | 11 |
| Stack Microsoft (Copilot, Power Platform, Azure, Fabric, DevOps) | 9 (Copilot citado em 5) |
| WO/Master explícito | 9 |
| GDPR/AVG/privacidade | 8 |
| Risco de IA / avaliação de impacto | 8 |
| Desenho de frameworks de governança de IA | 8 |
| Letramento em GenAI/LLM/RAG/agentic | 8 |
| Workshops / treinamento / AI literacy | 7 |
| Python / programação | 5 |
| Business case / roadmap / TOM | 5 |
| Business development / vendas | 5 |
| Experiência em setor regulado | 5 |
| Gestão de projetos de IA/TI | 4 |

Na amostra de automação/produto (24 registros, incluindo snippets), o mercado se divide em dois. As vagas de **emprego em RPA são UiPath-first**: UiPath em 5 anúncios, todos em neerlandês. A demanda **freelance e agentic é code-first ou low-code-agent**. Os números são: Python 8, UiPath 5, APIs de LLM (Claude/OpenAI/GPT) 4, Blue Prism 3, Power Automate 3, C#/.NET 3, Power BI 3, n8n 3, RAG 3, Automation Anywhere 2, LangChain 2, process mining 2, BPM 2, Agile/DevOps 2, GCP/AWS 2, e Copilot Studio 1 como requisito.

As faixas salariais publicadas (brutas mensais) mostram uma escada clara:

| Faixa | Vagas |
|---|---|
| Entry/junior | Talent&Pro €3.200–4.900; Loyens & Loeff a partir de €4.500; TADA €45–65 mil/ano |
| Mid / governança | Avans €3.826–5.699; KPMG €3.965–4.500; Add Value €4.000–6.500; accelerAite €4.750–5.750; KickstartAI até €5.100; Athora €5.082–6.776 |
| Senior | DICTU e ILT €4.818–7.094; Anderson MacGyver €5.000–7.500; MIVD €6.244–8.067 |
| Manager | Eraneos €6.238–8.154 (Mgr) e €7.677–10.166 (Sr Mgr) |
| Freelance | €40–60/h (A-020); fixo €500–1.000 (A-022). Referências fechadas: EZK €105/h; POOQ UiPath sênior €80–90/h ([POOQ](https://www.pooq.nl/opdrachten/senior-rpa-developer-uipath-hyperautomation)) |

### Certificações nomeadas literalmente nos anúncios

As certificações aparecem pouco e concentradas em governança. Nenhuma vaga ativa verificada nos Países Baixos cita **PSPO, PRINCE2, PMP, Prosci/ADKAR, UiPath ou OCEB**. Prosci aparece como obrigatório apenas num anúncio dos Emirados Árabes, fora do escopo ([Hirify](https://hirify.me/jobs/1070406-ai-change-management-consultant)). As certificações UiPath só aparecem em vagas de Hyderabad e Singapura ([jobstreet](https://sg.jobstreet.com/job/91460048)).

| Certificação literal | Vagas | Força | Fonte |
|---|---|---|---|
| IAPP AIGP | 2 | Preferencial (T-013); strong plus (T-017) | Deloitte; CGI |
| ISO 42001 como certificação | 1 | Strong plus (T-017) | CGI |
| ISO 42001 como framework | 4 | T-013 (M), T-015, T-019 (N), T-022 (N) | Deloitte, Everience, Avans, Deeploy |
| DAMA CDMP Practitioner / DCAM | 1 | **Obrigatória (pelo menos uma)** (T-017) | CGI |
| CIPP/E, CIPM, CIPT, "AI Governance", ISO 27701 LI | 1 | Já possuídas (T-014) | EY |
| RE / CISA / CISM / CIPP | 1 | M, ou em curso (T-018) | KPMG |
| CCLTE CAICO | 1 | Preferencial (T-013) | Deloitte |
| SAFe, TOGAF, DAMA, cloud, FinOps, TBM | 1 | Bônus (T-007) | Accenture |
| Microsoft PL-100 / PL-200 / PL-400 | 1 | Preferidas (A-005) | Itility |
| Genérico "relevante certificeringen" em RPA/IA | 1 | Ou intenção de obter (A-003) | PMT |

### O filtro de idioma reduz o mercado acessível a cerca de 10%

Nas 52 vagas ativas, **26 exigem neerlandês explicitamente**: 22 de 36 em transformação/governança e 4 de 16 em automação. **Apenas 4 aceitam inglês explicitamente**: Deeploy (T-022), Zanders (T-025), Loyens & Loeff (T-031) e The Automation Group (A-009). Uma quinta, Nanzen (A-010), aceita inglês por inferência. Das 21 sem requisito declarado, **17 são anúncios em neerlandês**, o que na prática sinaliza neerlandês. Restam 4 anúncios em inglês sem linha de idioma (Corbion, Everience, ABN AMRO, ING), a confirmar com o recrutador. Todas as Big4 e consultorias neerlandesas da amostra exigem neerlandês: Eraneos, Accenture, EY, Deloitte, KPMG, Atos, CGI, BearingPoint, PwC, Anderson MacGyver e Fellowmind. A CGI T-017 aceita apenas falantes nativos ou quase nativos, e a MIVD exige nacionalidade neerlandesa. A pesquisa genérica corrobora esse quadro sem desmenti-lo: o único número sólido é o do Indeed para 2024, cerca de **8% das vagas NL sem exigência de neerlandês**, concentradas em limpeza, hotelaria e logística ([IamExpat](https://www.iamexpat.nl/career/employment-news/indeed-speaking-dutch-often-not-required-jobs-netherlands)). A alegação de que o neerlandês seria "preferido em 60% das contratações tech" não tem fonte e foi descartada ([nlcompass](https://www.nlcompass.com/guides/expat-job-market-netherlands-2026)). A conclusão é direta: **sem neerlandês, o pool realista cai para cerca de 5–9 das 52 vagas**. Com B2/C1, ele se abre para a maior parte dos papéis mid e júnior.

A cobertura tem lacunas. Organizações internacionais de Den Haag (OPCW, ICC, EPO, ESA, Europol) não tinham vaga ativa encontrada, e a Europol aparece só num [PDF de fevereiro de 2026](https://www.europol.europa.eu/cms/sites/default/files/documents/VacanciesStatus20260213.pdf). Também não foram encontradas vagas em universidades de pesquisa nem em energia in-house (Eneco, Vattenfall, Alliander, salvo o process mining, e TenneT). Indeed, Glassdoor e Werken voor Nederland renderizam via JavaScript e não puderam ser enumerados.

---

## 3. Certificações: só o AIGP tem tração de mercado; o resto é opcional ou adiado

### O que é oficialmente vigente em 17/10/2026

O plano do rascunho do usuário (CERT-01 a CERT-08) usa nomes que, em sua maioria, existem, com quatro correções. **A UiPath tem agora três credenciais agentic**: Associate (AAA), Professional (AAP) e a nova **Agentic Automation Builder Professional**, lançada em 22/09/2026 ([UiPath Certification](https://www.uipath.com/learning/certification); [UiPath Academy](https://academy.uipath.com/certifications)). As antigas UiRPA/UiARD **expiram em 15/10/2026**. **O AIGP roda sob o BoK v2.1** desde 02/02/2026, que substitui o v2.0.1 e nomeia o EU AI Act ([AIGP BoK v2.1](https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt0d33152fd20bc134/AIGP_Cert%20BOK.pdf)). **O OCEB 2 virou "BPM Certifications" na OMG**, mas o exame Fundamental continua ativo ([OMG](https://www.omg.org/certification/bpm/)). **O PRINCE2 agora se chama "PRINCE2 Project Management (Version 7)"** ([PeopleCert Foundation v7](https://www.peoplecert.org/browse-certifications/project-programme-and-portfolio-management/PRINCE2-2/PRINCE2-7-foundation-3579)). O PSPO-AI Essentials existe e tem avaliação, mas **só para alunos da turma oficial** ([Scrum.org](https://www.scrum.org/professional-scrum-product-ownertm-ai-essentials-certification)).

### Fatos oficiais por credencial

| Credencial | Preço (moeda original) | Formato | Pré-requisitos / regra | Status G0 |
|---|---|---|---|---|
| Scrum.org PSPO I | US$200 por tentativa | 80 questões, 60 min, 85% | Curso opcional; senha válida para uma tentativa ([Scrum.org, extrato de busca](https://www.scrum.org/assessments/professional-scrum-product-owner-i-certification)) | **PENDING_OFFICIAL_VERIFICATION**: o fetch deu 403, e tipos de questão, proctoring e validade estão em conflito em fontes de terceiros ([cprime](https://cprime.com/learning/certifications/professional-scrum-product-owner-i); [open-exam-prep](https://open-exam-prep.com/study-guides/pspo-i/introduction/exam-facts)) |
| PSPO-AI Essentials | Turma definida pelo trainer; exemplo de EUR 595 sem 21% de IVA ([listagem](https://www.scrum.org/courses/professional-scrum-product-owner-ai-essentials-2026-07-29-99049)) | 20 questões, 30 min, 85% | **Turma obrigatória** | PENDING (extrato de busca) |
| PSPO II | US$250 | 40 questões, 60 min, 85% | Curso não exigido; se PSPO I é pré-requisito, está PENDING ([Scrum.org](https://www.scrum.org/Assessments/Professional-Scrum-Product-Owner-Assessments/PSPO-II-Assessment)) | PENDING |
| UiPath Agentic Automation Associate (UiPath-AAAv1) | US$150 | 90 min, 70%; voltado a perfis técnicos e não técnicos | Sem pré-requisito; validade de 3 anos ([EDD AAA](https://start.uipath.com/rs/995-XLT-886/images/UiPath%20Agentic%20Automation%20Associate%20Exam%20Description%20v1.0.pdf?version=0)) | OK (o número de questões está PENDING) |
| UiPath Automation Developer Associate (ADAv1) | US$150 | 90 min, 70%; produto 2024.10+ | Sem pré-requisito; 3 anos ([EDD ADA](https://start.uipath.com/rs/995-XLT-886/images/UiPath%20Certified%20Professional%20-%20Automation%20Developer%20Associate%20Exam%20Description.pdf?version=5)) | OK |
| UiPath Agentic Automation Professional (AAPv1) | US$300 | 120 min, 70%; Pearson VUE/OnVUE | Inclui AI Trust Layer e Coded Agents ([EDD AAP](https://start.uipath.com/rs/995-XLT-886/images/UiPath%20Agentic%20Automation%20Professional%20Exam%20Description.pdf)) | OK |
| UiPath Agentic Automation Builder Professional (AABPv1) | EDD diz US$150, FAQ diz US$300 para Professional | 120 min, 70% | Perfil MQC: **6+ meses construindo** em UiPath ([EDD AABP](https://start.uipath.com/rs/995-XLT-886/images/UiPath%20Agentic%20Automation%20Builder%20Professional%20Exam%20Description.pdf?version=0)) | **PENDING**: preço inconsistente; relação com AAP não esclarecida |
| Política UiPath (todas) | Taxa cheia por tentativa; espera de 2 semanas e depois de 1 mês; voucher vale 12 meses | Inglês e japonês | ([FAQ](https://www.uipath.com/learning/certification/faqs); [Policies](https://www.uipath.com/learning/certification/program-policies)) | OK |
| PRINCE2 v7 Foundation | US$701 (voucher + eBook); US$1.029; US$1.338 | 60 questões, 60 min, livro fechado, 60%; 14 idiomas, incluindo neerlandês e português (BR) | Renovação a cada 3 anos com 60 CPD ([PeopleCert](https://www.peoplecert.org/browse-certifications/project-programme-and-portfolio-management/PRINCE2-2/PRINCE2-7-foundation-3579)) | OK (EUR e retake Take2 PENDING) |
| PRINCE2 v7 Practitioner | US$778; US$1.235; US$1.544 (com retake grátis) | 56 questões/70 pontos, 150 min, livro aberto, 60% | Foundation v7, PMP, CAPM, IPMA A–D etc. ([PeopleCert](https://www.peoplecert.org/browse-certifications/project-programme-and-portfolio-management/PRINCE2-2/PRINCE2-7-practitioner-3581)) | OK |
| IAPP AIGP | **US$649 membro / US$799 não membro**; treinamento US$1.195; simulado US$60; associação US$295/ano | Múltipla escolha; escala 100–500, aprovação com 300; pausa no meio sem voltar à primeira metade; Pearson VUE/OnVUE; inglês | Treinamento opcional; prova em até 1 ano após a compra; CMF de US$250 na recertificação para não membros ([IAPP store](https://store.iapp.org/aigp-exam/); [Handbook](https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blteb8b5d531fd78971/IAPP-Certification_Handbook.pdf)) | OK. **PENDING**: total de questões e duração (terceiros falam em 100 questões e cerca de 2,75 h, [verifywise](https://verifywise.ai/ai-governance-library/standards-and-certifications/iapp-aigp-certification)), taxa de retake e horas de CPE |
| PECB ISO/IEC 42001 Lead Implementer | Preço definido pelo parceiro; exame incluído; 1 retake grátis em 12 meses | Curso de 5 dias, exame no dia 5; 31 CPD | **Passar no exame sem experiência dá só "Provisional Implementer"**. "Lead Implementer" exige 5 anos (2 em IA) + 300 h de AIMS; upgrade custa US$100 ([PECB LI](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001/iso-iec-42001-lead-implementer); [Manutenção](https://pecb.com/en/certification-maintenance-policy)) | **PENDING**: duração/questões/nota de corte (terceiros: 3 h, 80 questões, 70%, [digicomp](https://digicomp.ch/certification/security-certifications/pecb/isoiec-42001-lead-implementer)), valor da AMF e idiomas |
| PECB ISO/IEC 42001 Foundation | Parceiro | 2 dias; "Certificate Holder" | Sem pré-requisito ([PECB Foundation](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001/iso-iec-42001-foundation)) | PENDING (duração e corte) |
| Prosci Change Management Certification | **US$4.500 online / US$4.850 presencial** | 3–5 dias; knowledge checks e apresentação; credencial "Prosci Certified Change Practitioner" | **Treinamento obrigatório**; projeto próprio ([Prosci](https://www.prosci.com/solutions/training-programs/change-management-certification-program)) | PENDING: renovação; a página é inconsistente (assinatura de 1 ano vs. trial de 90 dias) |
| OMG BPM 2 Fundamental (ex-OCEB 2) | US$350 + impostos; 20% de desconto no retake | 90 questões, aprovação com 62 (69%); 90 min (120 min fora de países anglófonos) | Sem pré-requisito; 3 anos ([OMG PDF](https://www.omg.org/certification/bpm/BPM2-Fundamental.pdf)) | OK |

### Uma rota principal por domínio, reconciliada com o rascunho

A regra 4 do prompt pede uma rota por domínio e só adiciona opcionais diante de lacuna demonstrada ou exigência recorrente nas vagas. Cruzar as certificações com as 52 vagas ativas leva a uma conclusão clara: **o único exame pago com evidência de mercado é o AIGP**. O rascunho previa oito credenciais principais em sequência até jan/2028. Pela evidência de mercado, deveria ficar com **uma principal paga agora, duas baratas opcionais e o restante adiado** para depois da realocação, quando a função real estiver definida.

| Domínio | Rascunho do usuário | Rota recomendada | Evidência de mercado (52 vagas) | Decisão |
|---|---|---|---|---|
| AI Governance | AIGP | **AIGP (BoK v2.1)**, autoestudo com BoK e guia gratuitos | 2 citações nominais; EU AI Act em 11/36; governança em 8/36 | **PRINCIPAL – priorizar** |
| AI Automation/Agents | ADA → Agentic Automation Professional | **Agentic Automation Associate (AAA)** para o perfil de gestor. ADA → AAP só se o alvo for RPA developer, onde todas as vagas UiPath são em neerlandês. AABP exige 6+ meses construindo | 0 citações de certificação; UiPath como ferramenta em 5 vagas, todas em neerlandês. A justificativa do rascunho (DICTU) está **expirada (410)** | **OPCIONAL BARATO** (US$150); o mercado não sustenta AAP/ADA agora |
| Product Ownership | PSPO I; PSPO-AI; PSPO II | **PSPO I** (US$200), autoestudo | 0 citações verificadas. As vagas Boels/IVO Rechtspraak dos rascunhos são **USER_CLAIM, NOT_VERIFIED** | **OPCIONAL BARATO**; PSPO-AI e PSPO II **DEFER** |
| Project Management | PRINCE2 F → P | PRINCE2 v7 Foundation, só se uma vaga-alvo pedir | 0 citações; nem as vagas de projeto de IA (T-026, T-027) pedem. SLTN (IPMA-C/PRINCE2 Practitioner) é **USER_CLAIM, NOT_VERIFIED** | **DEFER**. US$701 + US$778 sem retorno demonstrado |
| AI Management Systems | PECB 42001 LI | Cobrir a 42001 via domínio II do AIGP + mapeamento de controles no portfólio; PECB depois de ter função com AIMS | 1 citação como certificação (CGI, só para nativos); 4 como framework | **DEFER**. O título LI completo é inalcançável sem 2 anos em IA e 300 h de AIMS |
| Change Management | Prosci | Vocabulário ADKAR aplicado num caso de portfólio | 0 citações nos Países Baixos (só no anúncio dos Emirados). A citação Capgemini dos rascunhos é **USER_CLAIM, NOT_VERIFIED** | **DEFER**. US$4.500+ e treinamento obrigatório não se justificam |
| Process Management | OCEB 2 só se as vagas justificarem | BPMN e process mining como evidência de portfólio | 0 citações. Process mining aparece em 2 vagas (Celonis) | **NÃO COMPRAR**. A própria regra do usuário dispara aqui |

O custo direto da rota enxuta é **US$799 (AIGP, não membro) + US$150 (AAA) + US$200 (PSPO I) = US$1.149**, contra cerca de **US$2.628** da rota "core" do rascunho (PSPO I + AAA + PRINCE2 F+P + AIGP), que ainda exclui PECB e Prosci. Os dois totais são somas dos preços oficiais citados na tabela acima. O mercado também nomeia credenciais **fora do plano do usuário**: DAMA CDMP (gate na CGI), CIPP/E e CIPM (EY), RE/CISA (KPMG) e PL-100/200/400 (Itility). Elas só entram se o candidato mirar especificamente governança de dados, privacidade em Big4, assurance ou Power Platform, e quase todas essas vagas exigem neerlandês. A UiPath recomenda ainda a **Automation Business Analyst Associate** para "Change/Transformation Managers" ([UiPath Academy](https://academy.uipath.com/certifications)). É uma alternativa à AAA a avaliar, com preço pela regra geral de Associate (US$150).

### Sobreposições: o que já está coberto

A maior redundância está entre **AIGP e ISO 42001**. O domínio II do BoK do AIGP cobre a NIST AI RMF e as "core ISO AI standards (22989, 42001…)", e o risco de IA reaparece nos domínios I–IV ([AIGP BoK v2.1](https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt0d33152fd20bc134/AIGP_Cert%20BOK.pdf)). O PECB acrescenta implementação de sistema de gestão, e não conhecimento regulatório. **PSPO e PRINCE2** cobrem papéis, valor e entrega por paradigmas opostos, e o PRINCE2 Agile ([PeopleCert](https://www.peoplecert.org/browse-certifications/project-programme-and-portfolio-management/PRINCE2-Agile-28/prince2-agile-practitioner-4076)) seria redundante com os dois. **Prosci e PRINCE2 v7** se sobrepõem só parcialmente, porque a v7 incluiu o "human element". **UiPath AAA e AIGP** são complementares, com sobreposição mínima via AI Trust Layer e evals. **PMP e IPMA** são alternativas ao PRINCE2, não complementos: escolhe-se uma (fees PMP e exame de jul/2026 = PENDING; pmi.org deu 403). Nenhum emissor publica cross-mapping oficial, então esta análise é inferência a partir dos syllabi.

### Implicações para os gates G0–G5

Nenhuma credencial está hoje além de NOT_STARTED. O **G0 OFFICIAL** está satisfeito para AIGP, UiPath AAA/ADA/AAP, PRINCE2 v7 e OMG BPM2. Fica **PENDING_OFFICIAL_VERIFICATION** para todo o Scrum.org (403), para os parâmetros de exame PECB e AMF, para a renovação Prosci, para o preço e o posicionamento do AABP, para a duração e o número de questões do AIGP e para todo o PMP. **G1 KNOWLEDGE** e **G3 MOCKS** dependem de diagnóstico por domínio. Para o AIGP, os pesos oficiais permitem um diagnóstico de 4 domínios: 16–20, 19–23, 21–25 e 21–25 questões. O simulado oficial custa US$60, e a meta interna de ≥85% em dois simulados não substitui o corte oficial de 300/500. **G2 PRACTICE** é onde o portfólio já ajuda. Os gates humanos e o registro de agentes cobrem parte de "Governing AI deployment" (AIGP IV), e o motor agentic cobre a maior parte do blueprint da AAA (discovery, blueprint de agente, escalonamentos, evals). **G4 ECONOMIC** está bloqueado: o orçamento é NOT_VERIFIED, e a evidência de mercado acima é o critério. **G5 AUTHORIZATION** exige ordem explícita do usuário. Sem ela, o estado máximo é READY_TO_BOOK. Recursos gratuitos permitem chegar a G1–G3 sem gasto: BoK, handbook e guia AIGP ([IAPP](https://iapp.org/certify/aigp)), trilhas e simulados gratuitos UiPath ([Academy](https://academy.uipath.com/certifications)), "Product Owner AI Open" ([Scrum.org](https://www.scrum.org/product-owner-ai-open)) e o blog "How to Pass PSPO I" ([Scrum.org](https://www.scrum.org/resources/blog/how-pass-pspo-i)).

---

## 4. Evidence Gap Report: L3 em agentic, L1 em governança e mudança

### Escopo e honestidade de autoria

Foram auditados apenas os clones locais de `programaex/design` (HEAD `6f6b66f1ca281c34ff2b3df91a7ffedcfa38ebe4`, 18 commits entre 15 e 16/10/2026) e `programaex/workbook` (HEAD `cffe5907c6511b2830010c7c9520ad32c6c5608d`, igual ao `main` remoto, 8 commits em 17/10/2026). Todos os outros repositórios estão **NOT_VERIFIED**, inclusive o `main` remoto do design (`fc45fce…`), ausente do clone, e as branches `claude/executar-app-mobile` e `claude/miniapps-pwa`. O histórico é curto, e **14 dos 18 commits do design são do agente "Claude"**, com 4 merges do owner. Há conteúdo com datas anteriores ao primeiro commit, por exemplo evals de 27/09/2026, o que indica importação em bloco. Isso não invalida a evidência, mas a narrativa de entrevista precisa ser explícita: **o candidato desenha, especifica, governa e revisa; o agente implementa**.

### Maturidade por família de vaga

| Família | Nível | Evidências principais (SHA do último commit no path) | O que falta para subir |
|---|---|---|---|
| Agentic AI / Automation | **L3** | EVD-D-001 `apps/workflow/` @ [`6851cd2`](https://github.com/programaex/design/blob/6851cd2264ff7270721ca5542daa5cab3350f7ef/apps/workflow/): Workers + Workflows + Durable Objects + R2 + MCP + OAuth, **64/64 testes**. A URL de deploy dá 404, então não há demo viva. EVD-D-005/006: 6 subagentes e fila WIP=1. EVD-D-007: eval de plugin **4/4 com vs 0/4 sem** (auto-relatada, NOT_RUN) | Demo pública viva, logs de execução, custo e taxa de sucesso por agente, reexecução da eval |
| Arquitetura / Cloud (transversal) | **L3** | EVD-D-001 e EVD-D-003; monorepo Turborepo; CI EVD-D-004 @ [`77c4de0`](https://github.com/programaex/design/blob/77c4de0ed236b1d3656bacfb754be0a71b06d216/.github/workflows/deploy-site.yml), que **pula silenciosamente sem secrets**. Execuções reais do Actions NOT_VERIFIED. O `deploy-workflow.yml` citado no README **não existe** | Evidência de runs de CI; diagrama C4 em inglês |
| Product & Value | **L2–L3** | EVD-D-003 `apps/site/` @ [`6f6b66f`](https://github.com/programaex/design/blob/6f6b66f1ca281c34ff2b3df91a7ffedcfa38ebe4/apps/site/): CMS com **15/15 + 17/17 testes**, Worker vivo `[subdominio-redigido].workers.dev` (302 → /login) e KPIs com regra, fonte e "N/D" honesto. EVD-D-013 Scroll Task (PRD → spec → wireframe → protótipo, L2). EVD-D-012 ADR/PRD (L1) | Discovery com usuários; métricas de adoção e outcome |
| Project & Process Mgmt | **L2** | Workflow de 8 fases com gates G01/G04/G06 (EVD-D-001); Gantt finish-to-start e DAG sem ciclo (EVD-D-003); cadeia AIKB-0001 de dependências, otimização e runbook (EVD-D-002 @ `6851cd2`); tripla clonagem (EVD-W-002) | Projeto entregue a terceiros; planejado vs. real |
| AI Management Systems | **L2** | EVD-W-002 `workbook.py` @ [`11e63fe`](https://github.com/programaex/workbook/blob/11e63fe51892f699f8b8c9690c3f7340688ce0fe/500_Copiloto_templates/scripts/workbook.py): **"check ok"**, checksums, completude. Skill de plano rastreável ancorada em ISO 9001/10005/10006/21502/31000/10075-2 (EVD-D-006) | AIMS ISO 42001 explícito; auditoria e indicadores de controle |
| AI Governance | **L1–L2** | Gates humanos antes de passos de agente; política "sem evidência = GAP"; registro de 6 agentes com fichas CV/schema (EVD-W-003, `draft`); ADR-001 VALIDATED (EVD-W-001 @ [`11e63fe`](https://github.com/programaex/workbook/blob/11e63fe51892f699f8b8c9690c3f7340688ce0fe/00_Workbook/registros/adr/ADR-001_arquitetura-unificada-workbooks.md)). **grep por "42001\|AI Act\|EU AI" = zero ocorrências relevantes** | Classificação de risco pelo EU AI Act, avaliação de impacto, mapeamento de controles ISO 42001, model cards, política de dados/PII |
| Change Management | **L1** | Apenas indireto: ADR do CMS com "entrypoint único" e ritual semanal CAPTURAR→…→APRENDER | Qualquer adoção por outras pessoas ou equipes; plano ADKAR com indicadores |
| Comunicação (transversal) | L1 | READMEs extensos, 4 artigos MDX, ADRs, **quase tudo em pt-BR** | Versões em inglês para o mercado NL |

### Bandeiras de privacidade e segurança

A bandeira crítica é a **credencial padrão hardcoded `DEFAULT_USER=[REDACTED]` / `DEFAULT_PASS=[REDACTED]`** em [`apps/site/worker/index.js` l.22–23 @ 6f6b66f](https://github.com/programaex/design/blob/6f6b66f1ca281c34ff2b3df91a7ffedcfa38ebe4/apps/site/worker/index.js), introduzida pelo commit `52c34d6` ("default login 000/003 while Worker secrets are not set"). O Worker `https://[subdominio-redigido].workers.dev` está vivo e redireciona para `/login`. **Se `CMS_USER`/`CMS_PASS` não estiverem setados, o site aceita esse login.** O login não foi testado. A ação é confirmar os secrets ou remover o fallback antes de compartilhar a URL, e só com autorização do usuário. Nenhum token ou chave real foi encontrado na árvore atual, mas o **histórico git não foi varrido**: recomenda-se gitleaks ou trufflehog antes de qualquer repo virar público, e a visibilidade atual dos repos é NOT_VERIFIED. As demais bandeiras são de redação, licença e permissão:

| Item | Classificação | Ação |
|---|---|---|
| Nome pessoal "[NOME REDIGIDO]" como owner de gates (README, workflow.json, taxonomy.ts, ai-registry, clp-orchestrator.md…) | REDACT | Substituir por papel |
| IDs de KV em `wrangler.jsonc`; subdomínio `[subdominio-redigido].workers.dev` derivado do e-mail | REDACT (baixo risco) | Decidir exposição |
| API do workflow pública por padrão sem `API_TOKEN` | SECURITY | Exigir token em produção |
| `plugins/agent-handoff/` (MIT, WillowRyu) e skills Apache-2.0 da Anthropic em `executar-cop` | PUBLIC com atribuição | **Nunca apresentar como autoria própria** |
| Capturas de páginas da Apple (`EXECUTAR_Claude_Design/referencias/*.png`) | PRIVATE | Não publicar; declarar reprodução estrutural |
| CSVs AlsoAsked (`apps/site/content/ops/`) | NEEDS_PERMISSION | Conferir os termos |
| `_sources/SRC-DOC-001..003` (PDF/DOCX de negócio) | NEEDS_PERMISSION/REVIEW | Não publicar sem revisão |
| `react-router-starter-template.hub-executar.workers.dev` atrás de Cloudflare Access | Sinal positivo | Código fora destes repos: NOT_VERIFIED |

### Clean Sea, Frankswaching e Risco Cognitivo

**Clean Sea e Frankswaching são GAP/NOT_VERIFIED**: zero ocorrências nos dois repositórios, então nenhuma linha de CV pode citá-los sem outra fonte. "Risco Cognitivo" existe como design system, UI kit com placeholders "Em construção" e 4 artigos MDX (L1–L2). O agente `blog-publisher` aponta para `apps/blog`, que não existe neste repo. Os ativos se classificam assim. **Production-ish**: Worker CMS `design` (vivo, sem uso medido). **Prototype**: `apps/workflow`, Scroll Task, cadeia AIKB-0001, design system. **Concept**: ADRs, PRD de Ops, workbooks A01–A15.

---

## 5. Emprego e realocação: sem visto, mas com relógio de 4 meses e 27%

**Autorização e registro.** Cidadãos UE/EEE não precisam de permissão para trabalhar como empregados nem como autônomos ([business.gov.nl](https://business.gov.nl/starting-your-business/registering-your-business/registration-at-the-netherlands-chamber-of-commerce-for-eu-self-employed-professionals)). Quem fica mais de 4 meses deve se registrar na **BRP** do município, o que gera o **BSN** necessário para trabalhar, abrir conta e contratar seguro ([The Hague International Centre](https://www.thehagueinternationalcentre.nl/municipal-registration); [I amsterdam](https://www.iamsterdam.com/en/living/take-care-of-official-matters/eu-citizens)). O prazo de "5 dias após a chegada" vem só de fonte secundária e está NOT_VERIFIED ([DutchReview](https://dutchreview.com/culture/living-in-the-netherlands/registration-netherlands/)). O **RNI** dá BSN a não residentes ou a estadias de até 4 meses. Desde 01/01/2026, o balcão RNI de Den Haag atende só passaportes europeus, o que inclui o candidato ([Gemeente Den Haag](https://www.denhaag.nl/en/moving-and-immigration/bsn-and-registration-for-non-residents-of-the-netherlands-rni/)). Isso permite obter um BSN antes da mudança. **O endereço é o caminho crítico**: sem endereço não há BRP. O aluguel médio novo no mercado livre foi de **€20,94/m², cerca de €1.882/mês, no 2º tri de 2026** ([Pararius](https://www.pararius.com/news/rent-rise-in-the-dutch-unregulated-sector-leveling-off-slightly)), e Amsterdam marcou €28,68/m² no 4º tri de 2025 ([Pararius](https://www.pararius.com/news/dutch-rental-prices-outpace-house-prices)). Os dados NVM do 2º tri de 2026 estão em [NVM](https://www.nvm.nl/media/2hsi0enf/20260730-analyse-nvm-vgmnl-huurontwikkelingen-q2-2026-def.pdf).

**Seguro-saúde.** O seguro básico neerlandês é obrigatório **até 4 meses após a chegada**, mesmo para quem tem apólice estrangeira. Não há cobertura retroativa além desse prazo, e o CAK pode multar ([government.nl](https://www.government.nl/documents/question-and-answer/health-insurance/when-do-i-need-to-take-out-health-insurance-if-i-come-to-live-in-the-netherlands); [Zorgverzekeringslijn](https://zorgverzekeringslijn.nl/english/)). Para chegada em 30/04/2027, o prazo cai por volta de 30/08/2027. As fontes divergem sobre o início da cobertura: chegada, registro ou primeiro dia de trabalho ([I amsterdam](https://www.iamsterdam.com/en/live-work-study/living/healthcare-insurance/health-insurance-in-the-netherlands); [Nyenrode](https://www.nyenrode.nl/en/about-us/about-nyenrode/internationals/scholars/insurance)), então o ponto está NOT_VERIFIED.

**ZZP/KvK/DBA.** O registro na KvK exige BSN, DigiD e endereço neerlandês (residencial ou comercial com consentimento) ([business.gov.nl](https://business.gov.nl/starting-your-business/registering-your-business/registering-with-the-kvk/)). A taxa de €85,15 e o limite KOR de €20.000 vêm só de fonte secundária (NOT_VERIFIED, [inburgering.org](https://inburgering.org/guides/zzp-freelance-netherlands-guide)). **Desde 01/01/2025 a Belastingdienst fiscaliza a falsa autonomia** e pode cobrar impostos retroativos ([Accountant.nl](https://www.accountant.nl/achtergrond/2024/12/wet-dba-opheffing-van-het-handhavingsmoratorium-en-de-rol-van-de-accountant/); [Randstad](https://www.randstad.nl/werkgevers/acties/wet-dba)). Em 2026 não há multas padrão, e a primeira etapa é uma visita ([Knab](https://bieb.knab.nl/ondernemen/handhaving-wet-dba-dit-betekent-het-voor-jou)). A Freelance.nl sugere o contrário ([Freelance.nl](https://www.freelance.nl/community/wet-dba-2025)), e para 2027 o quadro está NOT_VERIFIED. A **Wet VBAR** (presunção de emprego abaixo de cerca de €38/h) atrasou e provavelmente não está em vigor ([PwC](https://www.pwc.nl/nl/actueel-en-publicaties/belastingnieuws/loonbelasting-en-sociale-verzekeringen/wetvbarnaartweedekamer.html); [Brightmine](https://www.brightmine.com/nl/?p=24726); [carta do governo](https://www.staten-generaal.nl/eu/behandeling/20251104/brief_regering_voortgang/document3/f=/vmscgzgx03s7.pdf)). Na prática, clientes corporativos oferecem rotas "DBA-proof" via intermediário ou payroll ([Randstad](https://www.randstad.nl/werkgevers/wet-en-regelgeving/zzp/wet-dba/oplossingen)). Por isso o freelance corporativo é mais difícil que o freelance para PMEs.

**Trabalho remoto antes da mudança.** Quem trabalha 25% ou mais do tempo no país de residência tende a ficar na seguridade social desse país. O acordo-quadro permite ficar abaixo de 50% com **A1 pedido à SVB antes do início** ([SVB](https://svb.nl/en/id/you-work-in-2-or-more-countries/cross-border-teleworking); [SVB A1](https://svb.nl/en/id/you-are-an-employer/what-is-an-a1-certificate-of-coverage); [Declercq](https://www.declercq.com/en/blogs/issues-to-consider-when-working-remotely-from-abroad-part-3/); [grenzinfo](https://grenzinfo.eu/en/apply-for-a1-certificate-on-time/)). **Um início 100% remoto antes de 30/04/2027 exige payroll local, EOR ou adiamento da data de início.** O EOR não foi verificado em fonte.

**Regra dos 30% → 27%.** As condições oficiais são: morar a mais de 150 km da fronteira por mais de 16 dos 24 meses anteriores; norma salarial de **€48.013 em 2026** (€36.497 para menores de 30 com mestrado); teto de €78.600 isentos; até 5 anos; e o empregador **não é obrigado** a conceder ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/individuals/living_and_working/working_in_another_country_temporarily/you_are_coming_to_work_in_the_netherlands/30_facility_for_incoming_employees/)). **A partir de 01/01/2027 a taxa cai para 27% em casos novos**, com normas de €50.436 e €38.338 a preço de 2024, a indexar ([EY](https://www.ey.com/nl_nl/technical/tax/tax-updates/wijzigingen-30-procent-regelingen-definitief); [Loyens & Loeff](https://www.loyensloeff.com/nl/insights/news--events/news/van-30-regeling-naar-een-27-regeling-versoepeling-of-versobering/); [Meijburg](https://www.meijburg.nl/sites/default/files/2024-10/Wijzigingen%2030%25%20regeling%20okt%202024.pdf); [Grant Thornton](https://www.grantthornton.nl/insights/themas/prinsjesdag/2026/belastingplan-2027-wat-betekent-dit/)). Há divergência sobre quem começou entre 2024 e 2026 ([Rendement](https://www.rendement.nl/expatregeling/infographics/30-regeling-wordt-27-regeling.html)), e as normas indexadas de 2027 estão NOT_VERIFIED. A implicação prática é que **papéis júnior e ponte, com salário anual de €38–60 mil, podem não atingir a norma**: Talent&Pro €3.200–4.900/mês, Loyens & Loeff a partir de €4.500. Já os papéis sênior a atingem.

**Idioma e salários.** Fora da amostra, os guias salariais 2026 de Robert Walters e SGI estão atrás de cadastro e não forneceram números ([Robert Walters](https://www.robertwalters.nl/en/our-services/Salary-survey-direct-access-robert-walters.html); [SGI](https://www.sourcegroupinternational.com/source-reports/2026-netherlands-technology-salary-guide/)). Agregadores dão uma mediana de cerca de €62,9 mil para AI engineer ([ChoppingBlock](https://www.choppingblock.ai/salaries/ai-engineer-salary-in-netherlands)), com baixa confiança. Recrutadores dizem que papéis técnicos em empresas internacionais rodam em inglês ([SGI](https://www.sourcegroupinternational.com/technology-jobs-in-netherlands/); [JobRise](https://jobrise.io/en/blog/english-speaking-netherlands-jobs-2026/)), mas a amostra mostra que **governança, consultoria e setor público são neerlandês-first**.

**EU AI Act e Digital Omnibus.** O Regulamento (UE) 2026/1744 entrou em vigor em **27/07/2026**. As obrigações de alto risco do Anexo III passaram de 02/08/2026 para **02/12/2027**, e as do Anexo I para **02/08/2028**. A transparência do Art. 50 vale desde 02/08/2026, a marcação de conteúdo sintético de sistemas legados vale até 02/12/2026, e os sandboxes nacionais são devidos até 02/08/2027 ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo); [Cuatrecasas](https://www.cuatrecasas.com/en/spain/intellectual-property/art/digital-omnibus-ai-has-been-published); [FPF](https://fpf.org/wp-content/uploads/2026/07/FPF-EU-AI-Act-Timeline-2026-R2.pdf)). As proibições de deepfakes sexuais não consentidos começam em 02/12/2026 ([Abreu](https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/)), e o acordo político é de 07/05/2026 ([Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement); [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules)). O texto-base está em [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Nos Países Baixos, a Uitvoeringswet propõe um modelo híbrido: a **AP** como coordenadora e supervisora das práticas proibidas, a **RDI** para IA ligada a produtos e os reguladores setoriais (AFM, DNB) em seus domínios. A lei ainda não foi promulgada ([Stibbe](https://www.stibbe.com/nl/publications-and-insights/nederlands-voorstel-voor-ai-toezicht-hybride-samenwerking-tussen); [SecurityManagement](https://www.securitymanagement.nl/eu-ai-act-nederlandse-toezichthouders-ap-en-rdi-krijgen-sleutelrol/); [Rechtspraak](https://www.rechtspraak.nl/binaries/_rts_1784721574163/content/assets/rvdr/wa/2026/rvdr-wa-2026-uitvoeringswet-ai-verordening-jenv.pdf); [Kamerstuk 22112-4318](https://zoek.officielebekendmakingen.nl/kst-22112-4318.pdf)). A implicação é que a janela de candidatura de fev–mar/2027 cai **8–10 meses antes do prazo do Anexo III**, um bom momento para papéis de governança, ainda que provavelmente em neerlandês.

**Eventos.** O World Summit AI 2026 (7–8/10) já passou ([I amsterdam](https://www.iamsterdam.com/en/business/calendar/events/all/world-summit-ai-2026); [IamExpat](https://www.iamexpat.nl/lifestyle/events-festivals-netherlands/world-summit-ai-2026)). A Data Expo 2027 será em 15–16/09/2027, depois da viagem ([Luminik](https://www.luminik.io/events/data-expo-131b0d94e28c/), NOT_VERIFIED). O NL AI Congress foi em 14/04/2026 e não tem data para 2027 ([TU Delft](https://mondaioud.tudelftcampus.nl/event/the-dutch-ai-congress-2026/); [NL AIC](https://nlaic.com/en/agenda/nl-ai-congress-2024)). Os canais contínuos são [ProductTank AMS](https://producttankams.substack.com), [Mind the Product Amsterdam](https://mindtheproduct.com/amsterdam-pms-who-we-are-and-how-we-work) e [The Hague AI Meetup](https://www.meetup.com/the-hague-ai/). Esses calendários devem ser rechecados em jan/2027.

---

## 6. Faixas preliminares de aderência: bloqueios primeiro, sem probabilidades

**Premissa obrigatória.** As faixas abaixo **não são probabilidades de contratação**. Elas aplicam a regra do EPIC 08: se um MUST_HAVE bloqueante falha, a vaga é NOT_YET_ELIGIBLE, qualquer que seja o resto. Como **CV, LinkedIn, histórico de trabalho, anos de experiência, diploma e nível de neerlandês estão todos NOT_VERIFIED**, cada linha é condicional. As vagas ativas hoje servem de **arquétipos**: até a janela de 01/02/2027 a maioria terá expirado e precisará ser substituída e reverificada. Há também um conflito temporal: um início antes de 30/04/2027 implica trabalho remoto transfronteiriço (seção 5).

| Janela | Classe | Vagas-arquétipo | Bloqueios a verificar primeiro | Justificativa |
|---|---|---|---|---|
| **NOW** | APPLY (condicionado) | JOB-T-031 Loyens & Loeff Junior Innovation Advisor | Diploma de bacharel/mestre; data de início compatível | Inglês suficiente; sem anos exigidos; tarefas (pilotos, adoção, treinamento, requisitos) mapeiam direto para AI Transformation; €4.500+ |
| NOW | APPLY (condicionado) | JOB-A-009 The Automation Group Trainee Agentic AI | **5 anos de experiência de negócio** (NOT_VERIFIED) | Inglês ok; o portfólio próprio de agentes (EVD-D-001, L3) atende "own projects"; coortes trimestrais permitem mirar a coorte de 2027 |
| NOW | APPLY só se houver histórico comercial | JOB-T-022 Deeploy Partner Manager AI Governance | 3+ anos em parcerias ou vendas enterprise | Inglês ok; SaaS de governança de IA. Sem histórico de vendas fica NOT_YET_ELIGIBLE |
| NOW | NOT_YET_ELIGIBLE | JOB-T-023 MIVD; JOB-T-017 CGI; JOB-T-007 Accenture Junior; JOB-T-019 Avans (fecha 20/10, anúncio em neerlandês) | Nacionalidade; neerlandês nativo; Master e notas; neerlandês | Bloqueios duros |
| **30 dias** | BRIDGE | Anúncios corporativos em inglês: JOB-T-032 ING Agentic automation & AI Consultant; JOB-A-010 Nanzen AI/agents engineer | Confirmar o idioma com o recrutador; "proven experience" (ING); 2 anos + LLM em produção (Nanzen) | Exigem stack Copilot/Power Platform (ING), ausente do portfólio, e evals/produção (Nanzen). Com demo viva, eval reexecutada e caso em inglês, a candidatura fica defensável |
| 30 dias | BRIDGE | Freelance para PMEs: JOB-A-017 a A-023 (n8n, Claude/OpenAI, Copilot, Lindy) | Anúncios em neerlandês; KvK exige BSN e endereço; DBA | É o encaixe de entregável mais próximo do portfólio (L3 agentic). Taxas visíveis: €40–60/h ou fixo de €500–1.000. Antes da mudança, a viabilidade legal está NOT_VERIFIED |
| **60 dias** | BUILD_FIRST → APPLY | Governança mid: JOB-T-012 Athora (3 anos, WO), JOB-T-018 KPMG (3 anos de audit/risk) | Neerlandês (KPMG "harde eis"; Athora com anúncio em neerlandês); 3 anos em governança, risco ou auditoria | Exige o kit de governança (AI Act + 42001 + registro + avaliação de impacto) e a preparação AIGP em G1/G2. Sem neerlandês, continua NOT_YET_ELIGIBLE |
| 60 dias | BRIDGE | JOB-T-024 ABN AMRO; JOB-T-015 Everience (anúncios em inglês) | Experiência "significant" em consultoria; 8–12+ anos (Everience) | Provável NOT_YET_ELIGIBLE por anos. Vale contato de networking, não candidatura |
| **90 dias** | BUILD_FIRST | Mid de mudança e projetos de IA: JOB-T-004 accelerAite (3 anos + 2 em IA), JOB-T-026 Talent&Pro (2–4 anos em projetos de TI), JOB-T-027 KickstartAI (3 anos de PM em ML), JOB-T-028/029 BA júnior | Neerlandês (anúncios em neerlandês ou NL_REQ); anos de experiência | Ponte natural para Manager. Depende de neerlandês ≥B2 (fora do alcance em 90 dias, por inferência) e de um caso de mudança com indicadores |
| 90 dias | BUILD_FIRST | RPA developer: JOB-A-001/002 CareerValue (todos os níveis), A-003 PMT, A-004 ilionx | Neerlandês; HBO/WO; UiPath ou C# | Só se o candidato optar pela trilha técnica UiPath ADA. Todas as vagas UiPath são em neerlandês |
| **TARGET_LATER** | — | JOB-T-001 Eraneos, JOB-T-006 Accenture, JOB-T-010 BearingPoint, JOB-T-014 EY, JOB-T-016 Atos, JOB-T-011 Corbion, JOB-T-002/003 | 5–15 anos; consultoria; neerlandês | É o alvo AI Transformation Manager. Certificados não substituem anos nem projeto de adoção entregue |

A leitura de conjunto é que o caminho mais curto até "AI Transformation Manager" na amostra tem **três degraus**. O primeiro é um papel júnior de inovação/adoção (T-031) ou de BA/projeto de IA (T-026, T-028, T-029). O segundo é medior AI change ou governança (T-004, T-012, T-019). O terceiro é Manager (T-001), com 8+ anos e um projeto de adoção entregue. **O neerlandês é o maior fator de gate em todos os degraus**, e o freelance de governança/transformação não é rota de entrada: os casos vistos exigiam 3+ anos setoriais e fecharam em semanas.

---

## 7. Top 5 lacunas e ações da primeira semana (19–25/10/2026)

| # | GAP | Por que importa (evidência) | Artefato que prova | Prioridade |
|---|---|---|---|---|
| GAP-01 | Nível de neerlandês desconhecido | 26/52 exigem explicitamente e 17 anúncios são em neerlandês; CGI exige C1+, ILT C1, Capgemini Invent B2 | Teste de nivelamento CEFR + plano de estudo com marco A2/B1 até abr/2027 (inferência de viabilidade) | P0 |
| GAP-02 | Baseline profissional não verificado (anos, cargos, diploma, CV/LinkedIn) | Todo MUST_HAVE de MID+ é em anos (3–15); vários pedem WO/Master | CV-base em inglês com fatos, datas e fontes, classificados como FACT/USER_CLAIM | P0 |
| GAP-03 | Sem artefatos EU AI Act / ISO 42001 | AI Act em 11/36; governança em 8/36; grep = 0 ocorrências | AI inventory dos 6 agentes + classificação de risco pelo AI Act + avaliação de impacto + mapeamento de controles 42001, a partir do EVD-W-003 | P1 |
| GAP-04 | Nenhuma evidência L4 nem de adoção por terceiros | Change/adoção em 11/36; Eraneos exige ≥1 projeto de adoção de IA | Piloto com usuário real (com autorização) e métricas de adoção; até lá, rotular CONCEPT/PROTOTYPE | P1 |
| GAP-05 | Portfólio público não seguro e não em inglês; stack Microsoft ausente | Fallback 000/003 num Worker vivo; docs em pt-BR; terceiros sem distinção de autoria; Microsoft em 9/36 (Copilot em 5) | Repo saneado (sem fallback, histórico varrido, atribuições), caso âncora em inglês e, se o alvo for ING/consultorias Microsoft, um lab Copilot Studio/Power Automate | P0 (segurança) / P2 (Microsoft) |

**Plano da primeira semana.** A hipótese do prompt é 40/20/30/10 até 18/11, o que dá **16 h de estudo, 8 h de simulados, 12 h de build e 4 h de portfólio público**, num total de 40 h. Todas as ações externas (alterar repos, publicar, candidatar, pagar, contatar) dependem de autorização específica do usuário.

| Dia | Ação | Classe / horas | Critério de pronto |
|---|---|---|---|
| Seg 19/10 | Capturar o baseline: CV, LinkedIn, histórico com anos por função, diploma e equivalência HBO/WO, certificações existentes, orçamento e cidades. Marcar cada item como FACT/USER_CLAIM/NOT_VERIFIED | Público, 2 h | Tabela de baseline sem campo vazio sem rótulo |
| Seg 19/10 | Decidir sobre a Avans (fecha 20/10): a recomendação é **não aplicar** (anúncio em neerlandês, contrato de 1 ano, início incompatível com a mudança) e registrar a decisão | Público, 0,5 h | Registrado no DECISION_LOG |
| Seg–Ter | Segurança: com autorização, verificar se `CMS_USER/CMS_PASS` estão setados e propor um PR removendo o fallback; rodar gitleaks/trufflehog no histórico dos dois repos; decidir a redação de "[NOME REDIGIDO]" | Build, 4 h | Fallback removido ou secret confirmado; relatório do scanner |
| Ter–Qui | AIGP: baixar o BoK v2.1, o handbook e pedir o guia gratuito; diagnóstico por domínio (I–IV) com mapa de lacunas P0 | Estudo 10 h + simulados 4 h | Diagnóstico G1 com pontuação por domínio |
| Ter–Sex | Neerlandês: teste de nivelamento e escolha de curso. Opções de curso NOT_VERIFIED, pesquisar | Estudo, 4 h | Nível CEFR registrado; plano semanal |
| Qua–Sex | Kit de governança v0 sobre EVD-W-003: inventário dos 6 agentes, aplicabilidade do AI Act (avaliada, não presumida) e esqueleto de controles 42001 | Build, 6 h | Arquivo versionado com fontes e GAPs |
| Qui | UiPath AAA: trilha gratuita "Agentic Automation Training" + simulado gratuito, como diagnóstico, sem compra | Estudo 2 h + simulados 2 h | Pontuação do simulado registrada |
| Sex | Reverificar USER_CLAIM dos rascunhos: SLTN (PRINCE2/IPMA), Boels e IVO Rechtspraak (PSPO), Capgemini (Prosci), KPMG Sr Manager Technology Transformation, EUR PO AI Tooling, Capgemini Senior PO Agentic AI, Capgemini Manager IPA; e Scrum.org e pmi.org por outra via | Simulados/pesquisa, 2 h | Status VERIFIED_ACTIVE/EXPIRED para cada uma |
| Sex | Montar o JOB_PIPELINE com as 52 vagas, com prazos (DICTU 31/12, Alliander 30/11) e alertas em Freep, GreenPepper e Freelancer.nl | Build, 2 h | Pipeline com JOB_ID, status e próxima ação |
| Sáb–Dom | One-pager em inglês do caso âncora EVD-D-001 (Problem → Decision → Delivery → Evidence), com a narrativa de autoria assistida por IA | Público, 1,5 h | Rascunho revisado, não publicado |

---

## 8. Source & Assumption Ledger

| Fonte (nota) | Data | Estado | Confiança | Observação |
|---|---|---|---|---|
| Vagas de transformação/governança | 17/10/2026 | 36 VERIFIED_ACTIVE; 12 EXPIRED/ARCHIVED/fora de escopo; 4 UNVERIFIED | Alta para status; média para requisitos (paráfrases) | Peso no LinkedIn; PwC 021 incompleta; Younicorp sem data |
| Vagas de automação/produto | 17/10/2026 | 16 VERIFIED_ACTIVE (texto lista 8 freelance; A-024 possivelmente stale); 1 CONFLICT; 7 UNVERIFIED; 7 excluídas | Média | LinkedIn, Indeed e Glassdoor bloqueados; Alliander só via agregador |
| Certificações oficiais | 17/10/2026 | Oficial: UiPath, PeopleCert, IAPP, PECB, Prosci, OMG, Open Group, IPMA. Extrato de busca: Scrum.org, pmi.org (403) | Alta (oficial) / média (extrato) | Preços em US$; EUR PENDING |
| Auditoria de repositórios | 17/10/2026 | Local, somente leitura; testes executados; GETs anônimos | Alta | Apenas 2 repos; `main` remoto do design e outras branches NOT_VERIFIED |
| Emprego e realocação | 17/10/2026 (dados até out/2026) | Mistura de fontes oficiais (Belastingdienst, government.nl, business.gov.nl, SVB) e secundárias | Média | Não é aconselhamento jurídico/fiscal |
| Rascunhos do usuário (linhas 336+ do input) | Anteriores a 17/10/2026 | **USER_CLAIM** | Baixa até reverificação | Várias vagas citadas estão expiradas (Booking, DICTU UiPath) |

**Hipóteses assumidas neste relatório:**

1. O candidato não tem neerlandês funcional até prova em contrário.
2. Os anos de experiência são desconhecidos, por isso nenhuma vaga MID+ é tratada como APPLY.
3. As vagas ativas são arquétipos e serão substituídas até fev/2027.
4. A hipótese de horas 40/20/30/10 do prompt vale até a revisão quinzenal.
5. A meta de A2/B1 em neerlandês até abr/2027 é inferência, não fato.

**Itens abertos de verificação**, em ordem de desbloqueio:

1. **Baseline:** CV, LinkedIn, anos, diploma, nível CEFR, certificações existentes e orçamento.
2. **Segurança:** estado dos secrets do Worker `design`, scanner de histórico e visibilidade dos repos.
3. **Scrum.org**, por fonte oficial direta: formato, proctoring e validade do PSPO I; URL do Product Owner Open; pré-requisito do PSPO II.
4. **AIGP:** número de questões, duração, taxa de retake e horas de CPE.
5. **PECB 42001:** parâmetros do exame, AMF e idiomas.
6. **UiPath:** preço do AABP e sua relação com o AAP; número de questões.
7. **Prosci:** renovação.
8. **PMI:** taxas e exame de jul/2026. **PRINCE2:** preços em EUR e Take2.
9. **USER_CLAIM:** as vagas dos rascunhos (SLTN, Boels, IVO, Capgemini Prosci/PO/IPA, KPMG, EUR).
10. **Status confirmado com o recrutador:** idioma de ING, ABN AMRO, Everience e Corbion.
11. **Bancos e scaleups não verificados:** ING, ABN AMRO, KLM, Ahold, Workwize, a.s.r.
12. **Organizações internacionais de Den Haag e universidades:** portais próprios.
13. **Regras legais e fiscais:** prazo da BRP (5 dias), passos do DigiD, taxa da KvK e KOR, DBA e VBAR em 2027, normas indexadas da regra de 27% em 2027 e transição 2024–2026, início do seguro-saúde, EOR e regra dos 183 dias.
14. **Lei e eventos:** status parlamentar da Uitvoeringswet AI; datas de 2027 do NL AIC, ProductTank e UiPath Community NL.
15. **Iniciativas não verificadas:** existência de Clean Sea, Frankswaching e `apps/blog` em outros repositórios.

---

## Conclusão

A pergunta original era quais certificados fazer para virar AI Transformation Manager. A evidência de 17/10/2026 a reformula: **o mercado neerlandês filtra por idioma e anos antes de olhar credenciais**, e as credenciais que ele nomeia (AIGP, CIPP/E, DAMA CDMP, RE/CISA) quase não coincidem com o plano de oito certificações do rascunho. A consequência econômica é que gastar cerca de US$1.149 numa rota enxuta, com AIGP no centro, rende mais que US$2.628 ou mais numa sequência que inclui PRINCE2, além de US$4.500+ em Prosci e um PECB cujo título pleno nem é alcançável. O dinheiro e as horas liberados deveriam ir para o neerlandês, que é o maior multiplicador de elegibilidade na amostra, e para transformar o portfólio L3 agentic em prova de governança e adoção.

O ativo mais subestimado é o próprio padrão de trabalho dos repositórios: gates humanos, "sem evidência = GAP", registro de agentes, ADRs e validador. É exatamente o que as vagas de governança pedem com outro vocabulário (EU AI Act, ISO 42001, avaliações de impacto), e o prazo do Anexo III em 02/12/2027 cria demanda justamente na janela de candidatura. O risco mais subestimado é o oposto: uma credencial padrão num site vivo e um histórico de commits dominado pelo agente podem destruir credibilidade numa vaga de governança, se não forem tratados antes da primeira URL compartilhada.

Nota de redação: cópia do relatório com credenciais, nome pessoal e subdomínio da conta redigidos (original fora do repositório).
