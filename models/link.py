#!/usr/bin/python3

import os
from supabase import create_client
import uuid
from datetime import datetime

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

link_id = uuid.uuid4()


def new_link(sender_id, reciever_id):
    """add a new link"""
    lista = []
    data1 = supabase.table('link').select(
        '*').match({'receiver_id': reciever_id, 'sender_id': sender_id}).execute()
    data2 = supabase.table('link').select(
        '*').match({'receiver_id': sender_id, 'sender_id': reciever_id}).execute()
    if data1.data == lista  and data2.data == lista :
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

def accept_friendship(link_id):
    """upodates the status of the link so they accept the freinship"""
    try:
        supabase.table('link').update({'status': 2}).eq(
            'link_id', link_id).execute()
    except:
        raise Exception()


def block_friendship(link_id):
    """a method to update the status of the link so that they block the user"""
    try:
        supabase.table('link').update({'status': 3}).eq(
            'link_id', link_id).execute()
    except:
        raise Exception()


def search_link(lin_id):
    """a function that search for a link"""
    try:
        supabase.table('link').select().eq('link_id', lin_id).execute()
    except:
        raise Exception()


def deletefriend(lin_id):
    """a function that delete the frienship between two users"""
    try:
        supabase.table('link').delete().eq('link_id', lin_id).execute()
    except:
        raise Exception()

def list_friends_links(user_id):
    """a method that returns all the id of the users who are friends"""
    try:
        friend1 = supabase.table('link').select('receiver_id').match({'status': 2, 'sender_id': user_id}).execute()
        friend2 = supabase.table('link').select('sender_id').match({'status': 2, 'receiver_id': user_id}).execute()
        return [friend1.data, friend2.data] 
    except:
        raise Exception('you have no friends :(')