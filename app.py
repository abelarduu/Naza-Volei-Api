import os
from flask import Flask, render_template  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route("/Galeria")
def gallery():
    return render_template("gallery.html") 

@app.route("/Atletas")
def athletes():
    return render_template("Athletes.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)