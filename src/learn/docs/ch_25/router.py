from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(prefix="/ch-25", tags=["ch.25"])


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@router.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["items"],
    # description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    summary="Create an item",
    response_description="The created item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@router.get("/items/", status_code=status.HTTP_200_OK, tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@router.get("/users/", status_code=status.HTTP_200_OK, tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@router.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
