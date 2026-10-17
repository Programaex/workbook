---
id: FER-001
type: ficha_cv
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
# painel-gestao

**Painel SaaS admin de gestão dos épicos do Programa EXECUTAR**

| Descrição | Fatos |
|---|---|
| App `apps/gestao` (Worker Cloudflare `gestao`) com duas views — EPIC 01 riscocognitivo.org (EP-OP.OPS-0003, #3) e Emprego e realocação (EP-OP.OPS-0005, #5) — e folha de impressão A4 paisagem de uma página por view. KPIs com regra e drill-down, marcos, cronograma por frente/trilha com gates, próximos 14 dias, lacunas; a view EPIC 01 inclui o modelo Solo Campaign System. | **Versão / maturidade:** 0.1.0, não publicado (deploy pendente de secrets)<br>**Tecnologias / interfaces:** Cloudflare Workers + assets, React 18, esbuild, design system EXECUTAR, API REST do GitHub<br>**Acesso / preço:** login por usuário e senha (secrets do Worker) |

**Ação principal (CTA):** Imprimir PDF (uma página A4 paisagem por épico)

## Origem e histórico de versões
| Data/versão | Marco | Fonte |
|---|---|---|
| 2026-10-17 / 0.1.0 | Criação do app com snapshot do workbook (commit 532752a) e modelo do PDF Solo Campaign System | Programaex/design `apps/gestao/` |

## Integrações e dependências
- Snapshot dos clones `D08_operacoes/tarefas/*.md` + registro de tarefas do plano (`docs/planos/executar-epic01-2026-10-a-2027-04/`).
- GitHub `Programaex/workbook`: issue do épico e sub-issues (`/api/epicos/:n`, cache de 10 min, `GITHUB_TOKEN` opcional).
- `apps/site/lib/ops/pagefit.mjs` (SPEC-03, piso de 9 pt) e `packages/design-system`.

## Validações e aprovações
| Data | Validação | Por |
|---|---|---|
| 2026-10-17 | 18 testes automáticos (node --test 10, vitest 8); PDFs das 2 views com 1 página A4 paisagem e menor fonte 9 pt | Claude Code (verificação técnica; revisão do owner pendente) |

## Saídas e evidências
`out/gestao-epic01-<data>.pdf`, `out/gestao-emprego-<data>.pdf` (gerados por `npm run pdf -w apps/gestao`).

## Avaliações
| Autor | Data | Nota | Comentário |
|---|---|---|---|
| GAP | | | |

## Navegação
Rotas: `#/epic01`, `#/emprego` · Workbooks: `WB-A09` · Ficha schema: `FER-001_schema.md`

<!-- Ficha CV (TPL-022, ref. "Doctor's Profile"). 1 página; excesso → `<!-- page continuation -->`. -->
