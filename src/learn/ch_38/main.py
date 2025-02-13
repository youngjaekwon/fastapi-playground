from fastapi import Depends, status, APIRouter

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

router = APIRouter(
    prefix="/ch-38", tags=["ch.38"], dependencies=[Depends(get_query_token)]
)


router.include_router(users.router)
router.include_router(items.router)
router.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={status.HTTP_418_IM_A_TEAPOT: {"description": "I'm a teapot"}},
)


@router.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
