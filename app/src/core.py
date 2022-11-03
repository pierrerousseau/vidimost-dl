import importlib

# Constants
# path to the plugins
PLUGINS_PATH  = "app.plugins."
# // Constants


class Core:
    """ Core of the application.
    """
    def __init__(self, plugins:list=None):
        if plugins is None:
            plugins = []

        plugins_path = PLUGINS_PATH

        self._plugins = [importlib.import_module(plugins_path + plugin).Plugin
                         for plugin in plugins]

    def run(self):
        """ Run the application
        """
        print("Starting ...")

        print("This is the core system")

        for plugin in self._plugins:
            plugin().process()

        print("... done.")
