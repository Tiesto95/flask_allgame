from flask import Flask, render_template, request
import config as config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
    from models.models_db import Cat, Game, News
    from form.all_form import CatForm, GameForm
    cat_dict = Cat.query.all()
    game_dict = Game.query.join(Cat).all()
    news_dict = News.query.all()
    data_t = [cat_dict, game_dict, news_dict]
    return render_template('cat_html.html', data=data_t)

@app.route('/add_cat', methods=['POST'])
def add_cat():
    from models.models_db import Cat
    from form.all_form import CatForm
    if request.method == 'POST':
        form = CatForm(request.form)
        if form.validate():
            data = Cat(**form.data)
            db.session.add(data)
            db.session.commit()
        else:
            print('Валидация не прошла.')
    return 'Запрос выполнен'

@app.route('/add_game', methods=['POST'])
def add_game():
    from models.models_db import Game
    from form.all_form import GameForm
    if request.method == 'POST':
        print(request.form)
        form = GameForm(request.form)
        if form.validate():
            print(form.data)
            data = Game(**form.data)
            db.session.add(data)
            db.session.commit()
        else:
            print('Валидация не прошла')
    return 'Запрос выполнен'


@app.route('/add_news', methods=['POST', 'GET'])
def add_news():
    from models.models_db import News
    from form.all_form import NewsForm
    if request.method == 'POST':
        form = NewsForm(request.form)
        if form.validate():
            data = News(**form.data)
            db.session.add(data)
            db.session.commit()
        else:
            print('Валидация не прошла')
        return "Новость добавлена"
    if request.method == 'GET':
        return render_template('add_news.html')

if __name__ == '__main__':
    from models.models_db import *
    db.create_all()

    app.run()