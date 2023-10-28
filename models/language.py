#!/usr/bin/python3

import datetime
import os
import auth
import uuid
import random
from supabase import create_client
from typing import List

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def list_languages() -> List(str):
    """returns a list with all the languages supported by speek"""
    try:
        languages = supabase.table("languages").select("*")
        return languages
    except:
        raise Exception()


def list_languages(user_name: str) -> List(str):
    """returns a list with all the languages of the user"""
