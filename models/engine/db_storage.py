#!/usr/bin/python3
""" Contains all the methods of the database"""
from typing import List, Dict
import os

from supabase import create_client, Client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


#//methods of the user

def delete_user():
    """A function so that a user can delete themselves"""

def modify_user():
    """a function that lets the user modify one of its attributes"""

def invite():
    """a function that lets a user send a friend request"""

def list_friends(user_name: str)-> List[Dict]:
    """A function that list the friends of a user"""

def change_status():
    """a function so that the user can change their status"""

def del_friednf():
    """a function that can allow a user to erase a friend of their friend list"""

def block_user():
    """"a function that allows a user to block them so they will not be able to talk any longer"""

def report_user(user_name: str):
    """a function that sends a report to another user for misbehavior or some inapropiated behavior"""

def search_user(user_name: str):
    """a function that allows the search for a user"""

def list_random_chat():
    """a function that lists all your active random chats"""

def login(user_name: str, password: str):
    """a function to verify the identity of the user an allow them to use the page"""


#// method of the message table
def send_message():
    """a function so that an user will be able to send a message to another user"""

#// method of the chat table
def create_chat():
    """a function to create a chat"""

def delete_chat():
    """a function that allows to delete a chat when they finish their talk"""

def search_chat(user_name: str)-> Dict:
    """a function that looks for a chat a specific chat"""

#// method of the Topic table
def dictionary_topics()->Dict:
    """a function that returns a dictionary with all the topics"""

#// method of the Language table
def list_languages()-> List(str):
    """returns a list with all the languages suported by speek"""

def list_languages(user_name: str)-> List(str):
    """returns a list with all the languages of the user"""