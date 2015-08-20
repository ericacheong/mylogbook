# development.py
"""
    logbook.config.development
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This is logbook's development config.
"""

from logbook.config.default import DefaultConfig

class DevelopmentConfig(DefaultConfig):

    DEBUG = True
    
    SQLALCHEMY_DB_URI = 'sqlite:////vagrant/logbook/db/logbook.db'

    # Security
    SECRET_KEY = "SuperSecretKeyForSession"