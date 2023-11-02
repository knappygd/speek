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


def new_link(sender, reciever):
    """add a new status"""
    structure = {
        'link_id': str(link_id),
        'sender_id': sender,
        'receiver_id': reciever,
        'linked_at': datetime.now
    }
    supabase.table('link').insert(structure)
    status.new_status(link_id)
    return link_id


def search_link(lin_id):
    """a function that search for a link"""
    supabase.table('link').select().eq('link_id', lin_id)


def block_user(sender, receiver):
    """a method to block users"""
    link = new_link(sender, receiver)
    stat = status.search_status_id_by_link(link)
    status.block_friendship(stat)


def deletefriend(lin_id):
    """a function that delete the frienship between two users"""
    supabase.table('status').delete().eq('link_id', lin_id).execute()
    supabase.table('link').delete().eq('link_id', lin_id).execute()
