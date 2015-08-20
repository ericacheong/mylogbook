# seeddata.py

# from logbook.logbook import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Tag, Log, User
import datetime
# from logbook import app
from config.development import DB_URI

engine = create_engine(DB_URI)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

users = [
    ['Daniel Crockford', 'dcrockford@example.com', ''],
    ['Marie Singer', 'marie@example.com', '']
]

for u in users:
    name, email, pic = u
    user = User(name=name, email=email, picture=pic)
    session.add(user)
    session.commit()

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
    session.add(log)
    session.commit()

