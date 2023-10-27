#!/usr/bin/python3

import os
from supabase import create_client, Client
from datetime import datetime
from random import randint
from models import messages
from models import auth
from models import chat

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# insert data in the users column

created_at = str(datetime.now())
updated_at = str(datetime.now())
custom_id = f"{randint(0, 9999):0{4}}"

data = {
    'email': 'enriquecabrera@gmail.com',
    'password': 'admin1234',
    'status': 1,
    'pfp': 'pfpurl.server.com',
    'country': 'Uruguay',
    'desc': 'I speak English',
    'created_at': created_at,
    'updated_at': updated_at,
    'custom_id': custom_id,
    'username': 'Enrique Cabrera',
}

# auth.signup(data)
sesion1 = auth.signin(data['email'], data['password'])
you = auth.getuser()
Chit = chat.generate_chat({"chat_id": 1, "user_1": you, "user_2": sesion1})
messages.send_message('hii', Chit)
