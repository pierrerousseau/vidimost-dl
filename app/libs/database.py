""" Generic db functions.
"""
from functools import lru_cache

import pymongo

from app.config import settings


def get_cnx(col, uri=None, dbb=None):
    """ Create a connexion to the database.

        When a new connexion is needed.
    """
    if uri is None:
        uri = settings.db["uri"]
    if dbb is None:
        dbb = settings.db["dbb"]

    client = pymongo.MongoClient(uri)

    return client[dbb][col]


@lru_cache
def get_cached_cnx(col, uri=None, dbb=None):
    """ Create a connexion to the database.

        Allow to keep a small number of connexion (one per collection).
    """
    return get_cnx(col, uri=uri, dbb=dbb)
