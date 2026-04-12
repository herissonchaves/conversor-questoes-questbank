# SKILL — Rascunho do Agente (rascunho.json)

## O que é o rascunho

O agente **não monta o JSON final do QuestBank** — isso é feito pelo `montador.py`.

O agente produz apenas um arquivo intermediário enxuto: `saida/rascunho.json`.
Ele contém somente os campos que exigem inteligência (textos, metadados, adaptações).
O `montador.py` cuida de: IDs, `created_at`, `imagens`, `usedInExams`, `resolucao_link`,
cópia de campos idênticos e intercalação regular/adaptada.

---

## Schema do rascunho

O rascunho é um array JSON. Cada elemento representa **uma questão regular + sua adaptada**:

```json
[
  {
    "enunciado":            "string (HTML da questão regular)",
    "tipo":                 "objetiva | discursiva",
    "disciplina":           "string",
    "topico":               "string",
    "conteudo":             "string",
    "assunto":              "string",
    "banca":                "string",
    "ano":                  number,
    "dificuldade":          "facil | medio | dificil",
    "gabarito":             "string",
    "alternativas":         [ { "letra": "A", "texto": "..." }, ... ],
    "enunciado_adaptado":   "string (HTML da versão adaptada)",
    "alternativas_adaptadas": [ { "letra": "A", "texto": "..." }, ... ],
    "gabarito_adaptado":    "string"
  }
]
```

---

## Regras de preenchimento

### Campos da questão regular

| Campo | Regra |
|---|---|
| `enunciado` | HTML completo. Inicia com `(BANCA - ANO)` (sem negrito). Imagens → `<p>[IMAGEM]</p>` |
| `tipo` | `"objetiva"` ou `"discursiva"` |
| `disciplina` | Ex: `"Física"`, `"Química"`, `"Matemática"` |
| `topico` | Tópico amplo. Ex: `"Mecânica"`, `"Termodinâmica"` |
| `conteudo` | Conteúdo específico. Ex: `"Cinemática"`, `"Fontes de Energia"` |
| `assunto` | Assunto pontual. Ex: `"MRU"`, `"Impactos Ambientais"` |
| `banca` | Ex: `"ENEM"`, `"FUVEST"`. Se desconhecida: `"Desconhecida"` |
| `ano` | Inteiro. Se desconhecido: `0` |
| `dificuldade` | `"facil"`, `"medio"` ou `"dificil"` |
| `gabarito` | Letra maiúscula (objetiva) ou resumo/`""` (discursiva) |
| `alternativas` | Array de `{"letra":"A","texto":"..."}`. Vazio `[]` se discursiva |

### Campos da versão adaptada

| Campo | Regra |
|---|---|
| `enunciado_adaptado` | HTML seguindo SKILL-adaptacao.md. **Sempre inicia com `(BANCA - ANO)` (sem negrito). `[IMAGEM]` vem depois. Todo `[IMAGEM]`, gráfico, diagrama ou texto motivador deve ter 1–2 frases de contextualização logo após em baixo da referencia bibliografia (se houver) do marcador ou o trecho — explicando o que o elemento representa, sem revelar a resposta nem dar pistas.** |
| `alternativas_adaptadas` | Exatamente 3 itens: `A`, `B`, `C`. Vazio `[]` se discursiva |
| `gabarito_adaptado` | `"A"`, `"B"` ou `"C"` (objetiva) ou `""` (discursiva) |

> Os demais campos (`tipo`, `disciplina`, `topico`, `conteudo`, `assunto`, `banca`, `ano`,
> `dificuldade`) são **copiados automaticamente** pelo `montador.py` — não repita no rascunho.

---

## Exemplo de rascunho mínimo

