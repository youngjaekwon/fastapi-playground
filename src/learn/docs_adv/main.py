from fastapi import FastAPI

from src.learn.docs_adv import ch_01

app = FastAPI()

app.include_router(ch_01.router)
