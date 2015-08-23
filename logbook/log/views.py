"""
    logbook.log.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the log entries creation and viewing.

"""

from flask import (current_app, Blueprint, render_template, request, 
    redirect, url_for, flash)
from logbook.log.models import User, Tag, Log
from logbook.extensions import db

log = Blueprint('log', __name__)

@log.route('/')
def index():
    logs = Log.query.order_by(Log.create_date.desc())
    return render_template("index.html", logs=logs)

@log.route('/new/', methods=['GET','POST'])
def new_log():
    if request.method == 'POST':
        print "in POST"
        newlog = Log(subject=request.form['subject'],
                     link=request.form['link'],
                     notes=request.form['notes'],
                     user_id=1)  #TODO: get user_id from session
        
        # process tags
        tags = request.form['tag'].split(',')

        for t in tags:
            print t
            tag = Tag.query.filter_by(name=t.lower()).first()
            if tag:
                newlog.tag.append(tag)
            else:
                tag = Tag(name=t.lower())
                newlog.tag.append(tag)
        db.session.add(newlog)
        db.session.commit()
        return redirect(url_for('log.index'))
    else:
        return render_template("log/newlog.html")

@log.route('/<int:log_id>/edit/')
def edit_log(log_id):
    return "This page edits a log entry."

@log.route('/<int:log_id>/delete')
def delete_log(log_id):
    return "This page deletes a log entry."

@log.route('/tag/<tagname>')
def show_tag(tagname):
    return "This page shows all entries with %s." % tagname