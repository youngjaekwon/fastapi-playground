from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ch-01", tags=["ch.01"])


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@router.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]


@router.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item


@router.get("/new-items/", include_in_schema=False)
async def read_items_excluded():
    return [{"item_id": "Foo"}]


def use_route_names_as_operation_ids(router: APIRouter) -> None:
    """
    Simplify operation IDs so that generated API clients have impler function names.

    Should be called only after all routes have been added.
    """
    for route in router.routes:
        if isinstance(route, APIRouter):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(router)
