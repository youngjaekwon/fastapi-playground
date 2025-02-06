from random import randint
from typing import Annotated

from fastapi import APIRouter, Depends, Cookie

router = APIRouter(prefix="/ch-30", tags=["ch.30"])


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q


@router.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or_default}


def get_random_value():
    return randint(1, 10)


@router.get("/rand-int/cached/")
async def get_cached_random_value(
    value_a: Annotated[int, Depends(get_random_value)],
    value_b: Annotated[int, Depends(get_random_value)],
):
    return {"random_value_a": value_a, "random_value_b": value_b}


@router.get("/rand-int/fresh/")
async def get_fresh_random_value(
    value_a: Annotated[int, Depends(get_random_value, use_cache=False)],
    value_b: Annotated[int, Depends(get_random_value, use_cache=False)],
):
    return {"random_value_a": value_a, "random_value_b": value_b}
