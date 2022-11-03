
from .core import Core
from ..config import settings

def main():
    """ Main function.
    """
    settings.validators.validate_all()

    plugins = settings.plugins

    app = Core(plugins=plugins)
    app.run()
