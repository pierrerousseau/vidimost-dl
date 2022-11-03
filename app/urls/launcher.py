from fastapi import APIRouter
from app.src import main

launcher = APIRouter(
    prefix="/launcher",
    tags=["launcher"],
    responses={404: {"description": "Not found"}},
)


@launcher.post("/", tags=["launcher"])
async def launch():
    main()
    return {"done": "ok"}
