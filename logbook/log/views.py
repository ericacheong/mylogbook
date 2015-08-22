"""
    logbook.log.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the log entries creation and viewing.

"""

from flask import current_app, Blueprint, render_template
from logbook.log.models import User, Tag, Log

log = Blueprint('log', __name__)

@log.route('/')
def index():
    logs = Log.query.all()
    return render_template("index.html", logs=logs)
	# return 'Hello. This is my logbook!'

@log.route('/new/')
def new_log():
    return "This page adds a log entry."

@log.route('/<int:log_id>/edit/')
def edit_log():
    return "This page edits a log entry."

@log.route('/<int:log_id>/delete')
def delete_log():
    return "This page deletes a log entry."
