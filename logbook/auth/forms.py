"""
    logbook.auth.forms
    ~~~~~~~~~~~~~~~~~~

    It provides the forms that are needed for the auth views.
"""

from flask_wtf import Form
from wtforms import (TextAreaField, StringField, SubmitField, PasswordField,
    BooleanField, HiddenField)
from wtforms.validators import (DataRequired, InputRequired, Email, Length,
    ValidationError, EqualTo)
from logbook.user.models import User
from datetime import datetime

class LoginForm(Form):
    # username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', validators=[
        Length(min=6, max=35),
        Email(message="An email address is required.")],
        description="Email"
        )
    password     = PasswordField(description="Password")
    remember_me = BooleanField("Remember Me", default=False)
    submit = SubmitField("Submit")

class RegisterForm(Form):
    name = StringField("Name", description="Full Name")
    email        = StringField('Email Address', validators=[
        Length(min=6, max=35),
        Email(message="An email address is required.")],
        description="Email"
    )
    password = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('confirm_password', message="Passwords does not match.")
        ],
        description="Password")

    confirm_password = PasswordField('Confirm password',
        description="Type password again")

    def validate_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if email:
            raise ValidationError("This email has already been registered.")

    def save(self):
        user = User(name=self.name.data,
                    email=self.email.data,
                    password=self.password.data,
                    picture=""
                    )
        return user.save()

class ForgotPasswordForm(Form):
    email = StringField('Email Address', validators=[
        DataRequired(message="An email address is required"),
        Email()
        ])
    submit = SubmitField("Request Password")


class ResetPasswordForm(Form):
    token = HiddenField('Token')

    email = StringField('E-Mail Address', validators=[
        DataRequired(message="A E-Mail Address is required."),
        Email()])

    password = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('confirm_password', message='Passwords must match.')])

    confirm_password = PasswordField('Confirm Password')

    submit = SubmitField("Reset Password")

    def validate_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if not email:
            raise ValidationError("Wrong E-Mail Address.")
