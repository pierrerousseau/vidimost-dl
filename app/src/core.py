""" Core application.
"""
from importlib import import_module

from app.config import settings

# Constants
# path to the plugins
PLUGINS_PATH  = "app.plugins."
# // Constants


class Core:
    """ Core of the application.
    """
    def __init__(self, plugins=settings.plugins):
        plugins_path = PLUGINS_PATH

        self._plugins = \
            {plugin:
                {"downloader": import_module(plugins_path + plugin).Downloader,
                 "config": config}
             for plugin, config in plugins.items()}

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
            plugin["downloader"](plugin["config"]).process()

        print("... done.")
