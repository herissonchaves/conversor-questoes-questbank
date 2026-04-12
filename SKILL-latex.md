# SKILL — Regras de LaTeX e Formatação Matemática

---

## ⛔ REGRA CRÍTICA — Escaping de backslash em JSON

**Todo `\` de LaTeX vira `\\` dentro de strings JSON.**

| Você quer escrever | Coloque no JSON |
|---|---|
| `\text{kg}` | `\\text{kg}` |
| `\times` | `\\times` |
| `\frac{a}{b}` | `\\frac{a}{b}` |
| `\vec{F}` | `\\vec{F}` |
| `\Delta v` | `\\Delta v` |
| `\,` (espaço fino) | `\\,` |
| `\cdot` | `\\cdot` |

**Por quê?** Em JSON, `\t` é caractere de tabulação, `\n` é quebra de linha, etc.
Se você escrever `\text`, o parser JSON lê `\t` como tab e sobra `ext` — daí o bug
`extkg` no lugar de `kg`.

**Exemplos corretos no rascunho.json:**
```json
"enunciado": "...massa de $18\\,\\text{kg}$..."
"enunciado": "...pressão de $3{,}6 \\times 10^{10}\\,\\text{Pa}$..."
"texto": "$v_0 = 15\\,\\text{m/s}$"
```

---

## ⛔⛔ ATENÇÃO ESPECIAL: versão adaptada (`enunciado_adaptado`)

O bug de `extm`, `extPa`, `imes10³` aparece especificamente na versão adaptada porque
o agente tende a reescrever o enunciado do zero e adicionar LaTeX sem lembrar do escaping.

**Regra prática para a versão adaptada:**
1. **Copie o HTML já extraído** com `<sup>`/`<sub>` quando possível — não reescreva com LaTeX
2. Se precisar de LaTeX, **toda `\` vira `\\` no JSON** — sem exceção
3. Teste mental: `\text{m}` → no JSON escrevo `\\text{m}` → renderiza como `m` ✓

---

## Quando usar LaTeX vs HTML puro

O extrator (`construtor.py`) já produz `<sup>` e `<sub>` para potências e índices.
**Preserve o HTML quando possível — use LaTeX só quando HTML não é suficiente.**

| Situação | Use | Exemplo |
|---|---|---|
| Potência/expoente simples em prosa | HTML `<sup>` | `m<sup>2</sup>`, `10<sup>5</sup>` |
| Índice simples em prosa | HTML `<sub>` | `v<sub>0</sub>` |
| Unidade simples em prosa | Texto puro | `18 kg`, `15 m/s` |
| Notação científica na prosa | HTML `<sup>` | `3,6 · 10<sup>10</sup>` |
| Fração | LaTeX `$\\frac{}{}$` | `$\\frac{F}{A}$` |
| Letra grega | LaTeX | `$\\Delta v$`, `$\\rho$` |
| Fórmula complexa inline | LaTeX `$...$` | `$E = mc^2$` |
| Fórmula em bloco | LaTeX `$$...$$` | `$$F = ma$$` |
| Raiz quadrada | LaTeX | `$\\sqrt{2}$` |
| Vetor | LaTeX | `$\\vec{F}$` |

---

## Regras específicas

### Vírgula decimal
Use `{,}` dentro de LaTeX (padrão brasileiro):
```
✓  $3{,}6 \\times 10^{10}$
✗  $3.6 \\times 10^{10}$
```

### Unidades em expressões LaTeX
Use `\\,\\text{}` para separar número de unidade **quando dentro de LaTeX**:
```
✓  $9{,}8\\,\\text{m/s}^2$
✗  $9,8 m/s^2$
```

### Subscritos e sobrescritos em LaTeX
Sempre dentro de `$...$`:
```
✓  $v_0 = 5\\,\\text{m/s}$
✗  v_0 = 5 m/s  (fora do LaTeX)
```

### Notação científica em LaTeX
```
✓  $3{,}0 \\times 10^8\\,\\text{m/s}$
```

### Frações
```
✓  $\\frac{F \\cdot \\Delta t}{A}$
```

### Linhas de resposta (discursivas)
Use `\_\_\_\_`:
```
A pressão exercida é \_\_\_\_ Pa.
```

---

## Exemplos completos corretos no rascunho.json

### Enunciado com unidades em prosa (HTML puro — sem LaTeX):
```json
"enunciado": "<p>Suponha que o robô tenha massa de 18 kg e uma área de 1 mm<sup>2</sup>. A lança atinge a parede a 15 m/s e recua a 3 m/s em 9 ms.</p>"
```

### Alternativa com notação científica (HTML):
```json
{ "letra": "A", "texto": "3,6 · 10<sup>10</sup>" }
```

### Enunciado com fórmula inline (LaTeX — backslash dupla no JSON):
```json
"enunciado": "<p>A força resultante é $\\vec{F} = m \\cdot \\vec{a}$, onde $m$ é a massa.</p>"
```

### Alternativa com fórmula LaTeX:
```json
{ "letra": "B", "texto": "$\\frac{mv}{t} = 2{,}7 \\times 10^9\\,\\text{Pa}$" }
```

---

## Checklist LaTeX

- [ ] Toda `\` LaTeX está como `\\` na string JSON?
- [ ] Vírgulas decimais usam `{,}`?
- [ ] Unidades simples em prosa ficaram como texto puro?
- [ ] Potências em prosa usam `<sup>` HTML?
- [ ] Unidades em expressões LaTeX usam `\\,\\text{}`?
- [ ] Subscritos/sobrescritos dentro de `$...$`?
