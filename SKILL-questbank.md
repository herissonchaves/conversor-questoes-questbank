# SKILL — Formato QuestBank JSON (Modo Lite)

## Schema de cada questão

```json
{
  "id": "string",
  "enunciado": "string (HTML)",
  "tipo": "objetiva | discursiva",
  "disciplina": "string",
  "topico": "string",
  "conteudo": "string",
  "assunto": "string",
  "banca": "string",
  "ano": number,
  "dificuldade": "facil | medio | dificil",
  "gabarito": "string",
  "alternativas": [ { "letra": "A", "texto": "string (HTML)" }, ... ],
  "imagens": [],
  "resolucao_link": "string",
  "usedInExams": [],
  "created_at": "string ISO 8601"
}
```

---

## ⚠️ Regra de imagens — Modo Lite

**Imagens, figuras e gráficos NÃO são extraídos nem embutidos.**

Onde a questão original contiver uma imagem/figura/gráfico, insira **apenas** o marcador:

```html
<p>[IMAGEM]</p>
```

O usuário adicionará a imagem real manualmente no QuestBank após a importação.

Esta regra se aplica a:
- Gráficos de qualquer tipo (barra, linha, dispersão, etc.)
- Figuras geométricas ou físicas
- Fotografias
- Ilustrações
- Qualquer elemento visual não-textual

**Tabelas de dados** (linhas/colunas com texto e números) **devem ser preservadas** como `<table>` HTML — não são substituídas por `[IMAGEM]`.

---

## Regras de preenchimento

### `id`
- Regular: número com zero à esquerda, mínimo 5 dígitos. Ex: `"000052"`.
- Adaptada: prefixo `A-` + mesmo número. Ex: `"A-000052"`.

### `enunciado`
- HTML completo da questão.
- **A primeira linha do enunciado deve sempre ser `(BANCA - ANO)`**, em negrito, seguida do texto da questão.
  - Ex: `<span style="font-size: 0.875rem;"><b>(ENEM - 2020)</b> O uso de equipamentos elétricos...</span>`
  - Se a banca for `"Desconhecida"` ou o ano for `0`, omita o prefixo.
- Onde havia imagem/figura/gráfico: `<p>[IMAGEM]</p>`
- Tabelas de dados: `<table>...</table>`
- Fórmulas LaTeX inline: `$...$` — em bloco: `$$...$$`
- Referência bibliográfica: `<p>AUTOR. Título. Fonte, ano.</p>`

### `tipo`
- `"objetiva"` — tem alternativas A/B/C/D/E
- `"discursiva"` — questão aberta

### `disciplina`
`"Física"` | `"Química"` | `"Matemática"` | `"Biologia"` | `"Ciências"` | `"Geografia"` | `"História"` | `"Português"` | `"Inglês"`

### `topico`
Tópico amplo. Exemplos para Física: `"Mecânica"`, `"Termodinâmica"`, `"Óptica"`, `"Eletromagnetismo"`, `"Ondulatória"`, `"Física Moderna"`, `"Energia"`, `"Fluidos"`.

### `conteudo`
Conteúdo específico. Ex: `"Cinemática"`, `"Leis de Newton"`, `"Fontes de Energia"`, `"Calorimetria"`.

### `assunto`
Assunto pontual. Ex: `"MRU"`, `"Segunda Lei de Newton"`, `"Impactos Ambientais"`, `"Calor Sensível"`.

### `banca`
Ex: `"ENEM"`, `"FUVEST"`, `"UNICAMP"`, `"VUNESP"`, `"UERJ"`, `"ITA"`, `"IME"`.
Se não identificado: `"Desconhecida"`.

### `ano`
Inteiro. Se não identificado: `0`.

### `dificuldade`
- `"facil"` — uma etapa, sem cálculo complexo
- `"medio"` — mais de uma etapa ou conceito
- `"dificil"` — múltiplas etapas, integração de conceitos

### `gabarito`
- Objetiva: letra maiúscula. Ex: `"B"`.
- Discursiva: resumo da resposta ou `""`.

### `alternativas`
- Array de `{ "letra": "A", "texto": "..." }` com letras maiúsculas.
- HTML simples no texto.
- Discursiva: `[]`.

### `imagens` / `usedInExams`
Sempre `[]`.

### `resolucao_link`
`""` por padrão.

### `created_at`
Data/hora atual em ISO 8601. Ex: `"2026-04-11T14:25:04.112Z"`.

---

## Checklist

- [ ] `id` único e no formato correto?
- [ ] Imagens/figuras substituídas por `<p>[IMAGEM]</p>`?
- [ ] Tabelas de dados preservadas como `<table>`?
- [ ] `tipo` correto?
- [ ] `disciplina`, `topico`, `conteudo`, `assunto` preenchidos?
- [ ] `banca` e `ano` identificados ou pesquisados?
- [ ] `dificuldade` avaliada?
- [ ] `gabarito` correto?
- [ ] `alternativas` com letras maiúsculas?
- [ ] `imagens: []` e `usedInExams: []`?
- [ ] `created_at` em ISO 8601?
