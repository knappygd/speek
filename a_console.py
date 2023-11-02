#!/usr/bin/python3

import os
from supabase import create_client
from datetime import datetime
from random import randint
from models import messages
from models import auth
from models import chat
from models import listener


# insert data in the users column
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

created_at = str(datetime.now())
updated_at = str(datetime.now())
custom_id = f"{randint(0, 9999):0{4}}"

data = {
    'email': 'emiliodamasco@gmail.com',
    'password': 'admin1234',
    'status': 1,
    'pfp': 'pfpurl.server.com',
    'country': 'Uruguay',
    'desc': 'I speak German',
    'created_at': created_at,
    'updated_at': updated_at,
    'custom_id': custom_id,
    'username': 'Emilio Damasco',
}

# auth.signup(data)
auth.signin(data['email'], data['password'])
message = input("type your message: ")
messages.send_message(message,
                      'a89136d5-9fee-465e-af62-8b7c49c197ff', 'ea2ea75b-1f37-4a10-bd21-3a96b64b1cf4')
