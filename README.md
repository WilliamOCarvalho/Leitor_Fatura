# Leitor de Fatura de Cartão 💳📊

Este projeto tem como objetivo **automatizar a leitura de faturas de cartão de crédito em PDF**, identificando gastos específicos (como Uber, 99, etc.), listando as transações encontradas e calculando o **total geral** de forma clara, no estilo planilha.

O sistema foi pensado para facilitar o controle mensal de gastos e permitir evolução futura, como novos filtros, categorias e melhorias visuais.

---

## 🚀 Funcionalidades

- 📂 Upload de faturas em PDF
- 🔍 Identificação automática de cobranças por palavras-chave
- 📅 Extração de data, descrição e valor
- ➕ Soma automática do total geral
- 🧾 Visualização em formato de tabela (estilo planilha)
- ⚙️ Cadastro de novas palavras-chave para busca
- 🌐 Interface web acessada pelo navegador
- 📤 Exportação dos dados (CSV / planilha)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask** – Backend web
- **pdfplumber** – Leitura e extração de texto de PDFs
- **openpyxl** – Geração da planilha Excel
- **HTML / CSS / JavaScript** – Interface
- **Bootstrap** – Estilização (opcional)

---

## 📁 Estrutura do Projeto

```text
leitor_fatura/
│
├── app.py                 # Arquivo principal da aplicação Flask
├── leitor_fatura.py       # Parser do PDF e exportação XLSX
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação
├── keywords.json          # Palavras-chave para identificação de cobranças
├── resultado.xlsx         # Planilha gerada após o processamento
│
├── templates/
│   ├── index.html         # Interface principal
│
├── static/
│   └── style.css
│
└── uploads/               # Criado automaticamente ao rodar a aplicação
```

## ▶️ Como rodar no Windows com ambiente virtual

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000` no navegador.

Nas próximas execuções, basta ativar o ambiente e iniciar a aplicação:

```powershell
.\.venv\Scripts\Activate.ps1
python app.py
```

Se o PowerShell bloquear a ativação, execute diretamente:

```powershell
.\.venv\Scripts\python.exe app.py
```

## Rodar com o Python local

As dependências também podem ser instaladas e executadas sem ativar um ambiente:

```powershell
python -m pip install -r requirements.txt
python app.py
```
