#!/usr/bin/python3

from models import messages

while True:
    message = input("type your message: ")
    messages.send_message(message,
                          'a89136d5-9fee-465e-af62-8b7c49c197ff', 'ea2ea75b-1f37-4a10-bd21-3a96b64b1cf4')
