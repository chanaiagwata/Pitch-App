from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class Pitch_form(FlaskForm):
    Pitch_form = TextAreaField('Enter new pitch')
    submit = SubmitField('Submit')
