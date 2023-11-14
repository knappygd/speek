#!/usr/bin/python3

import os
from supabase import create_client
from api.v1.views import app_views
from models import auth, chat, language, link, listener, messages, random_topics, topics, user
import time
import uuid
from datetime import datetime
from random import randint

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
session = ""

created_at = str(datetime.now())
updated_at = str(datetime.now())
custom_id = f"{randint(0, 9999):0{4}}"


@app_views.route('/get_users', methods=['GET'])
def get_users():
    """return all the users"""
    return user.list_users()


@app_views.route('/signin/<email>/<password>', methods=['GET'])
def signin(email, password):
    """Sign in a user with email and password."""
    return auth.signin(email, password)


@app_views.route('/list_friends/<user_id>', methods=['GET'])
def list_friends(user_id):
    """a method that returns all the id of the users who are friends"""
    return link.list_friends_links(user_id)


@app_views.route('/get_id', methods=['GET'])
def getid():
    return auth.getid()


@app_views.route('/search_user/<user_id>', methods=['GET'])
def search_user(user_id):
    """a function to search for a user by their username"""
    return user.search_user(user_id)


@app_views.route('/search_chat/<user_id>/<friend_id>', methods=['GET'])
def search_chat(user_id, friend_id):
    """a function that search for the chat of the user"""
    return chat.search_chat(user_id, friend_id)


@app_views.route('/list_message/<chat_id>', methods=['GET'])
def list_message(chat_id):
    """a function that shows the last 50 messages of a chat"""
    return messages.list_message(chat_id)


@app_views.route('/send_message/<content>/<to_user>/<in_chat>', methods=['POST'])
def send_message(content, to_user, in_chat):
    try:
        return messages.send_message(content, to_user, in_chat)
    except Exception as e:
        print(f"Error: {str(e)}")


@app_views.route('/get_chat/<user_id>', methods=['GET'])
def get_chat(user_id):
    session_id = auth.getid()
    chat_id = chat.search_chat(session_id, user_id)
    time.sleep(1)
    return messages.list_message(chat_id)


@app_views.route('/signup/<username>/<email>/<password>/<desc>', methods=['GET'])
def signup(username, email, password, desc):
    return auth.signup({"pfp": "pfpuser", "country": "Uruguay", "created_at": created_at, "updated_at": updated_at, "id": str(uuid.uuid4()), "username": username, "email": email, "password": password, "desc": desc, "status": 1, 'custom_id': custom_id})


@app_views.route('/get_random_chat', methods=['GET'])
def get_random_chat():
    return chat.random_chat(1)


@app_views.route('/list_random/<user_id>', methods=['GET'])
def list_random(user_id):
    return link.list_random(user_id)


@app_views.route('/random_topic', methods=['GET'])
def random_topic():
    top = topics.search_topic()
    return top[0]["topic"]
