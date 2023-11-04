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
        'status_id': str(status_id),
        'status': 1,
        'link_id': str(link_id)
    }
    supabase.table('status').insert(structure).execute()


def search_status_id_by_link(link_id):
    """a method to search a status by their link id"""
    try:
        stat = supabase.table('status').select(
            'status_id').eq('link_id', link_id).execute()
        return stat
    except:
        raise Exception()


def search_status(stat_id):
    """a method to search a status by their status id"""
    try:
        stat = supabase.table('status').select(
            '*').eq('status_id', stat_id).execute()
        return stat
    except:
        raise Exception()


def accept_friendship(stat_id):
    """upodates the status of the link so they accept the freinship"""
    try:
        supabase.table('status').update({'status': 2}).eq(
            'status_id', stat_id).execute()
    except:
        raise Exception()


def block_friendship(stat_id):
    """a method to update the status of the link so that they block the user"""
    try:
        supabase.table('status').update({'status': 3}).eq(
            'status_id', stat_id).execute()
    except:
        raise Exception()
