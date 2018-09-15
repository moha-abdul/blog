from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()]) #email field
    username = StringField('Enter your username',validators = [Required()])   #username field
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])  #password
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])  #confirm password
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        '''
        checks if the email belongs to another account
        '''
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('email already in use')
    
    def validate_username(self,data_field):
        '''
        checks if the username is available
        '''
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')