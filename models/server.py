#!/usr/bin/python3

import asyncio
import websockets

async def server(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            response = f"{message}"
            await websocket.send(response)
    except websockets.ConnectionClosedError:
        print("Client disconnected")

# This is a temporary address
start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
