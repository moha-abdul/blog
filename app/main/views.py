from flask import render_template
from ..models import Role, User
from . import main
from .. import db


@main.route('/')
def index():

    '''
    View of root page function that returns the index page and its data
    '''
    message = 'hello'
    return render_template('index.html', message = message)