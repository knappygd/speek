#!/usr/bin/python3

import os
import uuid
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

speek_id = uuid.uuid4()


def list_users():
    """method to list all users"""
    try:
        data = supabase.table('users').select('*').execute()
        return data
    except:
        raise Exception()


def list_free_users():
    """a method to list all user with the status 1(they are free for random chat)"""
    try:
        data = supabase.table('users').select('*').eq('status', 1).execute()
        return data
    except:
        raise Exception()


def search_user(username):
    """a function to search for a user by their username"""
    try:

        data = supabase.table('users').select(
            'id').eq('username', username).execute()
        return data
    except:
        raise Exception()


def modify_user(user_id: str, column: str, data):
    """Update values associated with the user"""
    try:
        updt = supabase.table('users').update(
            {column: data}).eq('id', user_id).execute()
    except:
        raise Exception()


def self_delete(ex_user: str):
    """Deletes the user's own account"""
    try:
        user = supabase.table("users").delete().eq("username", ex_user)
        return user
    except:
        raise Exception()


def add_speeks(user_id, lang_id):
    """a function that adds the language to a user"""
    try:
        structure = {
            'speaks_id': str(speek_id),
            'user_id': str(user_id),
            'lang_id': str(lang_id)
        }
        data = supabase.table('speaks').insert(structure).execute()
        return data
    except:
        raise Exception()
