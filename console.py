#!/usr/bin/python3

import messages
import os
from postgrest.exceptions import APIError
from supabase import create_client, Client
from datetime import datetime
from random import randint
import time

import auth

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
auth.signin(data['email'], data['password'])
messages.send_message('hii')
