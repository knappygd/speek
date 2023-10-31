#!/usr/bin/python3
import websockets
import asyncio
import os
import json

SUPABASE_ID = os.environ.get("SUPABASE_ID")
API_KEY = os.environ.get("SUPABASE_KEY")


async def send_message():
    URL = f"wss://{SUPABASE_ID}.supabase.co/realtime/v1/websocket?apikey={API_KEY}&vsn=1.0.0"
    async with websockets.connect(URL) as ws:
        message_payload = {
            "topic": "realtime:*",
            "event": "new_message",  # Custom event name
            "payload": {
                "message": "Hello, this is a real-time message!",
                "user_id": "user123"
            }
        }

        # Send the message
        await ws.send(json.dumps(message_payload))

        # Receive the server's response
        response = await ws.recv()
        print(f"Server response: {response}")

        # Check the response to determine the status
        response_data = json.loads(response)

        if response_data.get("status") == "success":
            print("Message sent successfully")
        else:
            print("Message sending failed")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_message())
