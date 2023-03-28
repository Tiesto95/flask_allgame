from flask import Flask, render_template, request
import config as config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
    from models.models_db import Cat, Game
    from form.all_form import CatForm, GameForm
    cat_dict = Cat.query.all()

    return render_template('cat_html.html', data=cat_dict)

@app.route('/add_cat', methods=['POST'])
def add_cat():
    from models.models_db import Cat, Game
    from form.all_form import CatForm, GameForm
    if request.method == 'POST':
        form = CatForm(request.form)
        if form.validate():
            data = Cat(**form.data)
            db.session.add(data)
            db.session.commit()
        else:
            print('Валидация не прошла.')
    return 'Запрос выполнен'

if __name__ == '__main__':
    from models.models_db import *
    db.create_all()

    app.run()