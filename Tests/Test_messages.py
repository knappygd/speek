import unittest

class TestMessage(unittest.TestCase):
    """Test the class Message"""
    def Test_Message_Id(self):
        msg = Message()
        self.assertTrue(hasattr(msg,"id"))
        self.assertEqual(msg.id, None)

    def Test_Message_content(self):
        msg = Message()
        self.assertTrue(hasattr(msg,"content"))
        self.assertEqual(msg.content, None)