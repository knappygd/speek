import unittest
from models import Language

class Test_language(unittest.TestCase):
    """Test the class Language"""
    def Test_language_id(self):
        """test if the id exists an is created correctly as an uuid"""
        inst1 = Language()
        inst2 = Language()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def Test_language_language(self):
        lan = Language()
        self.assertTrue(hasattr(lan,"language"))
        self.assertEqual(lan.language, None)
