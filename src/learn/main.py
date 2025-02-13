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
from src.learn.ch_25.router import router as ch_25_router
from src.learn.ch_26.router import router as ch_26_router
from src.learn.ch_27.router import router as ch_27_router
from src.learn.ch_28.router import router as ch_28_router
from src.learn.ch_29.router import router as ch_29_router
from src.learn.ch_30.router import router as ch_30_router
from src.learn.ch_31.router import router as ch_31_router
from src.learn.ch_32.router import router as ch_32_router
from src.learn.ch_33.router import router as ch_33_router
from src.learn.ch_34.router import router as ch_34_router
from src.learn.ch_37.router import router as ch_37_router, on_startup
from src.learn.ch_38.main import router as ch_38_router
from src.learn.ch_39.router import router as ch_39_router

description = """
ChimichangApp API helps you do awesome stuff.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="ChimichangApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        # "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        "identifier": "MIT",
    },
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    # docs_url="/documentation",
    redoc_url=None,
)
app.include_router(ch_19_router)
app.include_router(ch_20_router)
app.include_router(ch_21_router)
app.include_router(ch_22_router)
app.include_router(ch_23_router)
app.include_router(ch_24_router)
app.exception_handler(UnicornException)(unicorn_exception_handler)
app.exception_handler(StarletteHTTPException)(custom_http_exception_handler)
app.exception_handler(RequestValidationError)(validation_exception_handler)
app.include_router(ch_25_router)
app.include_router(ch_26_router)
app.include_router(ch_27_router)
app.include_router(ch_28_router)
app.include_router(ch_29_router)
app.include_router(ch_30_router)
app.include_router(ch_31_router)
app.include_router(ch_32_router)
app.include_router(ch_33_router)
app.include_router(ch_34_router)
app.include_router(ch_37_router)
app.on_event("startup")(on_startup)
app.include_router(ch_38_router)
app.include_router(ch_39_router)
