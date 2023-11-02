#!/usr/bin/python3

import os
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def list_users():
    """method to list all users"""
    try:
        data = supabase.table('users').select('username').execute()
        return data
    except:
        raise Exception()


def list_free_users():
    """a method to list all user with the status 1(they are free for random chat)"""
    data = supabase.table('users').select('username').eq('status', 1).execute()
    return data


def search_user(username):
    """a function to search for a user by their username"""
    data = supabase.table('users').select(
        'id').eq('username', username).execute()
    return data
