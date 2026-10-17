---
id: ADR-001
type: adr
title: Arquitetura Unificada de Workbooks do Ecossistema EXECUTAR
status: VALIDATED
version: 1.0
date: 2026-10-17
approved: 2026-10-17
approved_by: owner do repositório (aprovação registrada na sessão)
macroarea_id: A01
owner: MA.GOV
scope: Programaex/workbook
note: Homônimo dos ADR-001 do repo Programaex/design (escopos distintos; não substitui aqueles).
---
# ADR-001 — Arquitetura Unificada de Workbooks do Ecossistema EXECUTAR

Versão 1.0 · 17/10/2026 · Arquitetura documental e governança de dados · **Estado: VALIDATED**

## 1. Contexto e decisão arquitetural

O Ecossistema EXECUTAR necessita de uma arquitetura documental capaz de organizar estratégias, pesquisas, produtos, projetos, produção, operações e evidências em um sistema único de consulta, atualização, exportação e reutilização.

**Decisão:** o Workbook Geral será um agregador de múltiplos workbooks especializados, organizados por áreas funcionais, com schemas independentes, identificadores persistentes, referências cruzadas e um padrão visual comum.

A arquitetura deverá separar quatro responsabilidades:

- **Informação:** dados, conteúdo, pesquisas e evidências.
- **Estrutura:** áreas, workbooks, seções, fichas e schemas.
- **Apresentação:** páginas, componentes, estilos e regras de paginação.
- **Operação:** responsáveis, estados, tarefas, dependências e agentes.

O Workbook Geral não será um documento monolítico. Será uma composição de workbooks, permitindo exportar o ecossistema inteiro, uma área, um produto, um projeto ou um conjunto de fichas.

## 2. Estrutura universal de cada workbook

| Bloco | Seção | Páginas | Comportamento |
|---|---|---|---|
| 01 · Abertura | Capa | 1 | Fixa |
| 02 · Navegação | Index | 1 | Fixa por padrão, com tratamento de overflow |
| 03 · Síntese executiva | Overview Top-down | 3 | Fixo, síntese progressiva |
| 04 · Desenvolvimento | Conteúdo modular | Ilimitadas | Dinâmico, com quebra automática e continuidade |
| | Notas | 3 | Fixas por ciclo |
| | Tarefas estruturadas | 2 | Fixas por ciclo |

Repetir o ciclo (Conteúdo · Notas · Tarefas) por módulo, capítulo ou unidade de trabalho.

O bloco inicial possui cinco páginas antes do conteúdo. O ciclo de fechamento adiciona cinco páginas.

**Regra de integridade:** nenhuma informação deverá ser omitida para caber no layout. Em caso de excesso, serão criadas páginas de continuação identificadas. A paginação final será calculada depois da composição do conteúdo, sem alterar a identidade dos registros.

## 3. Taxonomia oficial das 15 áreas

| ID proposto | Área | Responsabilidade principal |
|---|---|---|
| A01 | Governança | IDs, READMEs, schemas, rotas, links, QR codes, índices, padrões e ADRs globais |
| A02 | Programa | Project Charter, síntese do ecossistema, estratégia, tática, operações, épicos e portfólio |
| A03 | Business | Business Plan, Lean Plan, PMF, SWOT, MOAT, PESTEL, modelos econômicos e frameworks |
| A04 | Ecossistema | Arquitetura das iniciativas, fichas, ADRs, READMEs, subáreas, produtos e relações |
| A05 | Pesquisa e Evidências | Artigos, fontes, dados brutos, insumos, pesquisas, métodos e evidências |
| A06 | Dados | Dados estruturados e consultáveis de SEO, palavras-chave, ICP, métricas e indicadores |
| A07 | Creator PEM | Matrizes multiplataforma, dependências, regras e schemas de planejamento |
| A08 | Editorial | Calendário, programação e cronogramas editoriais multiplataforma |
| A09 | Operações | Épicos, issues, tarefas, responsáveis, prioridades, dependências e acompanhamento |
| A10 | Produção | Fases de produção, entregáveis, controles e critérios de aprovação por página |
| A11 | Agentes | Fichas de agentes, skills, soluções, ferramentas, permissões e contratos |
| A12 | Produtos | Catálogo de e-books, skills, ferramentas, soluções, ofertas e demais produtos |
| A13 | Design | Mockups, wireframes, design tokens, componentes e Storybook |
| A14 | Templates | Templates raw, schemas reutilizáveis, versões e documentação |
| A15 | Comercial | Ofertas, vendas, CTAs, propostas, argumentos, funis e materiais comerciais |

