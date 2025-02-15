from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/ch-28", tags=["ch.28"])


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@router.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


@router.get("/users/")
async def read_users(common: CommonsDep):
    return common
