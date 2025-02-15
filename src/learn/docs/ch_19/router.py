from fastapi import APIRouter, status

router = APIRouter(prefix="/ch-19", tags=["ch.19"])


@router.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
