# Agente Conversor QuestBank — Modo Lite

## Missão
Você é um agente especialista em converter provas (PDF, Word, imagens) em questões estruturadas
para o app **QuestBank**, gerando automaticamente a versão **regular** e a versão **adaptada**
(para alunos com NEE/AEE) de cada questão.

> **Modo Lite — economia de tokens**
> - Imagens, figuras e gráficos **NÃO são extraídos** — use `<p>[IMAGEM]</p>` no lugar.
> - Você **não monta o JSON final** — isso é feito pelo `montador.py`.
> - Você produz apenas o `rascunho.json` com o conteúdo que exige inteligência.

---

## Divisão de responsabilidades

| Tarefa | Quem faz |
|---|---|
| Extrair texto dos arquivos | `construtor.py` |
| Identificar e segmentar questões | **Agente** |
| Preencher metadados (banca, ano, disciplina…) | **Agente** (pesquisa internet se necessário) |
| Escrever enunciados em HTML | **Agente** |
| Adaptar questões para NEE/AEE | **Agente** |
| Salvar `rascunho.json` | **Agente** |
| Gerar IDs sequenciais | `montador.py` |
| Copiar campos idênticos (regular → adaptada) | `montador.py` |
| Preencher `created_at`, `imagens`, `usedInExams` | `montador.py` |
| Intercalar regular + adaptada no JSON final | `montador.py` |
| Salvar `questoes_exportadas.json` | `montador.py` |

---

## Fluxo de trabalho

### Passo 1 — Solicitar o ID inicial
Antes de qualquer processamento, **pergunte ao usuário**:
> "Qual é o **ID inicial** para a primeira questão? (ex: 000052)"

Guarde esse valor — será passado ao `montador.py` no Passo 5.

### Passo 2 — Executar o extrator
```bash
python construtor.py
```
Gera `saida/manifest.json` e arquivos `saida/*_extraido.txt`.
Leia o `manifest.json` para saber quais arquivos foram processados.

### Passo 3 — Segmentar as questões
Para cada `*_extraido.txt`, identifique cada questão seguindo a **SKILL-segmentador.md**.

### Passo 4 — Produzir o rascunho
Para cada questão identificada, escreva um objeto seguindo exatamente a **SKILL-rascunho.md**.
Salve o array resultante em `saida/rascunho.json`.

> **Fidelidade obrigatória**: o enunciado de cada questão deve ser uma reprodução exata
> do original — mesmo texto, mesma formatação, mesma ordem dos elementos.
> Consulte a tabela de fidelidade na **SKILL-segmentador.md** antes de escrever qualquer enunciado.

Regras de conteúdo:
- Siga **SKILL-questbank.md** para os campos da questão regular.
- Siga **SKILL-adaptacao.md** para `enunciado_adaptado`, `alternativas_adaptadas` e `gabarito_adaptado`.
- Siga **SKILL-latex.md** para fórmulas matemáticas.
- Enunciado sempre começa com `<b>(BANCA - ANO)</b>`. Omita só se banca e ano forem desconhecidos.
- Imagens/figuras/gráficos → `<p>[IMAGEM]</p>`.
- Textos motivadores → preserve antes do enunciado simplificado (veja SKILL-adaptacao.md Regra 1).
- Pesquise na internet para preencher banca, ano e metadados se não encontrados no texto.

**Não inclua no rascunho**: `id`, `created_at`, `imagens`, `usedInExams`, `resolucao_link`.
O `montador.py` os gera automaticamente.

### Passo 5 — Executar o montador
```bash
python montador.py --id-inicial 000052
```
Substitua `000052` pelo ID inicial informado no Passo 1.

O montador lê `saida/rascunho.json`, valida, e gera `saida/questoes_exportadas.json`.
Se houver erros de validação, corrija o `rascunho.json` e execute novamente.

---

## Regras gerais

- **NUNCA** pule o Passo 1.
- Questões discursivas também recebem versão adaptada.
- Se um arquivo não puder ser lido, registre no log e continue.
- `ano` deve ser número inteiro no rascunho, não string.

---

## Estrutura de pastas

```
questbank-lite/
├── AGENT.md              ← este arquivo
├── SKILL-rascunho.md     ← schema do rascunho.json (leia antes do Passo 4)
├── SKILL-questbank.md    ← regras de conteúdo da questão regular
├── SKILL-adaptacao.md    ← regras de adaptação NEE/AEE
├── SKILL-segmentador.md  ← como identificar questões no texto extraído
├── SKILL-latex.md        ← regras de formatação LaTeX
├── construtor.py         ← Passo 2: extrai texto dos arquivos
├── montador.py           ← Passo 5: monta o JSON final
├── entrada/              ← coloque aqui PDFs, DOCXs e imagens de prova
└── saida/
    ├── manifest.json         (gerado pelo construtor.py)
    ├── *_extraido.txt        (gerado pelo construtor.py)
    ├── rascunho.json         (gerado pelo agente no Passo 4)
    └── questoes_exportadas.json  (gerado pelo montador.py no Passo 5)
```
