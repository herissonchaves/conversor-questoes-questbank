# SKILL — Segmentador de Questões (Modo Lite)

## O que esta skill faz

Identifica e segmenta questões individuais a partir do texto bruto dos arquivos `*_extraido.txt`.
O texto já virá com marcadores `[IMAGEM]` onde havia figuras/gráficos.

---

## Como identificar questões

### Marcadores de início de questão

| Padrão | Exemplos |
|---|---|
| Número + ponto/parêntese | `1.` `2.` `3)` `01.` `02.` |
| "Questão" + número | `Questão 1` `QUESTÃO 01` |
| Número entre parênteses | `(1)` `(2)` |
| Número romano | `I.` `II.` `III.` |
| Variações | `Q1` `Q.01` `1-` |

Se não houver marcadores claros, use o padrão de alternativas como delimitador:
um bloco de `a)` / `b)` / `c)` indica o fim de uma questão.

---

## Componentes de cada questão

| Componente | Como identificar |
|---|---|
| **Enunciado** | Texto entre o marcador de início e as alternativas |
| **Marcador `[IMAGEM]`** | Já presente no texto extraído — preserve na posição correta |
| **Alternativas** | Linhas iniciadas por `a)` `b)` `c)` `d)` `e)` ou `A)` `B)` `C)` `D)` `E)` |
| **Gabarito** | Ao final da prova ou em seção separada: `1-B`, `2.C`, `Gabarito: D` |
| **Tabelas** | Texto com separadores `|` ou alinhamento por espaços — converter para `<table>` HTML |

---

## Tratamento de `[IMAGEM]`

O `construtor.py` já inseriu `[IMAGEM]` onde havia figura/gráfico.

---

## ⚠️ Regra de fidelidade total — obrigatória

O texto nos arquivos `*_extraido.txt` é a **fonte primária**. Ao converter cada questão
para o campo `enunciado` do rascunho, você deve reproduzir o conteúdo **exatamente**
como está no documento original. Isso significa:

| Elemento no original | Como representar no HTML do enunciado |
|---|---|
| Texto em **negrito** | `<b>texto</b>` |
| Texto em *itálico* | `<i>texto</i>` |
| Texto <u>sublinhado</u> | `<u>texto</u>` |
| Parágrafo alinhado à direita | `<p style="text-align:right;">...</p>` |
| Parágrafo centralizado | `<p style="text-align:center;">...</p>` |
| Parágrafo justificado | `<p style="text-align:justify;">...</p>` |
| Equação ou fórmula matemática | LaTeX inline `$...$` ou bloco `$$...$$` — siga SKILL-latex.md |
| Tabela de dados | `<table>` HTML com todas as linhas e colunas |
| Figura / gráfico / imagem | `<p>[IMAGEM]</p>` — nunca omita, nunca descreva |
| Texto motivador (citação, trecho) | Preserve integralmente, antes do enunciado |
| Referência bibliográfica | `<p>AUTOR. Título. Veículo, ano.</p>` |

**Nunca resuma, parafraseie ou omita** trechos do enunciado original.
Se o extrator gerou um marcador `$[EQUAÇÃO: ...]$`, converta o conteúdo para LaTeX correto
seguindo a SKILL-latex.md antes de gravar no rascunho.


Ao montar o `enunciado` em HTML, converta cada ocorrência para:
```html
<p>[IMAGEM]</p>
```

Nunca remova nem tente substituir o marcador por outra coisa.

---

## Tratamento de tabelas

Tabelas de dados (linhas/colunas com texto e números) aparecem como:
```
Velocidade (m/s) | Tempo (s) | Distância (m)
10               | 2         | 20
20               | 2         | 40
```

Converta para HTML:
```html
<table border="1" cellpadding="4" cellspacing="0">
  <tr><th>Velocidade (m/s)</th><th>Tempo (s)</th><th>Distância (m)</th></tr>
  <tr><td>10</td><td>2</td><td>20</td></tr>
  <tr><td>20</td><td>2</td><td>40</td></tr>
</table>
```

---

## Identificação de banca e ano

**Ordem de busca — siga esta sequência. Se não encontrar em nenhuma etapa, use os valores
padrão. Jamais invente banca, ano ou qualquer outro metadado.**

1. **Texto extraído** — procure no cabeçalho, rodapé ou enunciados por:
   - Nome da banca: `ENEM`, `FUVEST`, `UNICAMP`, `VUNESP`, `UERJ`, `ITA`, `IME`, etc.
   - Ano em 4 dígitos: `2023`, `2024`, etc.

2. **Busca na internet com trechos do enunciado** — use um fragmento único entre aspas
   (ex: `"Suponha que o robô da RioBotz tenha massa de 18 kg"`) para localizar a prova
   em sites oficiais. Consulte preferencialmente os sites listados em **SKILL-questbank.md** ou outros sites oficiais que encontrar (domínios `.br`, `.gov.br`, `.edu.br`, sites institucionais). Nunca use fóruns ou blogs.

3. **Não encontrado** → `banca: "Desconhecida"`, `ano: 0`. Nunca suponha nem invente.

---

## Gabarito separado

Gabaritos ao final de provas costumam aparecer em formatos como:

```
1-A  2-C  3-B  4-E  5-D
```
ou:
```
1. B    2. D    3. A
```

Associe cada gabarito à questão correspondente pelo número.

---

## Checklist de segmentação

- [ ] Todas as questões foram identificadas?
- [ ] Cada questão tem enunciado, tipo e gabarito?
- [ ] Marcadores `[IMAGEM]` estão na posição correta do enunciado?
- [ ] Questões objetivas têm todas as alternativas?
- [ ] Tabelas de dados foram convertidas para `<table>` HTML?
- [ ] Gabaritos associados corretamente?
- [ ] Banca e ano identificados no texto ou pesquisados em site oficial?
- [ ] Se não encontrado, usado `"Desconhecida"` / `0` em vez de inventar?
