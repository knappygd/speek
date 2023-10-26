<<<<<<< HEAD
#!/usr/bin/python3
"""
initialize the database
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from speek.models.API.v1 import DBStorage
    storage = DBStorage()
storage.reload()
=======
>>>>>>> 47e73fc72b776ef02d0f019082d29088615eaea7
