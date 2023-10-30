#!/usr/bin/python3

import os
from supabase import create_client
from datetime import datetime
from random import randint
from models import messages
from models import auth
from models import chat


# insert data in the users column
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

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
other_user = chat.get_random_user()
user2 = auth.getuser(other_user)
Chit = chat.generate_chat(
    {"user_1": sesion1, "user_2": other_user})
messages.send_message('hi', Chit)
