import unittest

class TestChat(unittest.TestCase):
    """test if the id exists an is created correctly as an uuid"""
    def Test_Chat_Id(self):
        chat = Chat()
        self.assertTrue(hasattr(chat,"id"))
        self.assertEqual(chat.id, None)        
