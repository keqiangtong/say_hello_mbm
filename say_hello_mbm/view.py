#coding:utf-8

from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from say_hello_mbm import app,db
from form import SayHelloForm
from models import Message


@app.route('/', methods=['post','get'])
def index():
    form = SayHelloForm()

    # db.create_all()      这一句我不知道放在那合适　　案例程序里是放在了ｃｏｍｍａｎｄ里
    if form.validate_on_submit():

        name = form.name.data
        message = form.message.data

        print(name)
        message_db = Message(name=name,body=message)
        db.session.add(message_db)
        db.session.commit()
        flash('message commit!')
        return redirect(url_for('index'))

    msg = Message.query.order_by(Message.timestamp.desc()).all()

    return render_template('index.html',form=form,msg=msg)

