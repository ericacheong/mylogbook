# development.py
"""
    logbook.config.development
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This is logbook's development config.
"""

from logbook.config.default import DefaultConfig

class DevelopmentConfig(DefaultConfig):

    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:////vagrant/logbook/logbook/db/logbook.db'

    # Security
    SECRET_KEY = "SuperSecretKeyForSession"

    # Mail
    # Local SMTP Server
    #MAIL_SERVER = "localhost"
    #MAIL_PORT = 25
    #MAIL_USE_SSL = False
    #MAIL_USERNAME = ""
    #MAIL_PASSWORD = ""
    #MAIL_DEFAULT_SENDER = "noreply@example.org"

    # Google Mail Example
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "topher.lab@gmail.com"
    MAIL_PASSWORD = "alwaysking"
    MAIL_DEFAULT_SENDER = ("Topher Lab", "topher.lab@gmail.com")