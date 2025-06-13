from enum import unique

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.app_context().push()
db = SQLAlchemy(app)

# Añade este bloque para crear tablas automáticamente al iniciar
with app.app_context():
    db.create_all()

import models
import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)