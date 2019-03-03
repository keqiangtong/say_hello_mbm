
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config.from_pyfile('config.py')
db = SQLAlchemy(app)



from say_hello_mbm import view,models

