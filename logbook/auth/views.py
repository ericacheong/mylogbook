"""
    logbook.auth.views
    ~~~~~~~~~~~~~~~~~~
    This module provides views for user login, logout and remember me.
"""

from flask import (Blueprint, render_template, request, redirect,
    url_for, flash, abort)
from logbook.auth.forms import LoginForm, RegisterForm
from logbook.user.models import User
from flask.ext.login import (login_user, login_required, logout_user, 
    current_user)

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET','POST'])
def login():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for("log.show_log"))

    form = LoginForm()
   
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.email.data, 
            form.password.data)
        if user and authenticated:
            login_user(user)
            # TODO: Redirect doesn't work
            return redirect(request.args.get("next") or url_for('log.show_log'))
        flash("Wrong email or password.", "danger")
        
    return render_template("auth/login.html", form=form)

# def next_is_valid(next):
#     pass

@auth.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('log.index')) 

@auth.route('/register/', methods=['GET','POST'])
def register():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for("log.show_log"))

    form = RegisterForm(request.form)

    if form.validate_on_submit():
        user = form.save()
        # user = User.query.filter_by(id=user_id)
        login_user(user)
        flash("Thank you for registering.", "success")
        return redirect(url_for("log.show_log"))
    return render_template("auth/register.html", form=form)
    # return "This is a sign up page."