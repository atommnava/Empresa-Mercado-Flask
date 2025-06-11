from enum import nonmember

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Hello Atom!</h2>"

@app.route("/about/<usuario>")
def about_page(usuario):
    return f"<h1>Esta es la pagina ABOUT de {usuario}</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
