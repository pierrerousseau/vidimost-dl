""" Point d'entrée FastAPI.
"""
from fastapi import FastAPI
from .urls.downloads import downloads

app = FastAPI(title="vidimost-dl",
              version="0.0.1")
app.include_router(downloads)


@app.get("/")
def read_root():
    """ Url example.
    """
    return {"Hello": "World"}
