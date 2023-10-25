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

    def Test_user_user_name(self):
        """Checks if the user has the username
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user, "username"))
        self.assertEqual(user.username, None)

    def Test_user_password(self):
        """Checks if the user has the password
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, None)

    def Test_user_email(self):
        """Checks if the user has the email
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.Email, None)

    def Test_user_status(self):
        """Checks if the user has the status
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user, "status"))
        self.assertEqual(user.status, None)

    def Test_user_profile_picture(self):
        """Checks if the user has the pfp
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user, "pfp"))
        self.assertEqual(user.pfp, None)

    def Test_user_updated_at(self):
        """Checks if the user has the updated_at
        attribute and is able to create it with a
        few miliseconds of difference with created_At"""
        tic = datetime.now()
        inst1 = User()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = User()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def Test_user_creation(self):
        """This is a function that will test the creation of a user"""
        leo = User.CreateUser("Leo", "password", "email@gmail.com",
                              "picture", "Uruguay", "Hi i am using speak")
        self.assertEqual(leo.username, "Leo")
        self.assertEqual(leo.password, "password")
        self.assertEqual(leo.email, "email@gmail.com")
        self.assertEqual(leo.picture, "picture")
        self.assertEqual(leo.country, "Uruguay")
        self.assertEqual(leo.description, "Hi i am using speak")

    def Test_user_mod(self):
        """This will test if the function of modify a user works"""
        leo = User.search_user("LR17")
        User.modifyUser(leo, "password", "Contraseña")
        self.assertEqual(leo.password, "Contraseña")

    def Test_user_delete(self):
        """This will test the function to delete a user"""
        leo = User.search_user("LR17")
        User.self_delete(leo.username)
        self.assertNotEqual(leo.username, "Leo")

    def Test_look_for_random(self):
        """this test the method of pair people in a random chat"""
        user = User.lookRandom()
        self.assertTrue(hasattr(user, "username"))

    def Test_list_Friend(self):
        """Test if the list of friends works"""
        leo = User.search_user("LR17")
        lista = User.list_friends(leo.id)
        self.assertTrue(isinstance(lista, dict))

    def Test_add_Friend(self):
        """Test if the add freind works"""
        leo = User.search_user("LR17")
        User.invite(leo, "Mishel")
        lista = User.list_friends(leo.id)
        size1 = len(lista)
        User.invite(leo, "Diego")
        lista = User.list_friends(leo.id)
        size2 = len(lista)
        self.assertNotEquals(size1, size2)

    def Test_login(self):
        """Test if the method login can find a user"""
        use = User.login("email@gmail.com", "password")
        self.assertEqual(use.username, "leo")

    def Test_delete_friend(self):
        """a test to check if a freind is removed of the friend lists"""
        leo = User.search_user("LR17")
        User.invite(leo, "Mishel")
        User.invite(leo, "Diego")
        lista = User.list_friends()
        size1 = len(lista)
        User.remove_friend("Diego")
        lista = User.list_friends()
        size2 = len(lista)
        self.assertNotEquals(size1, size2)
