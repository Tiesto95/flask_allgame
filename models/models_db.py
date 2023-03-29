from app import db
from sqlalchemy.orm import validates
from datetime import date


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    descr1 = db.Column(db.Text)
    descr2 = db.Column(db.Text)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False, index=True)
    cat = db.relationship('Cat', foreign_keys=[cat_id])
    code = db.Column(db.Text, nullable=False)
    descr = db.Column(db.Text)
    add_date = db.Column(db.Date, default=date.today(), nullable=False)
    is_visable = db.Column(db.Boolean, default=True, nullable=False)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text)
    descr = db.Column(db.Text)
    add_date = db.Column(db.Date, default=date.today(), nullable=False)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)