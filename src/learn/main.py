from fastapi import FastAPI

from src.learn.ch_19.router import router as ch_19_router
from src.learn.ch_20.router import router as ch_20_router
from src.learn.ch_21.router import router as ch_21_router

app = FastAPI()
app.include_router(ch_19_router)
app.include_router(ch_20_router)
app.include_router(ch_21_router)
