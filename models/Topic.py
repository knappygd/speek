#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Topic():
    """Creation of the class Topic"""
    __tablename__ = 'topic'
    topic_id = Column(Integer, primary_key=True)
    topic = Column(String(128), primary_key=True)
    
