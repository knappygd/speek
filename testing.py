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

mi = messages.list_message('ea2ea75b-1f37-4a10-bd21-3a96b64b1cf4')
print(mi)