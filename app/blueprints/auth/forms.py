from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import User 
import random 
from jinja2 import Markup


class LoginForm(FlaskForm):
    #field name = DatatypeField('LABEL', validators =[LIST OF validators])
    email = StringField('Email Address', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email Address', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
        EqualTo('password', message='Passwords, must match!')])
    submit = SubmitField('Register')

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email Address', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), 
        EqualTo('password', message = 'Passwords, must match!')])
    submit = SubmitField('Submit Changes')



