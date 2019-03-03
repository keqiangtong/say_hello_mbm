

from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField
from wtforms.validators import DataRequired,Length


class SayHelloForm(FlaskForm):

    name = StringField('name', validators=[DataRequired(),Length(1,20)])
    message= TextAreaField('message', validators=[DataRequired(),Length(1,200)])
    submit = SubmitField()