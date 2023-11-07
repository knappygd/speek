#!/usr/bin/python3

from models import messages

while True:
    message = input("type your message: ")
    messages.send_message(message,
                          '061bcaeb-c60b-44ed-bac1-58c2a151d119', 'ea2ea75b-1f37-4a10-bd21-3a96b64b1cf4')
