from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class Pitch_form(FlaskForm):
    Pitch_form = TextAreaField('Enter new pitch')
    submit = SubmitField('Submit')
    
class Category_form(FlaskForm):
    name = StringField('Pitch category', validators=[Required()])
    submit = SubmitField('Add to Category')
    
class Comment_form(FlaskForm):
    remark = TextAreaField('Leave a comment')
    submit = SubmitField('Submit')
