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


def get_random_user():
    records = user.list_users()
    rand = random.randint(0, len(records) - 1)
    random_userid = supabase.table('users').select(
        'email').range(0, rand).limit(1).execute()
    return str(random_userid)

print(supabase)
user_1 = auth.getuser()
user_2 = get_random_user()
if user_2 == user_1:
    while user_2 == user_1:
        user_2 = get_random_user()


def generate_chat():
    structure = {
        'chat_id': chat_id,
        'user_1': user_1,
        'user_2': user_2,
    }
    supabase.table('chat').insert(structure).execute()
    return chat_id


def delete_chat(chat_id):
    """a function that allows to delete a chat when they finish their talk"""
    try:
        supabase.table("chat").delete().eq("chat_id", chat_id)
    except:
        raise Exception()
