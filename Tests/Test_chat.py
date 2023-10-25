#!/usr/bin/python3
import unittest
from models import Chat
from models import User


class TestChat(unittest.TestCase):
    """test if the id exists an is created correctly as an uuid"""

    def Test_start_chat(self):
        """this test is for the creation of the chat"""
        leo = User.search_user("LR17")
        Mishel = User.search_user("GODD")
        Chit = Chat.create_chat(leo.id, Mishel.id)
        self.assertTrue(Chit.User1 == "Leo" or Chit.User1 == "Mishel")

    def Test_delete_chat(self):
        """this test will test if we can delete the chat"""
        leo = User.search_user("LR17")
        Mishel = User.search_user("GODD")
        Chit = Chat.create_chat(leo, Mishel)
        Chat.delete_chat(Chit.id)
        self.assertEquals(Chat.search_chat(Chit.chat_id), None)

    def Test_search_chat(self):
        """this test will test if we can search for a chat"""
        leo = User.search_user("LR17")
        Mishel = User.search_user("GODD")
        Chit = Chat.create_chat(leo, Mishel)
        self.assertNotEquals(Chit, None)
