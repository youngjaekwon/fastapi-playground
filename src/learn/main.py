from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.learn.ch_19.router import router as ch_19_router
from src.learn.ch_20.router import router as ch_20_router
from src.learn.ch_21.router import router as ch_21_router
from src.learn.ch_22.router import router as ch_22_router
from src.learn.ch_23.router import router as ch_23_router
from src.learn.ch_24.router import (
    router as ch_24_router,
    unicorn_exception_handler,
    UnicornException,
    validation_exception_handler,
    custom_http_exception_handler,
)

app = FastAPI()
app.include_router(ch_19_router)
app.include_router(ch_20_router)
app.include_router(ch_21_router)
app.include_router(ch_22_router)
app.include_router(ch_23_router)
app.include_router(ch_24_router)
app.exception_handler(UnicornException)(unicorn_exception_handler)
app.exception_handler(StarletteHTTPException)(custom_http_exception_handler)
app.exception_handler(RequestValidationError)(validation_exception_handler)
