from typing import Annotated

from fastapi import APIRouter, Form
from pydantic import BaseModel

router = APIRouter(prefix="/ch-21", tags=["ch.21"])


class FormData(BaseModel):
    model_config = {"extra": "forbid"}

    username: str
    password: str


@router.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
