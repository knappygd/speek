#!/usr/bin/python3

import os
from flask import Flask, jsonify
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

app = Flask(__name__)


@app.route('/api/get_users', methods=['GET'])
def get_users():
    """return all the users"""
    try:
        result = supabase.table('users').select().execute()
        data = result.get('data', [])
        print(data)
        return jsonify(data)
    except Exception as e:
        raise Exception(str(e))


if __name__ == '__main__':
    app.run()
