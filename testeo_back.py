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


user.add_speeks('e982193a-b11f-4b3b-82cc-aef6ce21a87d', 1)
