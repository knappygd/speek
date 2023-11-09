#!/usr/bin/python3

from flask import Flask, jsonify
import os
from supabase import create_client
from flask_cors import CORS

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/user/*": {"origins": "http://localhost:3000"}})


@app.route('/get', methods=['GET'])
def get_users():
    """return all the users"""
    try:
        response = supabase.table('users').select('*').execute()
        data = response.data
        return (data)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)