"""
    logbook.log.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the log entries creation and viewing.

"""

from flask import (current_app, Blueprint, render_template, request, 
    redirect, url_for, flash)
from logbook.log.models import User, Tag, Log
from logbook.extensions import db
from datetime import datetime

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
        newlog.set_tags(request.form['tag'])
        newlog.save()

        return redirect(url_for('log.index'))
    else:
        return render_template("log/newlog.html")

@log.route('/<int:log_id>/edit/', methods=['GET','POST'])
def edit_log(log_id):
    log = Log.query.get(log_id)
    if request.method == 'POST':
        if request.form['subject']:
            log.subject = request.form['subject']
        if request.form['link']:
            log.link = request.form['link']
        if request.form['notes']:
            log.notes = request.form['notes']
        if request.form['tag']:
            log.set_tags(request.form['tag'])
            
        log.update_date = datetime.now()
        log.save()

        flash("Log edited.")
        return redirect(url_for('log.index'))
    else:
        return render_template("log/editlog.html", log=log)

@log.route('/<int:log_id>/delete', methods=['GET','POST'])
def delete_log(log_id):
    log = Log.query.get(log_id)
    if request.method == 'POST':
        if log:
            log.delete()
            flash("Log deleted")
            return redirect(url_for('log.index'))
    else:
        return render_template('log/deletelog.html', log=log)

    return "This page deletes a log entry."

@log.route('/tag/<tagname>')
def show_tag(tagname):
    logs = Log.query.filter(Log.tag.any(name=tagname)).all()
    return render_template("index.html", logs=logs)
    return "This page shows all entries with %s." % tagname