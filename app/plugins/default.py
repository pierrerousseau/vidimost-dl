""" Default plugin.

    Other plugins should follow this model.
"""


class Downloader:
    """ Main class to deal with downloads.
    """
    def download(self):
        """ Download a file.
        """
        print("download file ...")

        return {"name": "test",
                "date": "test",
                "size": "test"}
