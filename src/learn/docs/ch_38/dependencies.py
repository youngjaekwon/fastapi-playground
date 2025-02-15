from typing import Annotated

from fastapi import Header, HTTPException, status


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake_super_secret-token":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="X-Token header invalid"
        )


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No Jessica token provided"
        )
