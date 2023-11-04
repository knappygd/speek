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

chat_id = uuid.uuid4()


def generate_chat():
    structure = {
        'chat_id': str(chat_id),
        'user_1': "a89136d5-9fee-465e-af62-8b7c49c197ff",
        'user_2': "061bcaeb-c60b-44ed-bac1-58c2a151d119",
        'topic_id': 1,
    }
    supabase.table('chats').insert(structure).execute()
    return chat_id


def delete_chat(chat_id):
    """a function that allows to delete a chat when they finish their talk"""
    try:
        supabase.table("chat").delete().eq("chat_id", chat_id)
    except:
        raise Exception()


def search_chat(friend):
    """a function that search for the chat of the user"""
    try:

        ch = supabase.table('chat').select(
            'chat_id, users(id)').eq('username', friend)
        return ch
    except:
        raise Exception()
