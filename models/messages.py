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

    """ async def client():
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            message = content
            await websocket.send(message)
            print(f"Sent to server: {message}")

            response = await websocket.recv()
            print(f"Received from server: {response}")

    asyncio.get_event_loop().run_until_complete(client()) """

    supabase.table('messages').insert(structure).execute()
