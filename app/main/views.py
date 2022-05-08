from flask import render_template, request, redirect,url_for
from . import main


@main.route('/')
def index():
    '''
    root page function
    '''
    
    return render_template('index.html')