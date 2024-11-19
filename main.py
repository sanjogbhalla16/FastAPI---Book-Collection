from fastapi import FastAPI
from routes import user_cred
from database import db

app = FastAPI()
#this is basically used to run db on and off

@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    
app.include_router(user_cred.router, prefix="/user_cred", tags=["user_cred"])