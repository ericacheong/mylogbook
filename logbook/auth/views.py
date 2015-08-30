"""
    logbook.auth.views
    ~~~~~~~~~~~~~~~~~~
    This module provides views for user login, logout and remember me.
"""

from flask import (Blueprint, render_template, request, redirect,
    url_for, flash, abort)
from logbook.auth.forms import (LoginForm, RegisterForm, ForgotPasswordForm, 
    ResetPasswordForm)
from logbook.user.models import User
from flask.ext.login import (login_user, login_required, logout_user, 
    current_user)
from logbook.email import send_reset_token, send_registration_token

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
            login_user(user, remember=form.remember_me.data)
            # TODO: Redirect doesn't work. Need to check next
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
        token = user.make_token(op="register")
        send_registration_token(user, token=token)
        flash("Email sent! Please check your inbox.", "info")
        # login_user(user)
        # flash("Thank you for registering.", "success")
        return redirect(url_for("log.index"))
    return render_template("auth/register.html", form=form)
   
@auth.route("/activateaccount/<email>/<token>")
def activate_account(email,token):
    """
    Handles the register account process.
    """
    if not current_user.is_anonymous():
        return redirect(url_for("log.index"))

    user = User.query.filter_by(email=email).first()
    expired, invalid, data = user.verify_registration_token(token)

    if invalid:
        flash("Your account activation link is invalid.", "danger")
        return redirect(url_for("auth.register"))

    if expired:
        flash("Your account activation link has expired.", "danger")
        return redirect(url_for("auth.register"))

    if user and data:
        user.verified = True
        user.save()
        login_user(user)
        flash("Your account is now activated.", "success")
        return redirect(url_for("log.show_log"))

@auth.route('/resetpassword', methods=["GET", "POST"])
def forgot_password():
    """
    Sends a reset password token to the user.
    """

    if not current_user.is_anonymous():
        return redirect(url_for("log.index"))

    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            token = user.make_token(op="reset")
            send_reset_token(user, token=token)

            flash("E-Mail sent! Please check your inbox.", "info")
            return redirect(url_for("auth.forgot_password"))
        else:
            flash("You have entered a Username or E-Mail Address that is "
                    "not linked with your account.", "danger")
    return render_template("auth/forgot_password.html", form=form)


@auth.route("/resetpassword/<token>", methods=["GET", "POST"])
def reset_password(token):
    """
    Handles the reset password process.
    """

    if not current_user.is_anonymous():
        return redirect(url_for("log.index"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        expired, invalid, data = user.verify_reset_token(form.token.data)

        if invalid:
            flash("Your Password Token is invalid.", "danger")
            return redirect(url_for("auth.forgot_password"))

        if expired:
            flash("Your Password Token is expired.", "danger")
            return redirect(url_for("auth.forgot_password"))

        if user and data:
            user.password = form.password.data
            user.save()
            flash("Your Password has been updated.", "success")
            return redirect(url_for("auth.login"))

    form.token.data = token
    return render_template("auth/reset_password.html", form=form)