Os IDs A01–A15 são provisórios até a reconciliação com o catálogo de identificadores já existente. Nenhum ID previamente utilizado deverá ser sobrescrito.

> **Reconciliação aplicada neste repositório (decisão do owner, 2026-10-17):** A01–A15 são **macroáreas** acima dos domínios D01–D16, que permanecem imutáveis. Cada artefato declara `macroarea_id` e `dominio_id`. Não há mapeamento global D→A; relações só entram em `relations.csv` com fonte comprovada.

## 4. Hierarquia lógica

```
WORKBOOK GERAL
│
├── GOVERNANÇA GLOBAL
│   ├── Identificadores
│   ├── Schemas e contratos
│   ├── Registro de rotas
│   └── Índices e referências
│
├── WORKBOOKS POR ÁREA (A01–A15)
│   │
│   ├── Subáreas
│   │   ├── Iniciativas / Projetos
│   │   │   ├── Produtos / Entregáveis
│   │   │   │   ├── Fichas
│   │   │   │   ├── Conteúdos
│   │   │   │   └── Evidências
│   │   │   └── Tarefas / Dependências
│   │   └── Schemas especializados
│   │
│   └── Páginas renderizadas
│       ├── Capa
│       ├── Index
│       ├── Overview
│       ├── Conteúdo
│       ├── Notas
│       └── Tarefas
│
└── REGISTROS TRANSVERSAIS
    ├── Produtos
    ├── Pessoas e Owners
    ├── Fontes de dados
    ├── Evidências
    ├── Rotas
    ├── ADRs
    └── Dependências
```

A hierarquia acima representa a navegação documental, não uma obrigação de armazenar cada entidade fisicamente em apenas uma pasta. Um produto pode aparecer nos workbooks de Ecossistema, Produtos, Comercial e Operações, mas deve possuir um único registro canônico, referenciado pelos demais.

## 5. Regras de arquitetura e responsabilidade

### ADR-001.1 — Separação entre Programa, Ecossistema e Produtos

Essas três áreas não devem duplicar suas informações.

| Área | Pergunta respondida | Registro principal |
|---|---|---|
| Programa | O que estamos tentando alcançar e como coordenamos a execução? | Objetivos, prioridades, roadmap e portfólio |
| Ecossistema | Como as iniciativas e soluções se relacionam? | Domínios, subáreas, aplicações, integrações e ADRs |
| Produtos | O que entregamos ou comercializamos? | Catálogo de produtos, versões e entregáveis |

Por exemplo, Risco Cognitivo, EXECUTAR App e Marketplace podem possuir estruturas diferentes, com seus próprios schemas, fichas e workbooks. As rotas servirão para confirmar essa classificação e suas relações.

### ADR-001.2 — Separação entre Pesquisa, Dados e Business

Pesquisa e Evidências preserva fontes, métodos e resultados originais. Dados transforma e organiza informações para consulta. Business interpreta essas informações para formular estratégias, hipóteses e decisões.

Uma mesma pesquisa poderá fundamentar uma análise de ICP, uma hipótese de Product-Market Fit e uma decisão comercial sem precisar ser copiada três vezes.

### ADR-001.3 — Separação entre Creator PEM, Editorial e Produção

