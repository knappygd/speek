#!/usr/bin/python3

import os
import json
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
session = None


def signup(data):
    """Sign up a user with email and password and store the data in the users table."""
    try:
        supabase.auth.sign_up({
            'email': data['email'],
            'password': data['password'],
        })
    except:
        raise Exception
    finally:
        supabase.table('users').insert(data).execute()


def signin(email, password):
    """Sign in a user with email and password."""
    try:
        supabase.auth.sign_in_with_password(
            {"email": email, "password": password})
        uid = supabase.table('users').select('id').eq('email', email).execute()
        state = "exist"
    except:
        state = "not exist"
        uid = "data=[] count=None"
    data = {
        'email': email,
        'password': password,
        'id': str(uid),
    }
    with open('session.json', 'w') as f:
        json.dump(data, f)
    return state


def signout():
    """Sign out a user."""
    supabase.auth.sign_out()


def getuser():
    data = supabase.auth.get_user()
    print(data)


def getid():
    with open('session.json', 'r') as f:
        data = json.load(f)
    return data['id'][14:50]
