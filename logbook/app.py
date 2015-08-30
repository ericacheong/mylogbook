"""
    logbook.app
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mangages the app creation and configuraiton process

"""

from flask import Flask
from logbook.log.views import log
from logbook.admin.views import admin
from logbook.user.views import user
from logbook.auth.views import auth
from logbook.user.models import User
from flask_bootstrap import Bootstrap
# extensions
from logbook.extensions import db, login_manager, csrf, migrate

def create_app(config=None):
    """Creates the app."""

    app = Flask("logbook")
    
    app.config.from_object('logbook.config.default.DefaultConfig')

    app.config.from_object(config)
    # TODO: set up settings
    app.config.from_envvar("LOGBOOK_SETTINGS", silent=True)

    configure_blueprints(app)
    configure_extensions(app)

    return app


def configure_blueprints(app):
    app.register_blueprint(log, url_prefix=app.config["LOG_URL_PREFIX"])
    app.register_blueprint(admin, url_prefix=app.config["ADMIN_URL_PREFIX"])
    app.register_blueprint(user, url_prefix=app.config["USER_URL_PREFIX"])
    app.register_blueprint(auth, url_prefix=app.config["AUTH_URL_PREFIX"])

def configure_extensions(app):
    """Configure the extensions."""

    # Flask-SQLAlchemy
    db.init_app(app)
    with app.test_request_context():
        from log.models import User, Tag, Log
        db.create_all()

    # Bootstrap
    Bootstrap(app)

    # Flask-Login
    login_manager.login_view = app.config["LOGIN_VIEW"]

    @login_manager.user_loader
    def load_user(userid):
        """Loads the user. Required by the 'login' extension."""
        return User.query.get(userid)

    login_manager.init_app(app)


    # Flask-WTF CSRF
    csrf.init_app(app)
