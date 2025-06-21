from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(f"¡El usuario ya existe! Por favor, intenta otro nombre.")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError(f"¡El correo ya está registrado! Por favor, intenta otro correo.")

    username = StringField(label='Nombre de Usuario:', validators=[Length(min=2, max=32), DataRequired()])
    email_address = StringField(label='Corréo electrónico:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Contraseña:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirmar Contraseña:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='¡Quiero ser MiMercado!')

class LoginForm(FlaskForm):
    username = StringField(label='Nombre de Usuario:', validators=[DataRequired()])
    password = PasswordField(label='Contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Ingresar')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='¡Realizar Pago!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Vender')
