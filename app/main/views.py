from flask import render_template, request, redirect,url_for, abort
from . import main 
from ..models import User, Category, Pitch, Votes, Category
from ..import db
from forms import Pitch_form, Category_form, Comment_form
from flask_login import login_required,current_user

@main.route('/')
def index():
    '''
    root page function
    '''
    
    return render_template('index.html')

#Aunthecate routes that allow auntheticated users to submit new pitch
@main.route('/category/new-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    pitch = Pitch_form()
    category = Category.query.filter_by(id=id).first()
    
    if category is None:
        abort(404)   #404 status code returned if no user is found in database
        
    if pitch.validate_on_submit():
        content = pitch.content.data
        new_pitch = Pitch(content=content,category_id= category.id,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=category.id))
    title = 'New pitch'
    return render_template('new_pitch.html',title = title, Pitch_form = pitch, category=category)
        
      