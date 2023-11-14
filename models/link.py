#!/usr/bin/python3

import os
import json
from supabase import create_client
import uuid
from datetime import datetime
from models import auth

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
from models import chat
link_id = uuid.uuid4()


def new_link(sender_id, reciever_id):
    """add a new link"""
    lista = []
    data1 = supabase.table('link').select(
        '*').match({'receiver_id': reciever_id, 'sender_id': sender_id}).execute()
    data2 = supabase.table('link').select(
        '*').match({'receiver_id': sender_id, 'sender_id': reciever_id}).execute()
    if data1.data == lista and data2.data == lista:
        structure = {
            "link_id": str(link_id),
            "sender_id": str(sender_id),
            "receiver_id": str(reciever_id),
            "status": 1,
            "linked_at": str(datetime.now())
        }
        data = supabase.table('link').insert(structure).execute()
        return data
    else:
        raise ('you are alredy connected')


def accept_friendship(link_id, user_id):
    """upodates the status of the link so they accept the freinship"""
    try:
        supabase.table('link').update({'status': 2}).eq(
            'link_id', link_id).execute()
        chat.generate_chat(user_id)
        
    except:
        raise Exception()


def block_friendship(link_id):
    """a method to update the status of the link so that they block the user"""
    try:
        supabase.table('link').update({'status': 3}).eq(
            'link_id', link_id).execute()
    except:
        raise Exception()


def search_link(receiver_id, sender_id):
    """a function that search for a link"""
    lista = []
    lk = supabase.table('link').select('link_id').match({'receiver_id': receiver_id, 'sender_id': sender_id}).execute()
    if lk == lista:
        lk = supabase.table('link').select('link_id').match({'receiver_id': sender_id, 'sender_id': receiver_id}).execute()
    if lk == lista:
        raise Exception('no existe un link')
    else:
        return lk


def deletefriend(lin_id):
    """a function that delete the frienship between two users"""
    try:
        supabase.table('link').delete().eq('link_id', lin_id).execute()
    except:
        raise Exception()


def list_friends_links(user_id):
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

def generete_random_link(reciever_id, sender_id):
    """a method to start a link in 0 relation"""
    lista = []
    data1 = supabase.table('link').select(
        '*').match({'receiver_id': reciever_id, 'sender_id': sender_id}).execute()
    data2 = supabase.table('link').select(
        '*').match({'receiver_id': sender_id, 'sender_id': reciever_id}).execute()
    if data1.data == lista and data2.data == lista:
        structure = {
            "link_id": str(link_id),
            "sender_id": str(sender_id),
            "receiver_id": str(reciever_id),
            "status": 0,
            "linked_at": str(datetime.now())
        }
        data = supabase.table('link').insert(structure).execute()
        return data
    else:
        raise ('you are alredy connected')


def list_random(user_id):
    """a method that returns all the id of the users who are friends"""
    friend1 = supabase.table('link').select('receiver_id').match(
        {'status': 0, 'sender_id': user_id}).execute()
    friend2 = supabase.table('link').select('sender_id').match(
        {'status': 0, 'receiver_id': user_id}).execute()
    lista = []
    for friend_id in friend1.data:
        lista.append(friend_id["receiver_id"])
    for friend_id in friend2.data:
        lista.append(friend_id["sender_id"])
    return lista