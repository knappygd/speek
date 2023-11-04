#!/usr/bin/python3
""" This module initializes the server """

import os
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/user/*": {"origins": "http://localhost:3000"}})
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(threaded=True)