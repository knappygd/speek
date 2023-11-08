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
from models import language

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

created_at = str(datetime.now())
updated_at = str(datetime.now())

chat.generate_chat('d30dd8e0-f51a-4791-9a8c-70c471e1f80d')