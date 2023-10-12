import unittest
from models import Message

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
        """this will test the method of send a message which creates a message"""
