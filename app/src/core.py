""" Core application.
"""
import importlib

from app.config import settings

# Constants
# path to the plugins
PLUGINS_PATH  = "app.plugins."
# // Constants


class Core:
    """ Core of the application.
    """
    def __init__(self, plugins:list=None):
        if plugins is None:
            plugins = settings.plugins

        plugins_path = PLUGINS_PATH

        self._plugins = {plugin: importlib.import_module(plugins_path + plugin).Downloader
                         for plugin in plugins}

    def get(self, name):
        """ Returns the requested plugin.
        """
        return self._plugins[name]

    def run(self):
        """ Runs the application.
        """
        print("Starting ...")

        print("This is the core system")

        for plugin in self._plugins.values():
            plugin().process()

        print("... done.")
