from fastapi import FastAPI
from routes import user_cred
from database import db

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    
app.include_router(user_cred.router)