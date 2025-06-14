from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/hogar')
def home():
    return render_template('home.html')

@app.route('/mercado')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/registro')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)