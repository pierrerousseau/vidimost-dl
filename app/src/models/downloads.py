""" Downloads managment.

    {"filename": name of the fle,
     "filedate": creation date of the file,
     "filesize": size of the file,
     "date": download date}
"""
from datetime import datetime

from app.libs.database import get_cached_cnx

# Constants
COL_NAME = "downloads"
# // Constants


def downloads():
    """ Get the list of processed downloads.
    """
    col = get_cached_cnx(COL_NAME)

    return col.find()


def create_download(file):
    """ Create a processed download.
    """
    col = get_cached_cnx(COL_NAME)

    now = datetime.now()

    insert = col.insert_one({"filename": file["name"],
                             "filedate": file["date"],
                             "filesize": file["size"],
                             "date": now})

    return insert.inserted_id
