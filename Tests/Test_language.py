import unittest

class Test_language(unittest.TestCase):
    """Test the class Language"""
    def Test_Language_Id(self):
        """test if the id exists an is created correctly as an uuid"""

    def Test_language_language(self):
        lan = Language()
        self.assertTrue(hasattr(lan,"language"))
        self.assertEqual(lan.language, None)
