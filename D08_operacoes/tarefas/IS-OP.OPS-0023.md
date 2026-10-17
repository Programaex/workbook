---
id: IS-OP.OPS-0023
type: issue
parent: EP-OP.OPS-0003
project: null
owner: OP.OPS
co_owners: [TD.ENG]
areas: [D08, D12]
macroarea_id: A09
area: D08
title: "Confirmar o domínio riscocognitivo.org, o DNS e a hospedagem na Cloudflare"
status: backlog
assignees: [Programaex]
start_date: 2026-10-19
due_date: 2026-10-20
labels: [tipo:issue, owner:OP.OPS, co:TD.ENG, macro:A09]
aliases: [TSK-0004]
github_url: https://github.com/Programaex/workbook/issues/23
github_number: 0023
owner_path: D08_operacoes/tarefas/IS-OP.OPS-0023.md
workbook_path: 00_Workbook/anexos/C_registro-de-tarefas/IS-OP.OPS-0023.md
source_refs: [Programaex/design:docs/planos/executar-epic01-2026-10-a-2027-04/registro-tarefas-executar-epic01-2026-10-a-2027-04.csv]
created: 2026-10-17
updated: 2026-10-17
---
# Confirmar o domínio riscocognitivo.org, o DNS e a hospedagem na Cloudflare

## Descrição
**Frente:** Site riscocognitivo.org · **Prioridade:** Alta · **Tempo estimado:** 1,5h

**Agora:** Entrar no painel da Cloudflare e procurar o domínio riscocognitivo.org na lista de sites.

**Resultado esperado:** Domínio ativo apontando para o Worker do site, com HTTPS funcionando.

## Passos
- [ ] Verificar o registro do domínio
- [ ] Apontar o DNS para o Worker do site
- [ ] Testar o acesso por HTTPS

**Concluído quando:** O endereço https://riscocognitivo.org abrir com certificado válido.
**Evidência:** Print do navegador e da configuração de DNS.

## Lacunas
- Situação do registro do domínio (GAP-03)

## Critérios de aceite
- [ ] Concluído quando: O endereço https://riscocognitivo.org abrir com certificado válido.

## Vínculos
Project: GAP (número do Project pendente) · Pai: EP-OP.OPS-0003 · Filhos: — · Bloqueada por: — · Blocos de tarefas afetados (`WB-A##-M##-TSK`): WB-A09-M01-TSK
