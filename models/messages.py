#!/usr/bin/python3

import datetime
import os
import auth
import chat
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


userid = auth.getid()
sent_at = str(datetime.now())
chat_id = chat.generate_chat()

response = supabase.sql(f"""
    SELECT messages.*, chat.receiver_info
    FROM messages AS messages
    INNER JOIN chats AS chats
    ON messages.chat_id = chats.chat_id
    WHERE messages.chat_id = {chat}
""")

for row in response.data:
    receiver = row['receiver']


def send_message(message, chat=chat_id):
    structure = {
        'content': message,
        'sender': userid,
        'receiver': receiver,
        'sent_at': sent_at,
        'chat_id': chat
    }
    supabase.table('messages').insert(structure).execute()