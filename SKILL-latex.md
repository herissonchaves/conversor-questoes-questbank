# SKILL — Regras de Formatação LaTeX

## Regras obrigatórias

### 1. Vírgula decimal
Use `{,}` para vírgula decimal em expressões LaTeX (padrão brasileiro):

```
✓  $9{,}8 \text{ m/s}^2$
✗  $9.8 \text{ m/s}^2$
```

### 2. Unidades de medida
Use `\,\text{}` para unidades de medida, separadas do número por espaço fino:

```
✓  $10\,\text{m/s}$
✓  $9{,}8\,\text{m/s}^2$
✓  $5{,}0 \times 10^3\,\text{J}$
✗  $10 m/s$
✗  $9.8 m/s^2$
```

### 3. Subscritos e sobrescritos
- Use `_{}` e `^{}` **sempre dentro de ambiente LaTeX** (`$...$`)
- Nunca use `~` para subscritos fora de LaTeX
- Nunca use `^` fora de LaTeX

```
✓  $v_0 = 5\,\text{m/s}$
✓  $E = mc^2$
✗  v~0~ = 5 m/s
✗  E = mc^2  (fora do LaTeX)
```

### 4. Fórmulas inline e em bloco
- **Inline**: envolva com `$...$`
- **Bloco** (fórmula em linha própria): envolva com `$$...$$`

```html
O trabalho é dado por $W = F \cdot d \cdot \cos\theta$.

$$E_k = \frac{1}{2}mv^2$$
```

### 5. Linhas de resposta (questões discursivas)
Use `\_\_\_\_` para linhas de preenchimento em questões discursivas:

```
A velocidade inicial do projétil é \_\_\_\_ m/s.
```

### 6. Frações
Use `\frac{numerador}{denominador}`:

```
✓  $\frac{d}{t}$
✓  $\frac{mv^2}{r}$
✗  d/t  (fora do LaTeX quando é expressão matemática)
```

### 7. Potências de 10 (notação científica)
```
✓  $3{,}0 \times 10^8\,\text{m/s}$
✗  3,0 x 10^8 m/s
```

### 8. Graus e ângulos
```
✓  $30°$  ou  $30^\circ$
✗  30 graus
```

---

## Exemplos completos

### Enunciado com fórmula inline
```html
<p>Um corpo de massa $m = 2\,\text{kg}$ é lançado com velocidade inicial
$v_0 = 10\,\text{m/s}$. Calcule a energia cinética.</p>
```

### Enunciado com fórmula em bloco
```html
<p>A Segunda Lei de Newton estabelece que:</p>
$$\vec{F}_{res} = m \cdot \vec{a}$$
<p>Onde $m$ é a massa e $\vec{a}$ é a aceleração resultante.</p>
```

### Alternativa com LaTeX
```html
{ "letra": "B", "texto": "<span>$v = 20\,\\text{m/s}$</span>" }
```

> **Atenção**: dentro de strings JSON, use `\\` para representar `\` em LaTeX.
> Ex: `\\frac`, `\\text`, `\\vec`.

---

## Checklist LaTeX

- [ ] Vírgulas decimais usam `{,}`?
- [ ] Unidades de medida usam `\,\text{}`?
- [ ] Subscritos/sobrescritos dentro de `$...$`?
- [ ] Fórmulas em bloco usam `$$...$$`?
- [ ] Dentro de JSON, `\` está escapado como `\\`?
