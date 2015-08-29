# models.py
"""
    logbook.log.models
    ~~~~~~~~~~~~~~~~~~

    This file provides models for logbook
"""

from logbook.extensions import db
from datetime import datetime

from logbook.user.models import User

tag_log_tbl = db.Table('tag_log_tbl',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.name

    def save(self):
        """Save the tag to database"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete tag object from database"""
        db.session.delete(self)
        db.session.commit()
        return self

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(250))
    link = db.Column(db.String(250))
    notes = db.Column(db.String)
    tag = db.relationship("Tag", secondary=tag_log_tbl,
                    backref=db.backref('log', lazy='dynamic'))
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship(User)


    def get_tags(self):
        """Return tag as string seperated by comma"""
        output = []
        for t in self.tag:
            output.append(t.name)
            print t.name
        return ','.join(output)

    def set_tags(self, tags):
        """Set log tags from a list of string tags"""
        self.tag = []
        tag_list = tags.split(',')
        
        for tag in tag_list:
            tag = " ".join(tag.split())
            print "inside set_tags %s" % tag
            t_obj = Tag.query.filter_by(name=tag).first()
            if t_obj is None:
                # add tag to log
                t = Tag(name=tag.lower())
                t.save()
                self.tag.append(t)
            else:
                # check if tag is already in log list
                if not t_obj in self.tag:
                    self.tag.append(t_obj)
        return self

    def save(self):
        """Save log object into database"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete log object from database"""
        db.session.delete(self)
        db.session.commit()
        return self