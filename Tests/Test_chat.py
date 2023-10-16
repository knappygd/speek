import unittest
from models import Chat
from models import User

class TestChat(unittest.TestCase):
    """test if the id exists an is created correctly as an uuid"""
    def Test_chat_id(self):
        inst1 = Chat()
        inst2 = Chat()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def Test_start_chat(self):
        """this test is for the creation of the chat"""
        leo = User.CreateUser("Leo", "password", "email@gmail.com",
                              "picture", "Uruguay", "Hi i am using speak")
        Mishel = User.CreateUser("Mishi", "pass", "mail@gmail.com", "pic", "Uruguay", "GODDDDDDDDDDD")
        Chit = Chat.StartChat(leo, Mishel)
        self.assertTrue(Chit.User1 == "Leo" or Chit.User1 == "Mishel")
