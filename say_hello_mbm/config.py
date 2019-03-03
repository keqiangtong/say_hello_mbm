import os

SECRET_KEY = os.getenv('SECRET_KEY','sdlf;jwocnowf')

SQLALCHEMY_DATABASE_URI = 'mysql://aaa:aaa@127.0.0.1:3306/say_hello_mbm'
SQLALCHEMY_TRACK_MODIFICATIONS = False