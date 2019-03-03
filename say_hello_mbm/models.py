from datetime import datetime

from say_hello_mbm import db

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp=db.Column(db.DateTime(),default=datetime.now ,index=True)


