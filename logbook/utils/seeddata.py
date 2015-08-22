# seeddata.py
"""
    logbook.fixtures.seeddata
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Initial data for logbook

"""

from logbook.app import create_app
from logbook.extensions import db
from logbook.log.models import User, Tag, Log
from random import sample
   
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

    tags = ['sql','python','programming']

    for t in tags:
        tag = Tag(name=t)
        db.session.add(tag)
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
        t_ids = sample([1,2,3], 2)
        for t in t_ids:
            tag = Tag.query.get(t)
            log.tag.append(tag)
        db.session.add(log)
        db.session.commit()


