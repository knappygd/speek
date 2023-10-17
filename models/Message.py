#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime

class Messages():
    """Creation of the class Message"""
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True)
    content = Column(String(1024))
    sent_at = Column(DateTime, default=datetime.utcnow)
    