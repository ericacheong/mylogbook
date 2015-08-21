
"""
    logbook.manage
    ~~~~~~~~~~~~~~
    This script uses Flask-Script to provide commands for creating
    the database with or without sample content.
    Run the development server with 'python manage.py runserver'
    You can run 'python manage.py' to see full list of commands.

"""

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand

from logbook import create_app
from logbook.utils.seeddata import load_seed_data
# Use the development configuration if available
try:
    from logbook.config.development import DevelopmentConfig as Config
except ImportError:
    from logbook.config.default import DefaultConfig as Config

app = create_app(Config)
manager = Manager(app)

# Run local server
manager.add_command("runserver", Server(host="0.0.0.0", port=8000))

# Migration commands
manager.add_command('db', MigrateCommand)

@manager.command
def populate():
    """Creates the database with default data."""
    load_seed_data()


if __name__ == "__main__":
    manager.run()