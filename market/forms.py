from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='Nombre de Usuario:')
    email_address = StringField(label='Corréo electrónico:')
    password1 = PasswordField(label='Contraseña:')
    password2 = PasswordField(label='Confirmar Contraseña:')
    submit = SubmitField(label='¡Quiero ser MiMercado!')