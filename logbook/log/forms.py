"""
    logbook.log.forms
    ~~~~~~~~~~~~~~~~~~

    This provides the forms that are needed for the log views.
"""

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length

class NewLogForm(Form):
    subject = StringField("Subject", validators=[
        Length(max=200)],
        description="Subject")
    link = StringField("Link", validators=[
        Length(max=200)],
        description="Link")
    notes = TextAreaField("Notes", description="Notes")
    tag = StringField("Tag", description="Tags (seperated by comma)")
    submit = SubmitField("Submit")
