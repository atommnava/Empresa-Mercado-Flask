from flask_login import login_user
from flask import render_template, redirect, url_for, flash
from market import app
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db

@app.route('/')
@app.route('/hogar')
def home():
    return render_template('home.html')

@app.route('/mercado')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/registro', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data # la variable password es la contraseña del metodo password en 'models.py'. Linea 13
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for error in form.errors.values():
            flash(f"err_msg: {error}", category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.get(form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_user=form.password.data):
            login_user(attempted_user)

    return render_template('login.html', form=form)