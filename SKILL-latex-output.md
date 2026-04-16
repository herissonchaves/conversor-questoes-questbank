# SKILL — Saída em LaTeX (formato QuestBank `.tex`)

Use esta skill como **alternativa ao Passo 4 do AGENT.md** quando o objetivo
for gerar um arquivo `.tex` no formato importável pelo QuestBank (em vez de
`rascunho.json` → `questoes_exportadas.json`).

Vantagens do formato `.tex`:

- Edição confortável em qualquer editor LaTeX antes de importar.
- Backslash único (`\frac`, `\text`) — sem o inferno de `\\` do JSON.
- Fórmulas legíveis, diff amigável no git.
- Imagens por caminho relativo, não mais pelo marcador `[IMAGEM]` manual.

O arquivo `.tex` é convertido em JSON pelo servidor local
`questbank-server` quando importado no app.

---

## Fluxo alternativo

1. Executar `construtor.py` normalmente (Passo 2 do AGENT.md).
2. Segmentar questões (Passo 3, usando **SKILL-segmentador.md**).
3. **[substitui o Passo 4]** Escrever diretamente um arquivo `saida/rascunho.tex` seguindo o schema desta skill.
4. Não rodar `montador.py`. Em vez disso:
   - IDs são atribuídos manualmente (ou via um utilitário futuro); a regra de numeração continua a mesma — zero à esquerda, mínimo 5 dígitos, prefixo `A-` para adaptadas.
   - Salvar `saida/questoes.tex` pronto para importação.

---

## Estrutura do arquivo `.tex`

Um único arquivo contém **todas** as questões, cada uma em um bloco
`\begin{questao}{ID}...\end{questao}`. Comentários `%` são permitidos
e ignorados pelo parser — úteis para notas suas.

```latex
% arquivo: saida/questoes.tex

\begin{questao}{000052}
  \meta{tipo}{objetiva}
  \meta{banca}{ENEM}
  \meta{ano}{2020}
  \meta{disciplina}{Física}
  \meta{topico}{Energia}
  \meta{conteudo}{Fontes de energia}
  \meta{assunto}{Energia eólica}
  \meta{dificuldade}{medio}
  \meta{tags}{vestibular, ENEM}

  \enunciado{
    Texto do enunciado em LaTeX puro.

    Quebra de parágrafo com linha em branco.

    \imagem{graficos/energia.png}

    Outro parágrafo após a imagem.
  }

  \begin{alternativas}
    \alt{A}{primeira alternativa}
    \alt{B}{segunda alternativa com $\frac{a}{b}$ inline}
    \alt{C}{terceira}
    \alt{D}{quarta}
    \alt{E}{quinta}
  \end{alternativas}

  \gabarito{E}
\end{questao}
```

### Macros reconhecidas

| Macro | Obrigatória? | Campo JSON | Observação |
|---|---|---|---|
| `\begin{questao}{ID}` | sim | `id` | 5+ dígitos, `A-` para adaptadas |
| `\meta{tipo}{...}` | sim | `tipo` | `objetiva` ou `discursiva` |
| `\meta{banca}{...}` | recomendada | `banca` | `Desconhecida` se omitida |
| `\meta{ano}{...}` | recomendada | `ano` (int) | `0` se omitida |
| `\meta{disciplina}{...}` | sim | `disciplina` | |
| `\meta{topico}{...}` | sim | `topico` | |
| `\meta{conteudo}{...}` | sim | `conteudo` | |
| `\meta{assunto}{...}` | sim | `assunto` | |
| `\meta{dificuldade}{...}` | sim | `dificuldade` | `facil` / `medio` / `dificil` |
| `\meta{tags}{a, b, c}` | não | `tags[]` | vírgula separa |
| `\enunciado{...}` | sim | `enunciado` (HTML) | |
| `\begin{alternativas}...\end{alternativas}` | se objetiva | `alternativas[]` | |
| `\alt{LETRA}{texto}` | dentro do bloco | item | letra maiúscula |
| `\gabarito{...}` | objetiva: letra; discursiva: resposta | `gabarito` | |
| `\imagem{caminho}` | dentro de `\enunciado` | adiciona a `imagens[]` | caminho relativo ao `.tex` |
| `\resolucao{url}` | não | `resolucao_link` | |

---

## Conversões LaTeX → HTML (automáticas no parser)

Você **não precisa** escrever HTML. Use LaTeX puro; o parser converte:

| Em LaTeX você escreve | No HTML sai |
|---|---|
| Parágrafos separados por linha em branco | `<p>...</p>` |
| `$x$` e `$$x$$` | preservado (KaTeX renderiza) |
| `\textbf{x}` | `<strong>x</strong>` |
| `\textit{x}`, `\emph{x}` | `<em>x</em>` |
| `\textsuperscript{2}` | `<sup>2</sup>` |
| `\textsubscript{0}` | `<sub>0</sub>` |
| `\imagem{foto.png}` | `<p>[IMAGEM]</p>` + registra em `imagens` |
| `\begin{tabular}{cc}...\end{tabular}` | `<table>` com primeira linha `<th>` |
| `---`, `--` | `—`, `–` |
| `\_\_\_\_` | `____` (linha de resposta em discursivas) |

### O prefixo `(BANCA - ANO)` é automático

O parser insere `(BANCA - ANO)` no início do enunciado quando `\meta{banca}`
e `\meta{ano}` estão presentes e válidos. **Não adicione manualmente.**
Se banca é `Desconhecida` ou ano é `0`, o prefixo é omitido.

---

## Regras de fidelidade (iguais ao fluxo JSON)

