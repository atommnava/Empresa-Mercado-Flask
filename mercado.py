from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/hogar")
def home():
    return render_template('home.html')

@app.route("/about/<usuario>")
def about_page(usuario):
    return f"<h1>Esta es la pagina ABOUT de {usuario}</h1>"

@app.route("/mercado")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', item_name='Phone')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
