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

def random_topic(chat_id):
    """this function it is a random topic"""
    try:
        ran = random.randint(1,10)
        ch = supabase.table('chats').update({'topic_id': ran}).eq('chat_id', chat_id).execute()
        return ch
    except:
        raise Exception()

def search_topic(topic_id):
    """a function that returns the topic"""
    topic = supabase.table('topics').select('topic').eq('topic', topic_id).execute()
    return topic