# SKILL — Adaptação de Questões para Alunos Atípicos (NEE/AEE)

## O que esta skill faz

Transforma questões regulares do QuestBank em versões acessíveis para alunos com necessidades
educacionais especiais (NEE/AEE): TEA, TDAH, dislexia, deficiência intelectual, entre outros.

A versão adaptada recebe o **mesmo ID com prefixo `A-`**:
- Regular `"000052"` → Adaptada `"A-000052"`

---

## Regras obrigatórias de adaptação

Siga **todas** as regras abaixo, sem exceção.

---

### Regra 1 — Manter textos motivadores, figuras e imagens

- Sempre que houver **texto motivador** na questão regular (trecho de jornal, revista, livro,
  citação, poema, tabela de dados, charge), **mantenha-o na versão adaptada**.
- O texto motivador deve vir **antes do enunciado simplificado**, na mesma posição em que
  aparecia na questão original.
- Sempre que houver `[IMAGEM]` na questão regular, **preserve o marcador `[IMAGEM]` na mesma
  posição** na versão adaptada. Nunca remova nem descreva.
- Tabelas de dados (`<table>`) presentes na questão regular devem ser **preservadas integralmente**
  na versão adaptada.

**Estrutura esperada do enunciado adaptado quando há texto motivador:**

```
[texto motivador — preservado]
[IMAGEM, se houver]
[enunciado simplificado — máx. 3 frases]
[IMAGEM, se houver após o enunciado]
**[Pergunta direta em negrito?]**
```

---

### Regra 2 — Enunciado curto (máx. 3 frases)

- Elimine contexto textual longo, dados históricos e informações periféricas **que não sejam
  o texto motivador** e não sejam necessárias para responder.
- Mantenha apenas o que é **essencial** para entender o que está sendo pedido.
- Se houver `[IMAGEM]`, adicione uma frase curta de contextualização logo antes dela.
  Ex: *"O gráfico abaixo mostra o custo de diferentes fontes de energia."*
- Use frases curtas. **Uma ideia por frase.**

---

### Regra 3 — Pergunta direta e em negrito

- Reescreva a pergunta de forma **direta e objetiva**.
- A pergunta **obrigatoriamente deve estar em negrito** — use `<b>...</b>` no HTML.
- Evite negações duplas, subordinadas complexas e vocabulário técnico desnecessário.
- Prefira a forma afirmativa:
  - ✓ "O que podemos afirmar sobre X?"
  - ✗ "Qual das alternativas NÃO descreve corretamente X?"

---

### Regra 4 — Apenas 3 alternativas (questões objetivas)

- Reduza para exatamente **3 alternativas** (A, B, C).
- Uma delas **obrigatoriamente** é a resposta correta — nunca omita o gabarito.
- As alternativas incorretas devem ser **plausíveis mas claramente distinguíveis**, sem pegadinhas.
- Reescreva com linguagem simples, direta, sem dupla negação.
- Cada alternativa deve focar em **um único aspecto**.
- O campo `gabarito` da versão adaptada deve ser a nova letra (A, B ou C) correspondente
  à resposta correta.

---

### Regra 5 — Questões discursivas

- Transforme em uma pergunta única e clara.
- Se a questão original tiver múltiplos itens (a, b, c...), escolha o mais relevante ou
  unifique em uma única solicitação acessível.
- Se houver cálculo, deixe explícito quais dados o aluno deve usar.
- `alternativas: []`.

---

### Regra 6 — Campos idênticos à questão regular

Estes campos devem ser **copiados sem alteração** da questão regular:

`tipo` · `disciplina` · `topico` · `conteudo` · `assunto` · `banca` · `ano` · `dificuldade` ·
`imagens` · `usedInExams` · `resolucao_link` · `created_at`

---

### Regra 7 — Campos que mudam na versão adaptada

| Campo | O que muda |
|---|---|
| `id` | Prefixo `A-` + número original. Ex: `"A-000052"` |
| `enunciado` | Texto motivador preservado + enunciado simplificado (máx. 3 frases) + pergunta em `<b>` |
| `alternativas` | Apenas 3 (A, B, C), reescritas de forma simples |
| `gabarito` | Letra correta na nova numeração: `"A"`, `"B"` ou `"C"` |

---

## Formato do enunciado adaptado (HTML)

