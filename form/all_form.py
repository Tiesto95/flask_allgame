from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm
from models.models_db import Cat, Game, News

class CatForm(ModelForm):
    class Meta:
        model = Cat

class GameForm(ModelForm):
    class Meta:
        model = Game
        include = ['cat_id']

class NewsForm(ModelForm):
    class Meta:
        model = News