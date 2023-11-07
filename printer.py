#!/usr/bin/python3
import json
import time

prev = ""

while True:
    with open('models/messages_cache.json', 'r') as file:
        data = json.load(file)

    current = data.get("message_content")

    if current != prev:
        print(current)

    prev = current

    time.sleep(1)
