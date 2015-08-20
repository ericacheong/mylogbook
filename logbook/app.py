"""
    logbook.app
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mangages the app creation and configuraiton process

"""
from flask import Flask
from logbook.log.views import log
from logbook.admin.views import admin
from logbook.user.views import user

def create_app(config=None):
    """Creates the app."""

    app = Flask("logbook")
    
    app.config.from_object('logbook.config.default.DefaultConfig')

    app.config.from_object(config)
    # TODO: set up settings
    app.config.from_envvar("LOGBOOK_SETTINGS", silent=True)

    configure_blueprints(app)

    return app


def configure_blueprints(app):
    app.register_blueprint(log, url_prefix=app.config["LOG_URL_PREFIX"])
    app.register_blueprint(admin, url_prefix=app.config["ADMIN_URL_PREFIX"])
    app.register_blueprint(user, url_prefix=app.config["USER_URL_PREFIX"])