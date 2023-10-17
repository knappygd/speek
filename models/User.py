#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime

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

    