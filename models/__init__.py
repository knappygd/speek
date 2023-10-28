#!/usr/bin/python3
"""
initialize the database
"""
import os
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from dev.speek.models.engine.db_storage import DBStorage
    storage = DBStorage()
