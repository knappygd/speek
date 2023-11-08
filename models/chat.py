#!/usr/bin/python3

import datetime
import os
from models import auth
from models import user
import uuid
import random
from models import auth
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

chat_id = uuid.uuid4()
session = str(auth.getid())
def generate_chat(user_id):
    structure = {
        'chat_id': str(chat_id),
        'user_1': session,
        'user_2': str(user_id),
        'topic_id': 0,
    }
    supabase.table('chats').insert(structure).execute()
    supabase.table('users_chats').insert({'user_id': str(session), 'chat_id': str(chat_id)}).execute()
    supabase.table('users_chats').insert({'user_id': str(user_id), 'chat_id': str(chat_id)}).execute()
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
