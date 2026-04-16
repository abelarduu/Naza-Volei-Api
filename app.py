from flask import Flask, render_template
from database import DB
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 


@app.route("/galeria")
def gallery():
    return render_template("gallery.html") 


@app.route("/atletas")
def athletes():
    # pega dados do banco
    DB.query("SELECT name, icon_path FROM Athletes")
    res = DB.cur.fetchall()

    # transforma no formato do Jinja
    dados = [
        {"name": r[0], "icon": r[1]}
        for r in res
    ]

    return render_template("Athletes.html", atletas=dados)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)