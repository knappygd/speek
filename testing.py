#!/usr/bin/python3

import os
from supabase import create_client
from datetime import datetime
from random import randint
from models import messages
from models import auth
from models import chat
from models import listener
from models import user
from models import link
from models import status
from models import language

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

created_at = str(datetime.now())
updated_at = str(datetime.now())
custom_id = f"{randint(0, 9999):0{4}}"

#/ data = {
#/    'email': 'LeonardoRodriguez17@gmail.com',
#/    'password': 'admin17',
#/    'username': 'Leo Kenobi',
#/    'status': 1,
#/    'pfp': 'pfpLeo',
#/    'country': 'Uruguay',
#/    'desc': 'Quien es mas boludo el boludo o el boludo que lo sigue',
#/    'created_at': created_at,
#/    'updated_at': updated_at,
#/    'custom_id': custom_id
#/}
#/ auth.signup(data)
#/lista = user.get_user_inicials('061bcaeb-c60b-44ed-bac1-58c2a151d119')
#/print(lista)

status.accept_friendship('11e2b536-cc8f-4a67-bc64-a95b2f9f7472')