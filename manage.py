
"""
    logbook.manage
    ~~~~~~~~~~~~~~
    This script uses Flask-Script to provide commands for creating
    the database with or without sample content.
    Run the development server with 'python manage.py runserver'
    You can run 'python manage.py' to see full list of commands.

"""

from flask.ext.script import Manager, Server

from logbook import create_app

# Use the development configuration if available
try:
    from logbook.config.development import DevelopmentConfig as Config
except ImportError:
    from logbook.config.default import DefaultConfig as Config

app = create_app(Config)
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=8000))

if __name__ == "__main__":
    manager.run()