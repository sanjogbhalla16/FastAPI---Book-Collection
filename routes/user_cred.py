# here we will create routes for user cred
from prisma import Prisma
from typing import Union
from fastapi import FastAPI
from schemas import userCreate , userResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}