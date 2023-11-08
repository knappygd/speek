#!/usr/bin/python3

import os
from supabase import create_client
from flask import Flask
from flask_cors import CORS
import json

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
session = ""

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


@app.route('/test_api/signin/<email>/<password>', methods=['GET'])
def signin(email, password):
    """Sign in a user with email and password."""
    try:
        supabase.auth.sign_in_with_password(
            {"email": email, "password": password})
        uid = supabase.table('users').select('id').eq('email', email).execute()
        session = '1'
    except:
        session = '0'
        uid = "data=[] count=None"
    data = {
        'email': email,
        'password': password,
        'id': str(uid),
    }
    with open('session.json', 'w') as f:
        json.dump(data, f)
    return session


@app.route('/test_api/list_friends/<user_id>', methods=['GET'])
def list_friends(user_id):
    """a method that returns all the id of the users who are friends"""
    friend1 = supabase.table('link').select('receiver_id').match(
        {'status': 2, 'sender_id': user_id}).execute()
    friend2 = supabase.table('link').select('sender_id').match(
        {'status': 2, 'receiver_id': user_id}).execute()
    lista = []
    for friend_id in friend1.data:
        lista.append(friend_id["receiver_id"])
    for friend_id in friend2.data:
        lista.append(friend_id["sender_id"])
    return lista


@app.route('/test_api/get_id', methods=['GET'])
def getid():
    with open('session.json', 'r') as f:
        data = json.load(f)
    return data['id'][14:50]


@app.route('/test_api/search_user/<user_id>', methods=['GET'])
def search_user(user_id):
    """a function to search for a user by their username"""
    try:
        data = supabase.table('users').select(
            '*').eq('id', user_id).execute()
        user = data.data
        return user[0]
    except:
        raise Exception()


@app.route('/test_api/search_chat/<user_id>/<friend_id>', methods=['GET'])
def search_chat(user_id, friend_id):
    """a function that search for the chat of the user"""
    lista = []
    ch = supabase.table('chats').select('chat_id').match(
        {'user_1': friend_id, 'user_2': user_id}).execute()
    if ch.data == lista:
        ch = supabase.table('chats').select('chat_id').match(
            {'user_2': friend_id, 'user_1': user_id}).execute()
    chat = ch.data
    return chat[0]["chat_id"]


@app.route('/test_api/list_message/<chat_id>', methods=['GET'])
def list_message(chat_id):
    """a function that shows the last 50 messages of a chat"""
    data = supabase.table('messages').select('*').match(
        {'chat_id': chat_id}).order('messages_id').execute()
    return data.data


if __name__ == "__main__":
    app.run(threaded=True)
