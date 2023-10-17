#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

speeks = Table('speaks', Base.metadata,
               Column('User_id', String(60),
                      ForeignKey('User.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True),
               Column('Lang_id', String(60),
                      ForeignKey('Language.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True))


class User():
    """Creation of the class User"""
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    pfp = Column(String(128), nullable=False)
    status = Column(Integer(128), nullable=False)
    country = Column(String(64), nullable=False)
    desc = Column(String(1024))
    chats = relationship("Chat",
                         backref="chat",
                         cascade="all, delete, delete-orphan")
    msg = relationship("Message",
                       backref="messages",
                       cascade="all, delete, delete-orphan")
    lan = relationship("Language",
                       backref="languages",
                       cascade="all, delete, delete-orphan")
