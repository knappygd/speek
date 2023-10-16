#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Topic():
    """Creation of the class Topic"""
    __tablename__ = 'topic'
    id = Column(String(60), primary_key=True)
    topic = Column(String(128), primary_key=True)

    