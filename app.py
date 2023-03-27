from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
    pass

