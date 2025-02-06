from typing import Annotated

from fastapi import APIRouter, Header, HTTPException, status, Depends


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="X-Token header invalid"
        )


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="X-Key header invalid"
        )
    return x_key


router = APIRouter(
    prefix="/ch-32",
    tags=["ch.32"],
    dependencies=[Depends(verify_token), Depends(verify_key)],
)


@router.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@router.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
