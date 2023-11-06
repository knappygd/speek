#!/usr/bin/python3

import os
from supabase import create_client
from flask import Flask
from flask_cors import CORS

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/test_api/get_users', methods=['GET'])
def get_users():
    """return all the users"""
    try:
        response = supabase.table('users').select('*').execute()
        data = response.data
        return (data)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(threaded=True)
