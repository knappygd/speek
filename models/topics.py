#!/usr/bin/python3

import datetime
import os
from models import auth
from models import user
import uuid
import random
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def dictionary_topics():
    """a function that returns a dictionary with all the topics"""
    try:
        topic = supabase.table("topics").select("*")
        return topic
    except:
        raise Exception()
