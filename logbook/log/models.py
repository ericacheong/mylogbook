# models.py

from sqlalchemy import Table, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from config.development import DB_URI

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250), nullable=False, unique=True)
    picture = Column(String(250))

log_tag_table = Table('log_tag', Base.metadata,
    Column('tag_id', Integer, ForeignKey('tag.id')),
    Column('log_id', Integer, ForeignKey('log.id'))
)

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    subject = Column(String(250))
    link = Column(String(250))
    notes = Column(String)
    tag = relationship("Tag", secondary=log_tag_table,
                    backref="logs")
    create_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

# DB_URI = 'sqlite:////vagrant/logbook/db/logbook.db'
engine = create_engine(DB_URI)

Base.metadata.create_all(engine)