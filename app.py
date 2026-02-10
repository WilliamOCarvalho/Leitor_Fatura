from flask import Flask, render_template, request, redirect, send_file
from pathlib import Path
import uuid

from leitor_fatura import read_pdf_extract, load_keywords, add_keyword, write_xlsx

app = Flask(__name__)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

KEYWORDS_FILE = Path("keywords.json")


@app.route("/", methods=["GET", "POST"])
def index():
    lancamentos = []
    total = 0

    if request.method == "POST":
        pdf = request.files["pdf"]
        if pdf:
            nome = f"{uuid.uuid4()}.pdf"
            caminho = UPLOAD_DIR / nome
            pdf.save(caminho)

            keywords = load_keywords(KEYWORDS_FILE)
            lancamentos = read_pdf_extract(caminho, keywords)
            total = sum(l.valor for l in lancamentos)

            output = Path("resultado.xlsx")
            write_xlsx(output, lancamentos, keywords)

    return render_template(
        "index.html",
        lancamentos=lancamentos,
        total=total,
        keywords=load_keywords(KEYWORDS_FILE),
    )


@app.route("/add_keyword", methods=["POST"])
def add_kw():
    termo = request.form.get("termo")
    if termo:
        add_keyword(KEYWORDS_FILE, termo)
    return redirect("/")


@app.route("/download")
def download():
    return send_file("resultado.xlsx", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
