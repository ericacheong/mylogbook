"""
    logbook.log.views
    ~~~~~~~~~~~~~~~~~~
    This module handles the log entries creation and viewing.

"""

from flask import (current_app, Blueprint, render_template, request, 
    redirect, url_for, flash, abort)
from logbook.log.models import Tag, Log
from logbook.user.models import User
from logbook.extensions import db, login_manager
from logbook.log.forms import NewLogForm
from datetime import datetime
from flask.ext.login import login_required, current_user

log = Blueprint('log', __name__)

@log.route('/')
def index():
    # logs = Log.query.order_by(Log.create_date.desc())
    # if current_user is not None and current_user.is_authenticated():
    #     logs = Log.query.filter_by(user_id=current_user.id).order_by(Log.create_date.desc())
    return render_template("index.html")

@log.route('/log/')
@login_required
def show_log():
    logs = Log.query.filter_by(user_id=current_user.id).order_by(Log.create_date.desc())
    return render_template("log/showlog.html", logs=logs)

@log.route('/new/', methods=['GET','POST'])
@login_required
def new_log():
    form = NewLogForm()
    
    if form.validate_on_submit():
        newlog = Log(subject=form.subject.data,
                     link=form.link.data,
                     notes=form.notes.data,
                     user_id=current_user.id)
        newlog.set_tags(form.tag.data)
        newlog.save()
        return redirect(url_for('log.index'))

    else:
        return render_template("log/newlog.html", form=form)

@log.route('/<int:log_id>/edit/', methods=['GET','POST'])
@login_required
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
            print request.form['tag']
            
        log.update_date = datetime.now()
        log.save()

        flash("Log edited.")
        return redirect(url_for('log.show_log'))
    else:
        return render_template("log/editlog.html", log=log)

@log.route('/<int:log_id>/delete/', methods=['GET','POST'])
@login_required
def delete_log(log_id):
    log = Log.query.get(log_id)
    if request.method == 'POST':
        if log:
            log.delete()
            flash("Log deleted")
            return redirect(url_for('log.show_log'))
    else:
        return render_template('log/deletelog.html', log=log)

    return "This page deletes a log entry."

@log.route('/tag/<tagname>/')
@login_required
def show_tag(tagname):
    logs = Log.query.filter((Log.tag.any(name=tagname)))\
        .filter(Log.user_id==current_user.id).order_by(Log.create_date.desc()).all()
    return render_template("log/showlog.html", logs=logs)
    # return "This page shows all entries with %s." % tagname
