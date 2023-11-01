#!/usr/bin/python3

import os
from supabase import create_client
from models import auth
import json
import time

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def listen(chat_id):
    receiver = supabase.table('chats').select(
        'user_1').eq('chat_id', chat_id).execute()
    receiver = str(receiver)[18:54]
    if auth.getid() == receiver:
        receiver = supabase.table('chats').select(
            'user_2').eq('chat_id', chat_id).execute()
        receiver = str(receiver)[18:54]
    while True:
        data = supabase.table('messages').select('content').match(
            {'sender': receiver, 'chat_id': chat_id}).limit(1).execute()
        message_id = supabase.table('messages').select('messages_id').match(
            {'sender': receiver, 'chat_id': chat_id}).limit(1).execute()
        message_id = str(message_id)[22:-13]
        with open('models/messages_cache.json', 'r') as f:
            data = json.load(f)
        if data['last_message'] != message_id:
            print(str(data))
        data = {
            'last_message': int(message_id)
        }
        with open('messages_cache.json', 'w') as f:
            json.dump(data, f)
        time.sleep(1)
