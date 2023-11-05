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
        languages = supabase.table('languages').select('language').execute()
        return languages
    except:
        raise Exception()


def list_languages_user(user_id: str):
    """returns a list with all the languages of the user"""
    try:
        languages = supabase.table('speaks').select(
            '*').eq('user_id', user_id).execute()
        return languages
    except:
        raise Exception()


def list_user_langugaes(lang_id):
    """returns all the users that know this language"""
    try:
        languages = supabase.table('speaks').select(
            '*').eq('lang_id', lang_id).execute()
        return languages
    except:
        raise Exception()
