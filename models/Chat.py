#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Chat():
    """Creation of the class Chat"""
    __tablename__ = 'chat'
    id = Column(String(60), primary_key=True)
    