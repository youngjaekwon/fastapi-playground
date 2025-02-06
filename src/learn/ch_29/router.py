from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/ch-29", tags=["ch.29"])

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


# Depends에 매개변수를 넣지 않아도 똑같이 작동함
@router.get("/items/")
# async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
