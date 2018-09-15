from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(db.Model,UserMixin):
    '''
    user class
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())


    def __repr__(self):
        return f'User {self.username}'
    
    

    @property
    def password(self):
        '''
        blocks access to the password property
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        '''
        takes in password, hashes it and compares it to the hashed password
        '''
        return check_password_hash(self.pass_secure,password)

    
    '''
    @login_manage.user_loader that modifies the load_user function by passing in a user_id to the function that queries the database and gets a User with that ID
    '''
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Role(db.Model):
    '''
    role class
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='roles', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'