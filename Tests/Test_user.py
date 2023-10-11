import unittest

class TestUser(unittest.TestCase):
    """Test the class User"""
    def Test_User_Id(self):
        """test if the id exists an is created correctly as an uuid"""


    def Test_User_Name(self):
        """Checks if the user has the username
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user,"username"))
        self.assertEqual(user.username, None)

    def Test_User_Password(self):
        """Checks if the user has the password
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user,"password"))
        self.assertEqual(user.password, None)

    def Test_User_Email(self):
        """Checks if the user has the email
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user,"email"))
        self.assertEqual(user.Email, None)

    def Test_User_status(self):
        """Checks if the user has the status
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user,"status"))
        self.assertEqual(user.status, None)

    def Test_User_profile_picture(self):
        """Checks if the user has the pfp
        attribute and is able to create it"""
        user = User()
        self.assertTrue(hasattr(user,"pfp"))
        self.assertEqual(user.pfp, None)

    def Test_User_created_at(self):
        """Checks if the user has the created_at
        attribute and is able to create it with
        the actual time"""

    def Test_user_updated_at(self):
        """Checks if the user has the updated_at
        attribute and is able to create it with a
        few miliseconds of difference with created_At"""