```html
<!-- Prefixo banca/ano — obrigatório quando conhecidos -->
<!-- Faz parte do início do enunciado simplificado, não de um parágrafo separado -->

<!-- Texto motivador (se houver) — preservado integralmente -->
<p>"[trecho do texto motivador original]"</p>
<p>FONTE. Autor. Título. Veículo, ano.</p>

<!-- Imagem antes do enunciado (se houver) — preservada -->
<p>[IMAGEM]</p>

<!-- Enunciado simplificado — máx. 3 frases, iniciando com (BANCA - ANO) em negrito -->
<div style="text-align: justify;">
  <span style="font-size: 0.875rem;">
    <b>(BANCA - ANO)</b> [Frase 1 de contextualização. Frase 2, se necessário.]
  </span>
</div>

<!-- Imagem após o enunciado (se houver) — preservada -->
<p>[IMAGEM]</p>

<!-- Pergunta em negrito — obrigatória -->
<p><b>[Pergunta direta em negrito?]</b></p>
```

---

## Exemplo completo

### Questão regular (ENEM 2020) — id `"000052"`

> O uso de equipamentos elétricos custa dinheiro e libera carbono na atmosfera. Entretanto,
> diferentes usinas de energia apresentam custos econômicos e ambientais distintos. O gráfico
> mostra o custo, em centavo de real, e a quantidade de carbono liberado, dependendo da fonte
> utilizada para converter energia. Considera-se apenas o custo da energia produzida depois de
> instalada a infraestrutura necessária para sua produção.
>
> `[IMAGEM]`
>
> CAVALCANTE, R. O vilão virou herói. Superinteressante, jul. 2007.
>
> Em relação aos custos associados às fontes energéticas apresentadas, a energia obtida a partir
> do vento é
>
> A) mais cara que a energia nuclear e emite maior quantidade de carbono.
> B) a segunda fonte mais cara e é livre de emissões de carbono. ✓
> C) mais cara que a energia solar e ambas são livres de emissões de carbono.
> D) mais barata que as demais e emite grandes quantidades de carbono.
> E) a fonte que gera energia mais barata e livre de emissões de carbono.

---

### Questão adaptada — id `"A-000052"`

**`enunciado` em HTML:**

```html
<!-- Imagem preservada -->
<p>[IMAGEM]</p>

<!-- Texto motivador preservado -->
<p>CAVALCANTE, R. O vilão virou herói. Superinteressante, jul. 2007.</p>

<!-- Enunciado simplificado com prefixo (BANCA - ANO) -->
<div style="text-align: justify;">
  <span style="font-size: 0.875rem;">
    <b>(ENEM - 2020)</b> O gráfico acima mostra o custo (em centavos) e o carbono
    liberado por diferentes fontes de energia.
  </span>
</div>

<!-- Pergunta em negrito -->
<p><b>Analisando o gráfico, o que podemos afirmar sobre a energia eólica (do vento)?</b></p>
```

**`alternativas`:**
```json
[
  { "letra": "A", "texto": "É a segunda energia mais cara e não emite carbono." },
  { "letra": "B", "texto": "É a mais barata e emite muito carbono." },
  { "letra": "C", "texto": "É mais cara que a solar e também não emite carbono." }
]
```

**`gabarito`: `"A"`** ← era B na questão regular; virou A na adaptada

---

## Checklist antes de gerar cada versão adaptada

- [ ] `id` tem prefixo `A-`?
- [ ] Texto motivador preservado e posicionado **antes** do enunciado simplificado?
- [ ] `[IMAGEM]` mantido na mesma posição da questão regular?
- [ ] Tabelas de dados preservadas como `<table>`?
- [ ] Enunciado simplificado começa com `(BANCA - ANO)` em negrito?
- [ ] Enunciado simplificado tem no máximo 3 frases?
- [ ] Pergunta está em `<b>...</b>`?
- [ ] Exatamente 3 alternativas (A, B, C)?
- [ ] `gabarito` é A, B ou C e corresponde à resposta correta?
- [ ] Alternativas simples, sem pegadinhas, sem dupla negação?
- [ ] Cada alternativa trata de um único aspecto?
- [ ] Nenhuma pegadinha foi introduzida ou mantida?
- [ ] `tipo`, `disciplina`, `topico`, `conteudo`, `assunto`, `banca`, `ano`, `dificuldade` idênticos ao regular?
