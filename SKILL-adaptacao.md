# SKILL — Adaptação de Questões para Alunos Atípicos (NEE/AEE)

## O que esta skill faz

Transforma questões regulares do QuestBank em versões acessíveis para alunos com necessidades
educacionais especiais (NEE/AEE): TEA, TDAH, dislexia, deficiência intelectual, entre outros.

A versão adaptada recebe o **mesmo ID com prefixo `A-`**:
- Regular `"000052"` → Adaptada `"A-000052"`

---

## ⛔ REGRAS CRÍTICAS — leia antes de escrever qualquer enunciado adaptado

### A — Nunca dar dicas nem respostas

**Esta é a regra mais importante de todas.**

O texto de contextualização de imagens, gráficos, diagramas e textos motivadores deve
**explicar o que o elemento representa**, mas **jamais** indicar qual é a resposta correta,
sugerir qual alternativa escolher ou dar qualquer dica de raciocínio.

| ✓ Permitido | ✗ Proibido |
|---|---|
| "O gráfico mostra o custo em centavos de diferentes fontes de energia." | "O gráfico mostra que a energia eólica tem custo baixo." |
| "A tabela apresenta a velocidade e o tempo de um objeto em movimento." | "Perceba na tabela que a velocidade diminui, então o objeto desacelera." |
| "O diagrama mostra dois blocos ligados por uma corda sobre uma superfície." | "Note que o bloco menor vai puxar o maior." |
| "A figura mostra o esquema de um circuito elétrico com resistores." | "O circuito tem resistores em série, então some as resistências." |

---

### B — JSON escaping obrigatório para LaTeX

Em strings JSON, toda `\` de LaTeX DEVE ser `\\`. Sem exceção.

| Quer escrever | Escreva no JSON |
|---|---|
| `\text{m}` | `\\text{m}` |
| `\times` | `\\times` |
| `\frac{a}{b}` | `\\frac{a}{b}` |
| `\,` | `\\,` |

**Prefira sempre HTML `<sup>`/`<sub>` a LaTeX para potências em prosa** — evita o escaping.

### C — `(BANCA - ANO)` sem negrito, sempre primeiro

Nunca: `<b>(ENEM - 2020)</b>`. Sempre: `(ENEM - 2020)` sem nenhuma tag de negrito.
O prefixo é **sempre o primeiro elemento** do enunciado adaptado.

### D — `[IMAGEM]` sempre depois de `(BANCA - ANO)`

Mesmo que a questão original comece com imagem, na versão adaptada:
`(BANCA - ANO)` → `[IMAGEM]` → texto de contextualização → enunciado → pergunta

---

## Regras obrigatórias de adaptação

### Regra 1 — Contextualizar TODOS os elementos visuais e motivadores

**Para cada elemento abaixo presente na questão regular, escreva um texto curto de
contextualização (1–2 frases) logo após logo após em baixo da referencia bibliografia (se houver) do marcador ou o trecho, explicando o que é —
sem revelar a resposta ou dar pistas de raciocínio.**

| Elemento | O que escrever |
|---|---|
| `[IMAGEM]` (foto, ilustração) | O que a imagem representa no contexto da questão |
| `[IMAGEM]` (gráfico) | Quais variáveis o gráfico relaciona e o que seus eixos mostram |
| `[IMAGEM]` (diagrama / esquema) | O que o diagrama representa (circuito, sistema, mecanismo, etc.) |
| `[IMAGEM]` (tabela visual) | O que a tabela organiza (quais colunas e linhas representam) |
| `<table>` (tabela de dados) | O que os dados da tabela representam |
| Texto motivador (trecho) | Uma frase resumindo o assunto do trecho, sem repetir o conteúdo |

**Exemplos corretos:**

```
[IMAGEM]
O gráfico acima mostra duas grandezas físicas: o custo (em centavos de real) no eixo
vertical e a quantidade de carbono liberado no eixo horizontal, para diferentes fontes
de energia.
```

```
[IMAGEM]
A figura representa um sistema com dois blocos conectados por uma corda sobre uma
superfície plana.
```

```
[IMAGEM]
O diagrama mostra um circuito elétrico com uma bateria e três resistores conectados.
```

```
[IMAGEM]
O gráfico apresenta a variação da posição de um objeto ao longo do tempo.
```

**Exemplos errados (dão pistas):**

```
[IMAGEM]
O gráfico mostra que a energia solar é a mais barata. ← PROIBIDO: revela dado da resposta
```

```
[IMAGEM]
A tabela indica que o objeto acelera, pois a velocidade aumenta. ← PROIBIDO: dá o raciocínio
```

---

### Regra 2 — Manter textos motivadores, figuras e imagens

- Textos motivadores (trechos de jornal, revista, livro, citação, charge) → **preservar integralmente**
  antes do enunciado simplificado, seguidos de contextualização de 1–2 frases.
- `[IMAGEM]` → preservar na estrutura correta (depois de `(BANCA - ANO)`), seguido de contextualização.
- Tabelas de dados `<table>` → preservar integralmente, seguidas de contextualização.

**Estrutura obrigatória:**

```
(BANCA - ANO)
[IMAGEM ou texto motivador]
[Contextualização: 1–2 frases sobre o que o elemento representa — sem revelar a resposta]
[Enunciado simplificado — máx. 3 frases]
**[Pergunta em negrito?]**
```

---

### Regra 3 — Enunciado curto (máx. 3 frases)

- Elimine contexto longo, dados históricos e informações periféricas.
- Mantenha apenas o essencial para entender o que está sendo pedido.
- Uma ideia por frase.

---

### Regra 4 — Pergunta direta e em negrito

- Em negrito obrigatório: `<b>...</b>` no HTML.
- Direta, sem negações duplas, sem subordinadas complexas.
- Prefira forma afirmativa.

---

### Regra 5 — Apenas 3 alternativas (objetivas)

- Exatamente **3 alternativas** (A, B, C).
- Uma é a resposta correta — nunca omita.
- Linguagem simples, sem pegadinhas, sem dupla negação, um aspecto por alternativa.
- `gabarito` = A, B ou C correspondente.

---

### Regra 6 — Questões discursivas

- Uma pergunta única e clara.
- Se houver cálculo, explicite os dados a usar.
- `alternativas: []`.

---

### Regra 7 — Campos idênticos à questão regular

`tipo` · `disciplina` · `topico` · `conteudo` · `assunto` · `banca` · `ano` · `dificuldade` ·
`imagens` · `usedInExams` · `resolucao_link` · `created_at`

---

### Regra 8 — Campos que mudam

| Campo | Mudança |
|---|---|
| `id` | Prefixo `A-`. Ex: `"A-000052"` |
| `enunciado` | Estrutura obrigatória com contextualização de elementos |
| `alternativas` | 3 itens (A, B, C) simplificados |
| `gabarito` | `"A"`, `"B"` ou `"C"` |

---

## Formato do enunciado adaptado (HTML)

```html
<!-- 1. Prefixo — SEMPRE PRIMEIRO, SEM NEGRITO -->
<p style="text-align:justify;">(BANCA - ANO)</p>

