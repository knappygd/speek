#!/usr/bin/python3

import os
from api.v1.views import app_views
from flask import jsonify
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


@app_views.route('/api/v1/views/get_users', methods=['GET'])
def get_users():
    """return all the users"""
    try:
        response = supabase.table('users').select('*').execute()
        data = response.data
        return (data)
    except Exception as e:
        print(f"Error: {str(e)}")
