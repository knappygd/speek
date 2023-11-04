#!/usr/bin/python3

import datetime
import os
import uuid
import random
from supabase import create_client
from typing import List

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def list_languages():
    """returns a list with all the languages supported by speek"""
    try:
        languages = supabase.table("languages").select("language").execute()
        return languages
    except:
        raise Exception()


def list_languages_user(user_id: str):
    """returns a list with all the languages of the user"""
    try:
        languages = supabase.table("users").select(
            'username, languages(language)').execute()
        return languages
    except:
        raise Exception()