<!-- 2. Imagem / texto motivador — logo após o prefixo -->
<p>[IMAGEM]</p>

<!-- 3. Contextualização do elemento — obrigatória, sem dar a resposta -->
<p style="text-align:justify;">[1–2 frases explicando o que a imagem/gráfico/diagrama representa.]</p>

<!-- 4. Enunciado simplificado — máx. 3 frases -->
<p style="text-align:justify;">[Dado 1. Dado 2, se necessário.]</p>

<!-- 5. Pergunta em negrito — obrigatória -->
<p><b>[Pergunta direta em negrito?]</b></p>
```

---

## Exemplo completo

### Regular (ENEM 2020) — id `"000052"`

> O gráfico mostra o custo (em centavo de real) e a quantidade de carbono liberado por fonte.
>
> `[IMAGEM]`
>
> CAVALCANTE, R. O vilão virou herói. Superinteressante, jul. 2007.
>
> A energia obtida a partir do vento é
>
> A) mais cara que a nuclear e emite mais carbono.
> B) a segunda fonte mais cara e livre de carbono.
> C) mais cara que a solar e ambas livres de carbono.
> D) mais barata e emite muito carbono.
> E) a mais barata e livre de carbono. ✓

### Adaptada (HTML correto) — id `"A-000052"`

```html
<p style="text-align:justify;">(ENEM - 2020)</p>
<p>[IMAGEM]</p>
<p style="text-align:justify;">O gráfico acima relaciona o custo (em centavos de real) e
a quantidade de carbono liberado por diferentes fontes de energia.</p>
<p style="text-align:justify;">CAVALCANTE, R. O vilão virou herói. Superinteressante, jul. 2007.</p>
<p><b>Analisando o gráfico, o que podemos afirmar sobre a energia eólica (do vento)?</b></p>
```

> Observe: a contextualização explica **o que o gráfico mostra** (custo × carbono × fontes),
> mas **não menciona** qual fonte é mais cara nem dá qualquer pista sobre a resposta.

---

## Exemplo com tabela de dados

### Regular

> A tabela abaixo mostra a posição x (em metros) de um objeto em função do tempo t (em segundos).
>
> `<table>...</table>`
>
> Qual é a velocidade média do objeto?

### Adaptada

```html
<p style="text-align:justify;">(BANCA - ANO)</p>
<table>...</table>
<p style="text-align:justify;">A tabela acima organiza os valores de posição (em metros)
e tempo (em segundos) de um objeto em movimento.</p>
<p><b>Qual é a velocidade média do objeto?</b></p>
```

---

## Checklist antes de gerar cada versão adaptada

- [ ] `id` tem prefixo `A-`?
- [ ] `(BANCA - ANO)` é o **primeiro elemento** do enunciado, sem negrito?
- [ ] `[IMAGEM]` / tabela / texto motivador vem **depois** de `(BANCA - ANO)`?
- [ ] Cada `[IMAGEM]`, gráfico, diagrama, tabela ou texto motivador tem **contextualização de 1–2 frases**?
- [ ] A contextualização **não revela a resposta nem dá pistas de raciocínio**?
- [ ] Enunciado simplificado tem no máximo 3 frases?
- [ ] Pergunta em `<b>...</b>`?
- [ ] Exatamente 3 alternativas (A, B, C)?
- [ ] `gabarito` é A, B ou C e corresponde à resposta correta?
- [ ] Alternativas simples, sem pegadinhas, sem dupla negação?
- [ ] Potências usando `<sup>`/`<sub>` HTML, não LaTeX?
- [ ] Se usou LaTeX, toda `\` está como `\\` no JSON?
- [ ] `tipo`, `disciplina`, `topico`, `conteudo`, `assunto`, `banca`, `ano`, `dificuldade` idênticos ao regular?
