#!/usr/bin/python3

import os
from supabase import create_client
from flask import Flask
from flask_cors import CORS
import json
from models import auth, chat, language, link, listener, messages, random_topics, topics, user

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
session = ""

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/api/get_users', methods=['GET'])
def get_users():
    """return all the users"""
    return user.list_users()


@app.route('/api/signin/<email>/<password>', methods=['GET'])
def signin(email, password):
    """Sign in a user with email and password."""
    return auth.signin(email, password)


@app.route('/api/list_friends/<user_id>', methods=['GET'])
def list_friends(user_id):
    """a method that returns all the id of the users who are friends"""
    return link.list_friends_links(user_id)


@app.route('/api/get_id', methods=['GET'])
def getid():
    return auth.getid()


@app.route('/api/search_user/<user_id>', methods=['GET'])
def search_user(user_id):
    """a function to search for a user by their username"""
    return user.search_user(user_id)


@app.route('/api/search_chat/<user_id>/<friend_id>', methods=['GET'])
def search_chat(user_id, friend_id):
    """a function that search for the chat of the user"""
    return chat.search_chat(user_id, friend_id)


@app.route('/api/list_message/<chat_id>', methods=['GET'])
def list_message(chat_id):
    """a function that shows the last 50 messages of a chat"""
    return messages.list_message(chat_id)


@app.route('/api/send_message/<content>/<to_user>/<in_chat>', methods=['POST'])
def send_message(content, to_user, in_chat):
    return messages.send_message(content, to_user, in_chat)


if __name__ == "__main__":
    app.run(threaded=True)
