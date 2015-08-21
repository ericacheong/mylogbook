# models.py
"""
    logbook.log.models
    ~~~~~~~~~~~~~~~~~~

    This file provides models for logbook
"""

from logbook.extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False, unique=True)
    picture = db.Column(db.String(250))

    def __init__(self, name, email, picture):
        self.name = name
        self.email = email
        self.picture = picture

    def __repr__(self):
        return '<User %r>' % self.name

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(250))
    link = db.Column(db.String(250))
    notes = db.Column(db.String)
    tag = db.relationship("Tag", secondary=tags,
                    backref=db.backref('logs', lazy='dynamic'))
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
