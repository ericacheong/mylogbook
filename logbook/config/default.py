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