- **Creator PEM:** define a matriz de distribuição, os formatos, canais e dependências.
- **Editorial:** determina o que será publicado, quando e em qual canal.
- **Produção:** registra como cada entregável será produzido, revisado e aprovado.

Cada fase de Produção terá uma ficha própria, renderizada em uma página por padrão. Quando o conteúdo ultrapassar essa capacidade, serão geradas páginas de continuação, preservando o requisito de não omitir dados.

### ADR-001.4 — Templates como fonte reutilizável

A área Templates utilizará `500_Copiloto_templates` como diretório canônico de modelos reutilizáveis. Ela armazenará modelos vazios, schemas, metadados, exemplos e versões, mas não deverá funcionar como depósito indiscriminado de registros operacionais preenchidos.

### ADR-001.5 — Fichas obrigatórias de entidades (decisão do owner, 2026-10-17)

Todo agente, skill, ferramenta e produto tem **duas fichas obrigatórias e complementares**: a **ficha CV** (perfil legível, estilo curriculum vitae; `TPL-022`) e a **ficha schema** (anatomia estruturada: gatilhos, armazenamentos, write policy, decisão de contexto, manutenção; `TPL-023`).

## 6. Contrato mínimo de metadados

Todo workbook, seção, ficha e registro deverá ter um identificador persistente e metadados suficientes para consulta e automação.

```yaml
schema_version: "1.0"
adr_id: "ADR-001"
workbook:
  id: null
  title: null
  area_id: null
  subarea_id: null
  owner_role: null
  owner_person: null
  status: "draft"
  version: "1.0"
  parent_workbook_id: null
  source_refs: []
  related_workbook_ids: []
  route_refs: []
  layout:
    cover_pages: 1
    index_pages: 1
    overview_pages: 3
    content_pages: "unlimited"
    notes_pages: 3
    tasks_pages: 2
    repeat_scope: "module"
  references:
    template_id: null
    schema_id: null
    adr_ids: []
    evidence_ids: []
  export:
    formats:
      - pdf
      - md
      - csv
    page_size: "A4"
    overflow_policy: "continuation"
```

Os campos null são obrigatórios para identificação de pendências, mas não autorizam a publicação definitiva sem validação. O formato A4 é a configuração inicial proposta para impressão.

## 7. Regras de aceitação

O ADR será considerado implementado quando:

- [ ] As 15 áreas estiverem cadastradas com IDs, owners e responsabilidades.
- [ ] Cada workbook puder ser criado a partir de um template validado.
- [ ] As fichas especializadas puderem coexistir com o layout universal.
- [ ] O índice geral permitir navegação entre áreas, subáreas, produtos e registros.
- [ ] As referências cruzadas não exigirem duplicação da fonte canônica.
- [ ] As exportações preservarem conteúdo, hierarquia e referências.
- [ ] As páginas de continuação forem criadas sem truncamento.
- [ ] Os agentes puderem consultar schemas e templates sem alterar os originais.
- [ ] Toda decisão arquitetural relevante tiver ADR e estado de aprovação.
- [ ] O registro de rotas puder associar páginas, aplicações, produtos e workbooks.

## 8. Consequências e decisões pendentes

**Consequências positivas:** maior padronização, reutilização de templates, rastreabilidade, exportação consistente e menor ambiguidade para agentes de IA.

**Custos e riscos:** manutenção de schemas, versionamento, validação de relações e necessidade de evitar que diferentes workbooks mantenham cópias divergentes dos mesmos dados.

**Pendentes:** a reconciliação dos IDs com o catálogo existente, a atribuição nominal dos owners, o mapeamento das rotas e a aprovação das regras de overflow para Index, Overview, Notas e Tarefas.

**Decisão final:** adotar o Workbook Geral como camada de composição e navegação, mantendo os workbooks especializados como unidades independentes, interoperáveis e governadas por schemas versionados.

**Próximo:** ADR-002 — Taxonomia de Domínios, Subáreas, Produtos e Rotas, sem modificar a arquitetura universal de paginação estabelecida aqui.