- Enunciado deve reproduzir o original exatamente (mesmo texto, ordem, formatação).
- Siga **SKILL-segmentador.md** para identificar onde começa e termina cada questão.
- Siga **SKILL-questbank.md** para as regras de metadados (banca, ano, taxonomia).
- Siga **SKILL-adaptacao.md** quando for gerar a versão adaptada — cada questão
  adaptada é um bloco `\begin{questao}{A-XXXXX}...\end{questao}` separado, logo
  após a regular. **Não herda metadados** — repita-os no bloco adaptado (ajuste
  apenas o que muda, como `dificuldade` e o próprio enunciado).

### LaTeX matemático — sem escape duplo

Diferente do fluxo JSON, aqui você escreve LaTeX **literal**:

```latex
% ✓ correto no .tex (uma barra só)
$m = 18\,\text{kg}$

% ✗ errado — não use \\ no .tex
$m = 18\\,\\text{kg}$
```

### Notação científica

```latex
$3{,}6 \times 10^{10}\,\text{Pa}$
```

### Vírgula decimal dentro de `$...$`

Use `{,}` para evitar espaçamento estranho:

```latex
$9{,}8\,\text{m/s}^2$
```

### Unidades em prosa (fora de `$...$`)

Escreva como texto comum — não precisa LaTeX:

```latex
\enunciado{
  Um corpo com 18 kg e velocidade de 15 m/s...
}
```

Potências em prosa: `m\textsuperscript{2}` ou, se já estiver em contexto
matemático, coloque dentro de `$...$`.

---

## Questões adaptadas (NEE/AEE)

Cada adaptada é um bloco independente com id `A-XXXXX`:

```latex
\begin{questao}{000073}
  \meta{tipo}{objetiva}
  \meta{banca}{ENEM}
  \meta{ano}{2022}
  ...
\end{questao}

\begin{questao}{A-000073}
  \meta{tipo}{objetiva}
  \meta{banca}{ENEM}           % mesmos metadados
  \meta{ano}{2022}
  \meta{dificuldade}{facil}    % geralmente mais fácil que a original
  \meta{tags}{adaptada, NEE}
  ...
\end{questao}
```

Siga **SKILL-adaptacao.md** para as regras de conteúdo da adaptada.

---

## Exemplo de arquivo completo de saída

```latex
% saida/questoes.tex — gerado pelo agente
% 1 questão regular + 1 adaptada

\begin{questao}{000052}
  \meta{tipo}{objetiva}
  \meta{banca}{ENEM}
  \meta{ano}{2020}
  \meta{disciplina}{Física}
  \meta{topico}{Energia}
  \meta{conteudo}{Fontes de energia}
  \meta{assunto}{Energia eólica e impacto ambiental}
  \meta{dificuldade}{medio}

  \enunciado{
    O uso de equipamentos elétricos custa dinheiro e libera carbono na
    atmosfera. Entretanto, diferentes usinas de energia apresentam custos
    econômicos e ambientais distintos.

    \imagem{grafico-energia.png}

    Em relação aos custos associados às fontes energéticas apresentadas,
    a energia obtida a partir do vento é
  }

  \begin{alternativas}
    \alt{A}{mais cara que a energia nuclear e emite maior carbono.}
    \alt{B}{a segunda fonte mais cara e é livre de emissões.}
    \alt{C}{mais cara que a energia solar e ambas são livres.}
    \alt{D}{mais barata que as demais e emite grandes quantidades.}
    \alt{E}{a fonte mais barata e livre de emissões de carbono.}
  \end{alternativas}

  \gabarito{E}
\end{questao}

\begin{questao}{A-000052}
  \meta{tipo}{objetiva}
  \meta{banca}{ENEM}
  \meta{ano}{2020}
  \meta{disciplina}{Física}
  \meta{topico}{Energia}
  \meta{conteudo}{Fontes de energia}
  \meta{assunto}{Energia eólica e impacto ambiental}
  \meta{dificuldade}{facil}
  \meta{tags}{adaptada, NEE}

  \enunciado{
    O gráfico abaixo mostra o custo e a quantidade de carbono liberado
    por diferentes fontes de energia.

    \imagem{grafico-energia.png}

    \textbf{Analisando o gráfico, o que podemos afirmar sobre a energia
    eólica (vento)?}
  }

  \begin{alternativas}
    \alt{A}{É a energia mais cara do gráfico e não emite carbono.}
    \alt{B}{É a energia mais barata do gráfico e não emite carbono.}
    \alt{C}{É mais barata que a nuclear, mas emite muito carbono.}
  \end{alternativas}

  \gabarito{B}
\end{questao}
```

---

## Checklist antes de entregar o `.tex`

- [ ] Todas as questões têm `\begin{questao}{ID}...\end{questao}` balanceado?
- [ ] IDs únicos? Adaptadas com prefixo `A-`?
- [ ] Cada `\meta{}` tem dois argumentos (campo e valor)?
- [ ] `\meta{tipo}` é `objetiva` ou `discursiva`?
- [ ] Objetivas têm bloco `\begin{alternativas}` e `\gabarito{LETRA}`?
- [ ] Letra do `\gabarito` bate com uma `\alt{LETRA}{...}`?
- [ ] Discursivas têm `\gabarito{resposta}` ou `\gabarito{}` vazio?
- [ ] Fórmulas em `$...$` ou `$$...$$` fechadas?
- [ ] Barras LaTeX únicas (sem `\\` no fonte)?
- [ ] Imagens via `\imagem{caminho}` com caminho relativo ao `.tex`?
- [ ] Metadados preenchidos por pesquisa (nunca inventados)?
- [ ] Não digitou `(BANCA - ANO)` manualmente no enunciado? (é automático)
