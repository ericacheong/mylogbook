"""
    logbook.user.models
    ~~~~~~~~~~~~~~~~~~~

    This file provides models for users
"""
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from logbook.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False, unique=True)
    _password = db.Column('password',db.String(250), nullable=False)
    picture = db.Column(db.String(250))
    registered_on = db.Column(db.DateTime)
    lastseen = db.Column(db.DateTime, default=datetime.utcnow())

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

    def _get_password(self):
        """Returns the hashed password"""
        return self._password

    def _set_password(self, password):
        """Generates a password hash for the provided password"""
        self._password = generate_password_hash(password)

    # Hide password encryption by exposing password field only
    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                               _set_password))

    def check_password(self, password):
        """Check passwords. If passwords match it returns true, else false."""
        if self.password is None:
            return False
        return check_password_hash(self.password, password)
        # if self.password == password:
        #     return True
        # else:
        #     return False

    @classmethod
    def authenticate(cls, login, password):
        """A classmethod for authenticating users"""

        user = cls.query.filter_by(email=login).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    def _make_token(self, data, timeout):
        s = Serializer(current_app.config['SECRET_KEY'], timeout)
        return s.dumps(data)

    def _verify_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        data = None
        expired, invalid = False, False
        try:
            data = s.loads(token)
        except SignatureExpired:
            expired = True
        except Exception:
            invalid = True
        return expired, invalid, data

    def make_reset_token(self, expiration=3600):
        """Creates a reset token. The duration can be configured through the
        expiration parameter.

        :param expiration: The time in seconds how long the token is valid.
        """
        return self._make_token({'id': self.id, 'op': 'reset'}, expiration)

    def verify_reset_token(self, token):
        """Verifies a reset token. It returns three boolean values based on
        the state of the token (expired, invalid, data)

        :param token: The reset token that should be checked.
        """

        expired, invalid, data = self._verify_token(token)
        if data and data.get('id') == self.id and data.get('op') == 'reset':
            data = True
        else:
            data = False
        return expired, invalid, data

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