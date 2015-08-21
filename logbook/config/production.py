# production.py
"""
    logbook.config.production
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    This is logbook's production config.
"""

from logbook.config.default import DefaultConfig

class ProductionConfig(DefaultConfig):

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://logbook:tiger@localhost/logbook"