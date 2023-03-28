from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm
from models.models_db import Cat, Game

class CatForm(ModelForm):
    class Meta:
        model = Cat

class GameForm(ModelForm):
    class Meta:
        model = Game