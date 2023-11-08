#!/usr/bin/python3

import os
import json
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def send_message(content, to_user, in_chat):
    with open('session.json', 'r') as f:
        data = json.load(f)
    structure = {
        'content': content,
        'sender': data['id'][14:50],
        'receiver': to_user,
        'chat_id': in_chat
    }
    supabase.table('messages').insert(structure).execute()


def list_message(chat_id):
    """a function that shows the last 50 messages of a chat"""
    data = supabase.table('messages').select('*').match(
        {'chat_id': chat_id}).order('messages_id', desc=True).execute()
    return data
