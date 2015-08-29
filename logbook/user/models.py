"""
    logbook.user.models
    ~~~~~~~~~~~~~~~~~~~

    This file provides models for users
"""

from logbook.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250))
    picture = db.Column(db.String(250))
    registered_on = db.Column(db.DateTime)


    def __init__(self, name, email, password, picture):
        self.name = name
        self.email = email
        self.password = password
        self.picture = picture
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.name

    def check_password(self, password):
        """Check passwords. If passwords match it returns true, else false."""
        if self.password is None:
            return False
        if self.password == password:
            return True
        else:
            return False

    @classmethod
    def authenticate(cls, login, password):
        """A classmethod for authenticating users"""

        user = cls.query.filter_by(email=login).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    def save(self):
        """Save user object into database"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete log object from database"""
        db.session.delete(self)
        db.session.commit()
        return self      