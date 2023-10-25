#!/usr/bin/python3
import unittest
from models import Message
from models import Chat
from models import User


class TestMessage(unittest.TestCase):
    """Test the class Message"""

    def Test_send_message(self):
        """this will test the method of send a message which Sends a message"""
        leo = User.search_user("LR17")
        Mishel = User.search_user("GODD")
        Chit = Chat.create_chat(leo.id, Mishel.id)
        msg = Message.SendMessage(Chit, leo, Mishel, "Hi")
        self.assertEqual(msg.content, "Hi")
