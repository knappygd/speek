#!/usr/bin/python3

import os
from supabase import create_client
from api.v1.views import app_views
from models import auth, chat, language, link, listener, messages, random_topics, topics, user

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
session = ""


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
        messages.send_message(content, to_user, in_chat)
    except Exception as e:
        print(f"Error: {str(e)}")


@app_views.route('/get_chat/<user_id>', methods=['GET'])
def get_chat(user_id):
    session_id = auth.getid()
    chat_id = chat.search_chat(session_id, user_id)
    return messages.list_message(chat_id)
