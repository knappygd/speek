#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Messages():
    """Creation of the class Message"""
    __tablename__ = 'messages'
    id = Column(String(60), primary_key=True)
    Content = Column(String(1024))
    send_at = Column(DateTime, default=datetime.utcnow)
    