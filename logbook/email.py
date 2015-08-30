"""
    logbook.email
    ~~~~~~~~~~~~~

    This modules adds the functionality to send emails
"""

from flask_mail import Message
from flask import render_template
from logbook.extensions import mail

def send_reset_token(user, token):
    send_email(
        subject="Password Reset",
        recipients=[user.email],
        text_body=render_template(
            "email/reset_password.txt",
            user=user,
            token=token
        ),
        html_body=render_template(
            "email/reset_password.html",
            user=user,
            token=token
        )
    )


def send_email(subject, recipients, text_body, html_body, sender=None):
    msg = Message(subject, recipients=recipients, sender=sender)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
