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

@log.route('/add')
def addLog():
    return "This page adds a log entry."