```json
[
  {
    "enunciado": "<p style=\"text-align:justify;\">(ENEM - 2020) O uso de equipamentos elétricos custa dinheiro e libera carbono na atmosfera. O gráfico mostra o custo e a quantidade de carbono por fonte de energia.</p><p>[IMAGEM]</p><p>CAVALCANTE, R. O vilão virou herói. Superinteressante, jul. 2007.</p><p>Em relação aos custos, a energia obtida a partir do vento é</p>",
    "tipo": "objetiva",
    "disciplina": "Física",
    "topico": "Energia",
    "conteudo": "Fontes de Energia",
    "assunto": "Impactos Ambientais",
    "banca": "ENEM",
    "ano": 2020,
    "dificuldade": "facil",
    "gabarito": "E",
    "alternativas": [
      { "letra": "A", "texto": "mais cara que a nuclear e emite mais carbono." },
      { "letra": "B", "texto": "a segunda fonte mais cara e livre de emissões de carbono." },
      { "letra": "C", "texto": "mais cara que a solar e ambas são livres de carbono." },
      { "letra": "D", "texto": "mais barata que as demais e emite grandes quantidades de carbono." },
      { "letra": "E", "texto": "a fonte mais barata e livre de emissões de carbono." }
    ],
    "enunciado_adaptado": "<p style=\"text-align:justify;\">(ENEM - 2020)</p><p>[IMAGEM]</p><p style=\"text-align:justify;\">O gráfico acima mostra o custo (em centavos de real) e a quantidade de carbono liberado por diferentes fontes de energia.</p><p style=\"text-align:justify;\">CAVALCANTE, R. O vilão virou herói. Superinteressante, jul. 2007.</p><p><b>Analisando o gráfico, o que podemos afirmar sobre a energia eólica (do vento)?</b></p>",
    "alternativas_adaptadas": [
      { "letra": "A", "texto": "É a mais barata e não emite carbono." },
      { "letra": "B", "texto": "É a segunda mais cara e não emite carbono." },
      { "letra": "C", "texto": "É a mais barata, mas emite muito carbono." }
    ],
    "gabarito_adaptado": "A"
  }
]
```

---

## O que o `montador.py` faz com o rascunho

```
rascunho.json (agente)          questoes_exportadas.json (montador.py)
─────────────────────           ──────────────────────────────────────
enunciado               ──────► id: "000052"  (gerado)
tipo                    ──────► enunciado
disciplina/topico/...   ──────► tipo, disciplina, topico, conteudo...
banca/ano               ──────► banca, ano, dificuldade
gabarito                ──────► gabarito
alternativas            ──────► alternativas
                                imagens: []        (fixo)
                                usedInExams: []    (fixo)
                                resolucao_link: "" (fixo)
                                created_at: "..."  (gerado)

enunciado_adaptado      ──────► id: "A-000052"  (gerado)
alternativas_adaptadas  ──────► enunciado_adaptado
gabarito_adaptado       ──────► alternativas_adaptadas
                                gabarito_adaptado
                         copia► tipo, disciplina, topico, conteudo,
                                assunto, banca, ano, dificuldade,
                                imagens, usedInExams, resolucao_link,
                                created_at
```

---

## Checklist do rascunho antes de salvar

- [ ] É um array JSON válido?
- [ ] Todo `\` LaTeX está duplicado como `\\` nas strings JSON?
  - Errado: `$18\,\text{kg}$` → Certo: `$18\\,\\text{kg}$`
  - Errado: `$3 \times 10^9$` → Certo: `$3 \\times 10^9$`
- [ ] Prefere HTML `<sup>`/`<sub>` a LaTeX para potências simples? (evita o problema de escaping)
- [ ] Cada objeto tem todos os campos obrigatórios da regular?
- [ ] `enunciado` começa com `(BANCA - ANO)` (sem negrito)?
- [ ] `enunciado_adaptado` começa com `(BANCA - ANO)` (sem negrito) como **primeiro elemento**?
- [ ] `[IMAGEM]` vem **depois** de `(BANCA - ANO)`, nunca antes?
- [ ] `alternativas_adaptadas` tem exatamente 3 itens (ou `[]` se discursiva)?
- [ ] `gabarito_adaptado` é `"A"`, `"B"` ou `"C"` (ou `""` se discursiva)?
- [ ] Imagens substituídas por `<p>[IMAGEM]</p>`?
- [ ] `ano` é número inteiro (não string)?
