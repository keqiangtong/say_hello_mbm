
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

bootstrap = Bootstrap(app)


app.config.from_pyfile('config.py')
db = SQLAlchemy(app)



from say_hello_mbm import view,models

