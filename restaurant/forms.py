from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, DataRequired
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with your secret key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define the "user" table as an SQLAlchemy model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    fullname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(label = 'username', validators = [Length(min = 2, max = 30), DataRequired()])
    fullname = StringField(label = 'fullname', validators = [Length(min=3, max = 30), DataRequired()])
    address = StringField(label = 'address', validators = [Length(min=7, max = 50), DataRequired()])
    phone_number = IntegerField(label = 'phone_number', validators = [DataRequired()]) #try to find phone
    password1 = PasswordField(label = 'password1', validators = [Length(min = 6), DataRequired()])
    password2 = PasswordField(label = 'password2', validators = [EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Sign Up')

class LoginForm(FlaskForm):
    username = StringField(label = 'username', validators = [DataRequired()])
    password = PasswordField(label = 'password', validators = [DataRequired()])
    submit = SubmitField(label = 'Sign In')

class OrderIDForm(FlaskForm):
    orderid = StringField(label ='order-id', validators = [Length(min = 1), DataRequired()])      
    submit = SubmitField(label = 'Track')

class ReserveForm(FlaskForm):
    submit = SubmitField(label = 'Reserve')

class AddForm(FlaskForm):
    submit = SubmitField(label = 'Add')
    
class OrderForm(FlaskForm):
    submit = SubmitField(label = 'Order Now')