from flask_wtf import FlaskForm
# from webhelpers.html.tags import submit
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Sign Up')