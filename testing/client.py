#!/usr/bin/python3

import asyncio
import websockets


async def client1():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Client 1: Enter a message (or 'exit' to quit): ")
            if message == 'exit':
                break
            await websocket.send(message)
            print(f"Sent to server: {message}")

            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(client1())
