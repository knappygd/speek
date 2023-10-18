#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Language():
    """Creation of the class Language"""
    __tablename__ = 'languages'
    id = Column(String(60), primary_key=True)
    language = Column(String(128))
    
    