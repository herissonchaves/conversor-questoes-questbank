# Workflow QuestBank — Modo Lite (Antigravity)

Converte provas em PDF, Word ou imagem em questões para o **app QuestBank**,
gerando versão **regular** e **adaptada (NEE/AEE)** de cada questão.

> **Modo Lite**: imagens, figuras e gráficos são substituídos por `[IMAGEM]` no JSON.
> O usuário adiciona as imagens manualmente no QuestBank após a importação.
> Isso reduz significativamente o consumo de tokens do agente.

---

## Estrutura do projeto

```
questbank-lite/
├── AGENT.md              ← Orquestração do agente Antigravity
├── SKILL-questbank.md    ← Schema e regras do JSON QuestBank
├── SKILL-adaptacao.md    ← Regras de adaptação NEE/AEE
├── SKILL-segmentador.md  ← Como segmentar questões do texto extraído
├── SKILL-latex.md        ← Regras de formatação LaTeX
├── construtor.py         ← Extrator de texto (sem imagens)
├── entrada/              ← Coloque seus arquivos aqui
└── saida/                ← JSON gerado aqui
```

---

## Como usar

### 1. Configurar no Antigravity
- Crie um novo projeto no Google Antigravity
- Faça upload de todos os arquivos desta pasta

### 2. Adicionar as provas
- Coloque PDFs, DOCXs ou imagens na pasta `entrada/`

### 3. Iniciar
- No chat do Antigravity: 

Leia o AGENT.md. Converta os arquivos da pasta entrada em questões para o QuestBank.
ID inicial é 01

- Informe o **ID inicial** quando o agente pedir (ex: `000052`)

### 4. Resultado
- `saida/questoes_exportadas.json` — pronto para importar no QuestBank
- Questões com `[IMAGEM]` indicam onde adicionar figuras manualmente

### 5. Importar e completar imagens
- Importe o JSON no QuestBank
- Para cada questão com `[IMAGEM]`, adicione a imagem/figura original pelo editor do app

---

## IDs das questões

| Questão | ID |
|---|---|
| Regular (1ª) | `000052` |
| Adaptada (1ª) | `A-000052` |
| Regular (2ª) | `000053` |
| Adaptada (2ª) | `A-000053` |

---

## Diferenças entre versões

| Recurso | Workflow Completo | **Modo Lite** |
|---|---|---|
| Imagens extraídas em base64 | ✅ Sim | ❌ Não — `[IMAGEM]` |
| Tabelas de dados preservadas | ✅ Sim | ✅ Sim |
| Versão adaptada NEE/AEE | ✅ Sim | ✅ Sim |
| Metadados automáticos | ✅ Sim | ✅ Sim |
| Consumo de tokens | Alto | **Baixo** |

---

## Formatos de arquivo suportados

| Formato | Extensão | Texto extraído | Imagens |
|---|---|---|---|
| PDF | `.pdf` | ✅ | `[IMAGEM]` |
| Word | `.docx` `.doc` | ✅ | `[IMAGEM]` |
| Imagem | `.png` `.jpg` `.jpeg` etc. | OCR (se disponível) | `[IMAGEM]` |
| HTML | `.html` `.htm` | ✅ | `[IMAGEM]` |

---

## Dependências Python (instaladas automaticamente pelo construtor.py)

- `pymupdf` — leitura e extração fiel de PDF (texto + formatação)
- `python-docx` + `lxml` — leitura fiel de DOCX (negrito, itálico, tabelas, equações)
- `beautifulsoup4` — leitura de HTML
- `pytesseract` — interface Python para o Tesseract OCR
- `Pillow` — manipulação de imagens
- `opencv-python-headless` + `numpy` — pré-processamento de imagens (CLAHE, binarização Otsu)

## Dependência de sistema

- **Tesseract OCR** com pacote de idioma português (`tesseract-ocr-por`)
  - Windows: https://github.com/UB-Mannheim/tesseract/wiki
  - macOS: `brew install tesseract tesseract-lang`
  - Linux: `sudo apt install tesseract-ocr tesseract-ocr-por`

O `construtor.py` detecta automaticamente o Tesseract nos locais de instalação padrão
(Windows `Program Files`, macOS Homebrew, Linux `/usr/bin`).
