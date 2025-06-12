from enum import unique

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.app_context().push()
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=32), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=16), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

# Añade este bloque para crear tablas automáticamente al iniciar
with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/hogar")
def home():
    return render_template('home.html')

@app.route("/about/<usuario>")
def about_page(usuario):
    return f"<h1>Esta es la pagina ABOUT de {usuario}</h1>"

@app.route("/mercado")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)