"""
    logbook.log.forms
    ~~~~~~~~~~~~~~~~~

    It provides the forms that are needed for the log views.
"""

from flask_wtf import Form
from wtforms import (TextAreaField, StringField, SubmitField, validators)

class LoginForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    
    submit = SubmitField("Submit")