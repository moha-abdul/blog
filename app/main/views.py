from flask import render_template
from ..models import Role, User
from . import main
from .. import db
from flask_login import login_required, current_user


@main.route('/')
def index():

    '''
    View of root page function that returns the index page and its data
    '''
    message = 'hello'
    return render_template('index.html', message = message)
    
@main.route('/')
@login_required
def all_blogs():
    title = 'welcomed'
    return render_template('index.html',title =title)
