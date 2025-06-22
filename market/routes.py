from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, flash, request
from market import app
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm
from market import db

@app.route('/')
@app.route('/hogar')
def home_page():
    return render_template('home.html')

@app.route('/mercado',  methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"¡Tu Pago se realizó con Éxito! Compraste {p_item_object.name} por ${p_item_object.price}", category='success')
            else:
                flash(f"No puedes adquirir este Producto porque no tienes suficientes fondos... {p_item_object.name}", category='danger')
        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id).first()
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items)

@app.route('/registro', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data  # La variable password es la contraseña del metodo password en 'models.py'.
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Cuenta creada exitosamente! Te registraste con {user_to_create.username}.', category='success')
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for error in form.errors.values():
            flash(f"err_msg: {error}", category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Exito! Ingresaste como: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('El nombre de usuario y/o la contraseña no coinciden! Por favor, intenta de nuevo', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('Cerraste la sesión!', category='info')
    return redirect(url_for('home_page'))