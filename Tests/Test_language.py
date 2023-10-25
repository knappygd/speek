#!/usr/bin/python3
import unittest
from models import Language
from models import User


class Test_language(unittest.TestCase):
    """Test the class Language"""

    def Test_language_language(self):
        """Test if the language value is created correctly"""
        lan = Language()
        self.assertTrue(hasattr(lan, "language"))
        self.assertEqual(lan.language, None)

    def Test_list_all_languages(self):
        """checks if it List all the languages of the page"""
        langs = Language.list_languages()
        self.assertTrue(isinstance(langs, list))

    def Test_list_user_languages(self):
        """checks if it List all the languages of the user"""
        langs = Language.list_language_usu(User.search_user("LR17"))
        self.assertTrue(isinstance(langs, list))
        self.assertEqual(langs[0], "español")
