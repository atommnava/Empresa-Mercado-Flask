from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.app_context().push()
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(),
        primary_key=True
    )
    name = db.Column(db.String(length=32),
        nullable=False,
        unique=True
    )
    price = db.Column(db.Integer(),
        nullable=False
    )
    barcode = db.Column(db.String(length=16),
        nullable=False,
        unique=True
    )
    description = db.Column(db.String(length=1024),
        nullable=False
    )
@app.route("/")
@app.route("/hogar")
def home():
    return render_template('home.html')

# ... resto de tus rutas ...

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)