#!/usr/bin/python3
import unittest
from datetime import datetime
import time
from models import User


class TestUser(unittest.TestCase):
    """Test the User"""

    def Test_search_user(self):
        """Test the function to search for a user
        by the special id"""
        leo = User.search_user("LR17")
        self.assertEqual(leo.username, "Leo")

    def Test_user_creation(self):
        """This is a function that will test the creation of a user"""
        User.CreateUser({"username":"Leo","password": "password","email": "email@gmail.com",
                              "pfp":"picture", "country": "Uruguay", "description": "Hi i am using speak", "specialid": "LR17"})
        user = User.search_user("LR17")
        self.assertEqual(user.email, "email@gmail.com")
        self.assertEqual(user.password, "password")

    def Test_user_mod(self):
        """This will test if the function of modify a user works"""
        user = User.search_user("LR17")
        User.modifyUser(user, {"password": "Contraseña"})
        user = User.search_user("LR17")
        self.assertEqual(user.password, "Contraseña")

    def Test_user_delete(self):
        """This will test the function to delete a user"""
        user = User.search_user("LR17")
        User.self_delete(user.username)
        user = User.search_user("LR17")
        self.assertEqual(user, None)

    def Test_look_for_random(self):
        """this test the method of pair people in a random chat"""
        user = User.lookRandom()
        self.assertTrue(hasattr(user, "username"))

    def Test_list_Friend(self):
        """Test if the list of friends works"""
        user = User.search_user("LR17")
        lista = User.list_friends(user.id)
        self.assertTrue(isinstance(lista, dict))

    def Test_add_Friend(self):
        """Test if the add freind works"""
        user1 = User.search_user("LR17")
        user2 = User.search_user("Godd")
        user3 = User.search_user("Coca")
        User.invite(user1, user2)
        lista = User.list_friends(user1.id)
        size1 = len(lista)
        User.invite(user1, user3)
        lista = User.list_friends(user1.id)
        size2 = len(lista)
        self.assertNotEquals(size1, size2)

    def Test_login(self):
        """Test if the method login can find a user"""
        use = User.login("email@gmail.com", "password")
        self.assertEqual(use.username, "leo")

    def Test_delete_friend(self):
        """a test to check if a freind is removed of the friend lists"""
        user1 = User.search_user("LR17")
        user2 = User.search_user("Godd")
        user3 = User.search_user("Coca")
        User.invite(user1, user2)
        User.invite(user1, user3)
        lista = User.list_friends()
        size1 = len(lista)
        User.remove_friend(user3)
        lista = User.list_friends()
        size2 = len(lista)
        self.assertNotEquals(size1, size2)
