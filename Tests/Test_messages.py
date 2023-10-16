import unittest
from models import Message
from models import Chat
from models import User
class TestMessage(unittest.TestCase):
    """Test the class Message"""
    def Test_message_id(self):
        msg = Message()
        self.assertTrue(hasattr(msg,"id"))
        self.assertEqual(msg.id, None)

    def Test_message_content(self):
        msg = Message()
        self.assertTrue(hasattr(msg,"content"))
        self.assertEqual(msg.content, None)

    def Test_send_message(self):
        """this will test the method of send a message which Sends a message"""
        """this test is for the creation of the chat"""
        leo = User.CreateUser("Leo", "password", "email@gmail.com",
                              "picture", "Uruguay", "Hi i am using speak")
        Mishel = User.CreateUser("Mishi", "pass", "mail@gmail.com", "pic", "Uruguay", "GODDDDDDDDDDD")
        Chit = Chat.StartChat(leo, Mishel)
        msg = Message.SendMessage(Chit, leo, Mishel, "Hi")
        self.assertEqual(msg.content, "Hi")

