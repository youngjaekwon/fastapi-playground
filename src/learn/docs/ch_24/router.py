from fastapi import APIRouter, HTTPException, status, Request
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


"""
FastAPI의 HTTPException과 Starlette의 HTTPException의 차이
- fast api 쪽은 detail에 json으로 변환 가능한 모든 값을 전달 가능
- starlette는 str만 가능
"""


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )


async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request=request, exc=exc)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request=request, exc=exc)


router = APIRouter(prefix="/ch-24", tags=["ch.24"])


items = {"foo": "The Foo Wrestlers"}


class Item(BaseModel):
    title: str
    size: int


@router.post("/items/")
async def create_item(item: Item):
    return item


@router.get("/items/{item_id}")
async def ream_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return {"item": items[item_id]}


@router.get("/items/{item_id}/without-three")
async def read_item_without_three(item_id: int):
    if item_id == 3:
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT, detail="Nope! I don't like 3."
        )
    return {"item_id": item_id}


@router.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


@router.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
