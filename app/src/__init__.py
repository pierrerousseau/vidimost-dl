""" Root of the backend code.
"""
from app.src.core import Core

from .models.downloads import create_download, \
    downloads

# Constants
# path to the plugins
PLUGINS_PATH  = "app.plugins."
# // Constants


def download_file(plugin=None):
    """ Downloads a file using the provided plugin.
    """
    if plugin is None:
        plugin = "default"

    downloader = Core().get(plugin)

    file = downloader().download()

    return create_download(file)


def downloaded_files():
    """ Returns the list of downloaded files.
    """
    return downloads()
