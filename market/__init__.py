from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.app_context().push()
app.config['SECRET_KEY'] = '8cdd20bff06ff3be077b779f'
db = SQLAlchemy(app)

from market import routes