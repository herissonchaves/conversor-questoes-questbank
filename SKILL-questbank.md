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
- **A primeira linha do enunciado deve sempre ser `(BANCA - ANO)`** (sem negrito), seguida do texto da questão.
  - Ex: `<p style="text-align:justify;">(ENEM - 2020) O uso de equipamentos elétricos...</p>`
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
Se não identificado após busca: `"Desconhecida"`. **Nunca inventar.**

### `ano`
Inteiro. Se não identificado após busca: `0`. **Nunca inventar.**

### `disciplina`, `topico`, `conteudo`, `assunto`, `dificuldade`
Preencher com base no conteúdo da questão.
Se não for possível determinar com certeza: deixar a string vazia `""`. **Nunca inventar.**

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

## Regras para preenchimento de metadados

Siga esta ordem para identificar cada metadado. Se não encontrar em nenhuma etapa,
**deixe em branco ou use o valor padrão** — nunca invente.

### Ordem de busca

1. **Texto do próprio documento** — leia o cabeçalho, rodapé e enunciados em busca de
   menções à banca, ano e disciplina.

2. **Busca na internet** — se não encontrado no documento, pesquise usando fragmentos
   do enunciado entre aspas. Use apenas sites confiáveis listados abaixo.

3. **Não encontrado** — deixe o valor padrão (`"Desconhecida"` / `0` / `""`).
   **Jamais invente ou suponha dados sem evidência.**

### Sites confiáveis para busca de metadados

Use preferencialmente os sites abaixo. Outros sites oficiais também são aceitos (domínios `.br`, `.gov.br`, `.edu.br` ou sites institucionais de universidades e bancas). **Nunca use fóruns, blogs ou sites de gabarito não oficiais como fonte de metadados.**

| O que buscar | Sites a consultar |
|---|---|
| Banca e ano de vestibulares estaduais | `vestibulares.brasilescola.uol.com.br` · `educacao.uol.com.br` · `guiadoestudante.abril.com.br` |
| Questões do ENEM | `enem.inep.gov.br` · `vestibulares.brasilescola.uol.com.br` |
| FUVEST | `fuvest.br` |
| UNICAMP | `comvest.unicamp.br` |
| VUNESP | `vunesp.com.br` |
| UEL | `uel.br` |
| UERJ | `vestibular.uerj.br` |
| UFRJ / FUVEST / USP | Site oficial da universidade (domínio `.br`) |
| ITA / IME | `ita.br` · `ime.eb.br` |
| FUVEST | `fuvest.br` |
| PUC-Rio | `puc-rio.br` |
| UEA | `uea.edu.br` |
| UFMS / UFPR / UFSM | Site oficial da universidade |
| FAMEMA | `famema.br` |
| FMJ | `fmj.br` |
| PUC-SP / PUC-MG | Site oficial |

> **Atenção:** não acesse fóruns, blogs, sites de gabarito não oficiais
> (como "colégio web", "descomplica", "me salva" etc.) como fonte primária de metadados.
> Esses sites podem conter erros de atribuição de banca e ano.

### O que fazer se não encontrar

| Campo | Valor quando não encontrado |
|---|---|
| `banca` | `"Desconhecida"` |
| `ano` | `0` |
| `disciplina` | `""` (string vazia) |
| `topico` | `""` |
| `conteudo` | `""` |
| `assunto` | `""` |
| `dificuldade` | `"medio"` (padrão conservador) |

---

## Checklist

- [ ] `id` único e no formato correto?
- [ ] Imagens/figuras substituídas por `<p>[IMAGEM]</p>`?
- [ ] Tabelas de dados preservadas como `<table>`?
- [ ] `tipo` correto?
- [ ] `disciplina`, `topico`, `conteudo`, `assunto` preenchidos?
- [ ] `banca` e `ano` identificados no texto ou pesquisados em site oficial?
- [ ] Se não encontrado, usou `"Desconhecida"` / `0` em vez de inventar?
- [ ] `dificuldade` avaliada?
- [ ] `gabarito` correto?
- [ ] `alternativas` com letras maiúsculas?
- [ ] `imagens: []` e `usedInExams: []`?
- [ ] `created_at` em ISO 8601?
