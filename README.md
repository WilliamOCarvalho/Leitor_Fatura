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
- **HTML / CSS / JavaScript** – Interface
- **Bootstrap** – Estilização (opcional)
- **Pandas** – Organização e soma de dados

---

## 📁 Estrutura do Projeto

```text
leitor_fatura/
│
├── app.py                 # Arquivo principal da aplicação Flask
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação
│
├── templates/
│   ├── index.html         # Interface principal
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── uploads/               # PDFs enviados pelo usuário
│
├── services/
│   ├── leitor_pdf.py      # Lógica de leitura do PDF
│   └── extrator.py        # Regras de extração e filtros
│
└── keywords.json          # Palavras-chave para identificação de cobranças
