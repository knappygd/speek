#!/usr/bin/python3

import datetime
import os
from models import auth
from models import user
import uuid
import random
from models import auth
from models import language
from models import link
from supabase import create_client


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

chat_id = uuid.uuid4()
session = auth.getid()


def generate_chat(user_id):
    structure = {
        'chat_id': str(chat_id),
        'user_1': session,
        'user_2': str(user_id),
        'topic_id': 0,
    }
    supabase.table('chats').insert(structure).execute()
    supabase.table('users_chats').insert(
        {'user_id': str(session), 'chat_id': str(chat_id)}).execute()
    supabase.table('users_chats').insert(
        {'user_id': str(user_id), 'chat_id': str(chat_id)}).execute()
    return str(chat_id)


def delete_chat(chat_id):
    """a function that allows to delete a chat when they finish their talk"""
    try:
        supabase.table("chat").delete().eq("chat_id", chat_id)
    except:
        raise Exception()


def search_chat(user_id, friend_id):
    """a function that search for the chat of the user"""
    lista = []
    ch = supabase.table('chats').select('chat_id').match(
        {'user_1': friend_id, 'user_2': user_id}).execute()
    if ch.data == lista:
        ch = supabase.table('chats').select('chat_id').match(
            {'user_2': friend_id, 'user_1': user_id}).execute()
    chat = ch.data
    return chat[0]["chat_id"]


def random_chat(lang_id):
    """a funtion to create a random chat"""
    ran = random.randint(1, 7)
    lista = supabase.table('speaks').select('user_id').match(
        {'lang_id': lang_id}).range(ran-1, ran).execute()
    usu = lista.data
    while usu[0]["user_id"] == session:
        lista = supabase.table('speaks').select('user_id').match(
            {'lang_id': lang_id}).range(ran-1, ran).execute()
    li = link.generete_random_link(session, usu[0]["user_id"])
    generate_chat(usu[0]["user_id"])
    return usu[0]["user_id"]
