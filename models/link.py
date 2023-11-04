#!/usr/bin/python3

import os
from supabase import create_client
import uuid
from datetime import datetime
from models import status

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

link_id = uuid.uuid4()


def new_link(sender_id, reciever_id):
    """add a new link"""
    structure = {
        "link_id": str(link_id),
        "sender_id": str(sender_id),
        "receiver_id": str(reciever_id),
        "linked_at": str(datetime.now())
    }
    data = supabase.table('link').insert(structure).execute()
    status.new_status(link_id)
    return data


def search_link(lin_id):
    """a function that search for a link"""
    try:
        supabase.table('link').select().eq('link_id', lin_id).execute()
    except:
        raise Exception()


def deletefriend(lin_id):
    """a function that delete the frienship between two users"""
    try:
        supabase.table('status').delete().eq('link_id', lin_id).execute()
        supabase.table('link').delete().eq('link_id', lin_id).execute()
    except:
        raise Exception()
