"""
    logbook.extensions
    ~~~~~~~~~~~~~~~~~~

    Extensions used by logbook
"""

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

# Database
db = SQLAlchemy()

# Login
login_manager = LoginManager()

# Migrations
migrate = Migrate()

# CSRF
csrf = CsrfProtect()