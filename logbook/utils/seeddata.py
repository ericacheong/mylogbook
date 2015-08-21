# seeddata.py
"""
    logbook.fixtures.seeddata
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Initial data for logbook

"""

from logbook.app import create_app
from logbook.extensions import db
from logbook.log.models import User, Tag, Log
# from logbook.config.development import DevelopmentConfig as Config
   
def load_seed_data():
    users = [
        ['Daniel Crockford', 'dcrockford@example.com', ''],
        ['Marie Singer', 'marie@example.com', '']
    ]

    for u in users:
        name, email, pic = u
        user = User(name=name, email=email, picture=pic)
        db.session.add(user)
        db.session.commit()

    logs = [
        ["sqlalchemy ORM tutorial", 
        "http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#building-a-relationship",
        "ORM is built on top of expression language.",
        1],
        ["Python tutorial - looping",
        "https://docs.python.org/2/tutorial/datastructures.html#looping-techniques",
        "",
        2]
    ]

    for l in logs:
        subject, link, notes, user_id = l
        log = Log(subject=subject, link=link, notes=notes, user_id=user_id)
        db.session.add(log)
        db.session.commit()


