"""
    logbook.admin.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the admin page.

"""

from flask import current_app, Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return 'Hello. This is the first page of admin portal.'
