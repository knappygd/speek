#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime


user_messages = Table('user_messages', Base.metadata,
                        Column('user_id', String(60),
                                ForeignKey('User.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                                primary_key=True),
                          Column('message_id', String(60),
                                ForeignKey('Message.message_id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))

class Messages():
    """Creation of the class Message"""
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True)
    content = Column(String(1024))
    sent_at = Column(DateTime, default=datetime.utcnow)

    usu = relationship("User",
                            secondary=user_messages,
                            viewonly=False)
