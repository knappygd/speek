import unittest
from datetime import datetime
import time
from models import User


class TestUser(unittest.TestCase):
    """Test the class User"""

    def Test_user_id(self):
        """test if the id exists an is created correctly as an uuid"""
        inst1 = User()
        inst2 = User()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

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
        leo = User.CreateUser("Leo", "password", "email@gmail.com",
                              "picture", "Uruguay", "Hi i am using speak")
        User.modifyUser(leo, "pass", "l@gmail.com", "pic", "Uru", "Hi")
        self.assertEqual(leo.username, "Leo")
        self.assertEqual(leo.password, "pass")
        self.assertEqual(leo.email, "l@gmail.com")
        self.assertEqual(leo.picture, "pic")
        self.assertEqual(leo.country, "Uru")
        self.assertEqual(leo.description, "Hi")

    def Test_user_delete(self):
        """This will test the function to delete a user"""
        leo = User.CreateUser("Leo", "password", "email@gmail.com",
                              "picture", "Uruguay", "Hi i am using speak")
        User.DeleteUser(leo)
        self.assertEqual(leo.username, "Leo")

    def Test_look_for_random(self):
        """this test the method of pair people in random"""
        user = User.lookRandom()
        self.assertTrue(hasattr(user, "username"))

    def Test_list_Friend(self):
        """Test that the list of friends works"""

    def Test_add_Friend(self):
        """Test the add the list of freinds"""

    def Test_search_user(self):
        """Test the function to search for a user
        by the username"""
