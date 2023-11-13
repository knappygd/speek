#!/usr/bin/python3

import datetime
import os
from models import auth
from models import user
import uuid
import random
from supabase import create_client
import random
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def dictionary_topics():
    """a function that returns a dictionary with all the topics"""
    try:
        topic = supabase.table("topics").select("*").execute()
        return topic
    except:
        raise Exception()

def search_topic():
    """a function that returns the topic"""
    ran = random.randint(1,10)
    topic = supabase.table('topics').select('topic').eq('id', ran).execute()
    return topic