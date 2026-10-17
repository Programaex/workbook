# 500_Copiloto_templates — Ecossistema EXECUTAR

Pacote de templates e schemas CSV para organizar workbooks com rastreabilidade por **área e owner**.
Gerado em 2026-10-17, exclusivamente a partir dos documentos fornecidos nesta conversa.

## Conteúdo

- **19 templates independentes**, extraídos das 11 seções do `Untitled 2.md` e de dois complementos editoriais (`CAPA.md`, `ID_AREA_TUTULO_OWNER.md`).
- Para cada template: `template.csv` (uma linha não preenchida, com metadados da área), `exemplo_origem.csv` (dados de exemplo ancorados no documento), `schema.csv` (dicionário de campos), `schema.json` (validação tipada) e `README.md`.
- `00_CONTROLE/MASTER_INDEX.csv`: índice canônico com caminho de todos os templates, áreas, owners sugeridos e origem.
- `00_CONTROLE/WORKBOOK_IMPORT_ORDER.csv`: ordem sugerida de importação dos CSVs em abas de workbook.
- `00_CONTROLE/CAMPOS_SCHEMA_GLOBAL.csv`: catálogo consolidado de todos os campos.
- `00_CONTROLE/AREAS.csv` / `OWNERS.csv` / `RELACOES.csv`: dimensões para organização relacional.
- `00_CONTROLE/MAPEAMENTO_ORIGEM.csv`: ligação com as seções de origem.
- `00_CONTROLE/INVENTARIO_LINHAS_ORIGEM.csv`: transcrição linha a linha dos blocos substantivos, com numeração para auditoria.
- `90_REFERENCIAS/`: cópias dos seis arquivos-fonte fornecidos, incluindo o mapa A4 das áreas.

## Layout

```text
500_Copiloto_templates/
├── 00_CONTROLE/
│   ├── MASTER_INDEX.csv
│   ├── AREAS.csv
│   ├── OWNERS.csv
│   ├── CAMPOS_SCHEMA_GLOBAL.csv
│   ├── WORKBOOK_IMPORT_ORDER.csv
│   ├── MAPEAMENTO_ORIGEM.csv
│   ├── INVENTARIO_LINHAS_ORIGEM.csv
│   ├── RELACOES.csv
│   └── CHECKSUMS.csv
├── areas/
│   └── D##_nome_area/
│       └── OWNER_papel_funcional/
│           └── TPL-###_nome_do_template/
│               ├── template.csv
│               ├── exemplo_origem.csv
│               ├── schema.csv
│               ├── schema.json
│               └── README.md
└── 90_REFERENCIAS/
```

## Uso no workbook

1. Identifique a área e o papel funcional em `00_CONTROLE/MASTER_INDEX.csv`.
2. Abra `template.csv` no Excel/Sheets/LibreOffice ou importe como tabela no seu sistema; a linha-padrão tem as colunas e metadados, mas **não é um registro preenchido**.
3. Consulte `exemplo_origem.csv` para valores de referência do documento — **não** para provar que um trabalho foi realizado.
4. Preencha `registro_id` com valor único e `owner_pessoa` com uma pessoa designada. Mantenha o mesmo `template_id` e `area_id`.
5. Valide tipos, obrigatoriedades e enumerações segundo `schema.csv`/`schema.json`; campos numéricos usam ponto decimal, bools usam `true`/`false`.
6. Para montar um workbook com múltiplas abas, use `WORKBOOK_IMPORT_ORDER.csv` e, para relacionar informações, `RELACOES.csv`.
7. Use `INVENTARIO_LINHAS_ORIGEM.csv` como auditoria quando necessário conferir se alguma instrução do briefing foi simplificada.

## Convenções

- Todos os CSVs usam **UTF-8 com BOM**, delimitador **vírgula** e cabeçalho na primeira linha.
- `area_id`: IDs D01–D16 mantidos exatamente conforme o catálogo-fonte. Atribuição de templates às áreas é uma **proposta de classificação**.
- `owner_papel`: papéis **sugeridos** pela estrutura do trabalho; o arquivo de origem não atribuiu pessoas reais. `owner_pessoa` permanece em branco.
- `status=referencia`: conteúdo extraído do briefing, **não** produção, teste, arquivo gerado ou aprovação.
- `status=rascunho`: registro novo não preenchido.
- `schema.json` requer `registro_id` preenchido em registros reais; por definição, o CSV `template.csv` vem vazio nesse campo.
- `TPL-005` desdobra os quatro lobos cerebrais em objetos independentes, pois a fonte os cita juntos. Isso não é uma alegação de que esses arquivos 3D existem.
- A câmera de 70 mm só é aplicável às variantes em perspectiva. O texto original aponta projeção ortográfica para a câmera principal.
- As referências visuais da Lidl e da imagem cerebral são citadas no briefing, mas **não foram disponibilizadas como imagens de referência específicas nos anexos** deste pedido.
- O mapa de áreas A4 é uma referência de **classificação de diretórios**, não uma referência estética do cérebro.
- `PDCPA` está preservado literalmente do anexo editorial; sua expansão e semântica não foram definidas nos documentos.

## Escopo e limites

Este ZIP contém **somente templates, schemas, exemplos e referências**, e não contém vídeo renderizado, cenas Blender, GIF, visualizador funcional ou workbook `.xlsx`. Os exemplos de entregáveis referem-se a **requisitos planejados** no briefing. Nenhum teste de renderização ou geração de modelos foi alegado.
