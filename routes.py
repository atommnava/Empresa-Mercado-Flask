@app.route("/")
@app.route("/hogar")
def home():
    return render_template('home.html')

#@app.route("/about/<usuario>")
#def about_page(usuario):
#    return f"<h1>Esta es la pagina ABOUT de {usuario}</h1>"

@app.route("/mercado")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
