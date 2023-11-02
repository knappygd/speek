#!/usr/bin/python3

import os
from supabase import create_client
import uuid

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
status_id = uuid.uuid4()


def new_status(link_id):
    """add a new status"""
    structure = {
        'status_id': status_id,
        'status': 1,
        'link_id': link_id
    }
    supabase.table('status').insert(structure)


def search_status_id_by_link(link_id):
    """a method to search a status by their link id"""
    stat = supabase.table('status').select('status_id').eq('link_id', link_id)
    return stat


def search_status(stat_id):
    """a method to search a status by their status id"""
    stat = supabase.table('status').select('*').eq('status_id', stat_id)
    return stat


def accept_friendship(stat_id):
    """upodates the status of the link so they accept the freinship"""
    supabase.table('status').update('status', 2).eq('status_id', stat_id)


def block_friendship(stat_id):
    """a method to update the status of the link so that they block the user"""
    supabase.table('status').update('status', 3).eq('status_id', stat_id)
