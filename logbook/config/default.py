# default.py
"""
    logbook.config.default
    ~~~~~~~~~~~~~~~~~~~~~~

    Default configuration for logbook.
    You can override these configuration variables in another class.

"""

import os

class DefaultConfig(object):

    DEBUG = False
    TESTING = False
    # Security
    # This is the secret key that is used for session signing.
    SECRET_KEY = 'secret key'

    # URL Prefixes
    LOG_URL_PREFIX = ""
    ADMIN_URL_PREFIX = "/admin"
    USER_URL_PREFIX = "/user"
    AUTH_URL_PREFIX = "/auth"

    # Auth
    LOGIN_VIEW = "auth.login"

    ## Mail
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_SSL = False
    MAIL_USE_TLS = False
    MAIL_USERNAME = "noreply@example.org"
    MAIL_PASSWORD = ""
    MAIL_DEFAULT_SENDER = ("Default Sender", "noreply@example.org")
    # Where to logger should send the emails to
    ADMINS = ["admin@example.org"]
