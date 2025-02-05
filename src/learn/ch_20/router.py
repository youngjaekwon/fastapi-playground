from typing import Annotated

from fastapi import APIRouter, Form

router = APIRouter(prefix="/ch-20", tags=["ch.20"])


@router.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
