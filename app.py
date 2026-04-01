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
    app.run(debug=True)