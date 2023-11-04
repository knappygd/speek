#!/usr/bin/python3

import os
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

"""method to list all users"""
try:
    response = supabase.table('users').select('*').execute()
    data = response.data
    print(data)
except Exception as e:
    print(f"Error: {str(e)}")
