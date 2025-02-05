from fastapi import FastAPI

from src.learn.ch_19.router import router as ch_19_router

app = FastAPI()
app.include_router(ch_19_router)
