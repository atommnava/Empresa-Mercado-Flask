from sqlalchemy.orm import backref

from market import db

class User(db.Model):
    id = db.Column(db.Integer(),
        primary_key=True
    )
    username = db.Column(db.String(length=32),
        nullable=False,
        unique=True
    )
    email_address = db.Column(db.String(length=64),
        nullable=False,
        unique=True
    )
    password_hash = db.column(db.String(length=64),
        nullable=False
    )
    budget = db.Column(db.Integer(),
        nullable=False,
        default=1500
    )
    # No es una columna. Referencia trasera para el modelo
    items = db.relationship('Item', backref='owned_user', lazy=True)

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
        nullable=False, unique=True
    )
    description = db.Column(db.String(length=1024),
        nullable=False,
        unique=True
    )
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'
