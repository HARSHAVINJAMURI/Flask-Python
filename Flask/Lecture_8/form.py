from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField('Name of student', [validators.DataRequired('Please enter your name')])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = StringField("Email", [
        validators.DataRequired('Please enter your email address'),
        validators.Email("Please enter a valid email address")
    ])

    Age = IntegerField("Age")
    Language = SelectField('Languages Known', choices=[('cpp', 'C++'), ('Py', 'Python')])

    submit = SubmitField("Submit")
