"""
    logbook.extensions
    ~~~~~~~~~~~~~~~~~~

    Extensions used by logbook
"""

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

# Database
db = SQLAlchemy()

# Migrations
migrate = Migrate()