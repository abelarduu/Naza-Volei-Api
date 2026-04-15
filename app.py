from flask import Flask, render_template  
from database import DB
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route("/Galeria")
def gallery():
    return render_template("gallery.html") 

@app.route("/Atletas")
def athletes():
    """Retorna todos os atletas cadastrados ou uma mensagem de ausência de atletas."""
    dados = [
        {"name": "Ygor Rafael", "icon": "assets/images/athletes/ygor-icon.png"},
        {"name": "Abel Lucas", "icon": "assets/images/athletes/Abel-icon.png"},
        {"name": "Miguel", "icon": "assets/images/athletes/Miguel-icon.png"},
        {"name": "Davi", "icon": "assets/images/athletes/Davi-icon.png"}
    ]

    return render_template("Athletes.html", atletas=dados)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)