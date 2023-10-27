#!/usr/bin/python3
"""
initialize the database
"""
import os
from os import getenv
from supabase import create_client, Client

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from speek.models.API.v1 import DBStorage
    storage = DBStorage()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
