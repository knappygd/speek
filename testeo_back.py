#!/usr/bin/python3

import datetime
import os
import uuid
from supabase import create_client
from models import chat
from models import user
from models import link

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

li = link.list_random('0228bb97-2adc-4ada-9788-6bf9b27e14c3')
print(li)