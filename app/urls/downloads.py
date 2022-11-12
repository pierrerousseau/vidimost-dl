""" Api to manage downloads.
"""
import json

from fastapi import APIRouter

from app.src import download_file, \
    downloaded_files

downloads = APIRouter(
    prefix="/downloads",
    tags=["downloads"],
    responses={404: {"description": "Not found"}},
)


def json_encoder(obj):
    """ Temporary solution for json encoding of custom types.

        FIXME: it is not clear to me how to globaly change the fastapi jsonencoder
    """
    return json.loads(json.dumps(obj, default=str))


@downloads.get("/", tags=["downloads"])
async def get_downloads():
    """ Get the list of downloads.
    """
    return json_encoder({"downloads": list(downloaded_files())})


@downloads.put("/", tags=["downloads"])
@downloads.put("/{downloader}", tags=["downloads"])
async def put_download(downloader=None):
    """ Initiate a new download.
    """
    return json_encoder({"download": download_file(downloader)})
