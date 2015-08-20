"""
    logbook.user.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the user profile page.

"""

from flask import current_app, Blueprint, render_template

user = Blueprint('user', __name__)

@user.route('/')
def index():
    return 'Hello. This is the first page of user profile.'
