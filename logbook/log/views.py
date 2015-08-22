"""
    logbook.log.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the log entries creation and viewing.

"""

from flask import current_app, Blueprint, render_template

log = Blueprint('log', __name__)

@log.route('/')
def index():
	return 'Hello. This is my logbook!'

@log.route('/new/')
def new_log():
    return "This page adds a log entry."

@log.route('/<int:log_id>/edit/')
def edit_log():
    return "This page edits a log entry."

@log.route('/<int:log_id>/delete')
def delete_log():
    return "This page deletes a log entry."
