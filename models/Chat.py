#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Chat():
    """Creation of the class Chat"""
    __tablename__ = 'chat'
    chat_id = Column(String(60), primary_key=True)
    