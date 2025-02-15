from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/ch-33", tags=["ch.33"])


class DBSession:
    def close(self):
        pass


async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


class DependencyA:
    def some_function(self):
        pass

    def close(self):
        pass


class DependencyB:
    def some_function(self):
        pass

    def close(self, dep_a: DependencyA):
        dep_a.some_function()


class DependencyC:
    def close(self, dep_b: DependencyB):
        dep_b.some_function()


def generate_dep_a():
    dep_a = DependencyA()
    return dep_a


def generate_dep_b():
    dep_b = DependencyB()
    return dep_b


def generate_dep_c():
    dep_c = DependencyC
    return dep_c


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a: Annotated[DependencyA, Depends(generate_dep_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b: Annotated[DependencyB, Depends(generate_dep_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)


data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}


class OwnerError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Owner error: {e}"
        )
        # print("error")
        # raise


@router.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item


class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db
