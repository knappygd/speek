#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Chat():
    """Creation of the class Chat"""
    __tablename__ = 'chat'
    chat_id = Column(String(60), primary_key=True)
    topic_id = Column(String(60), ForeignKey('topic.topic_id'), nullable=False)
