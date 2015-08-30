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

    
    ## Mail
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
    MAIL_USERNAME = "your_username@gmail.com"
    MAIL_PASSWORD = "your_password"
    MAIL_DEFAULT_SENDER = ("Your Name", "your_username@gmail.com")