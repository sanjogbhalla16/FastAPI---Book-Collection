# here we will create routes for user cred
#APIRouter class, used to group path operations, for example to structure an app in multiple files. It would then be included in the FastAPI app, or in another APIRouter
from prisma import Prisma
from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from schemas import UserCreate , UserResponse
from models import User
from hash_pwd import hash_password, verify_password , create_access_token
from database import db

router = APIRouter()

@router.post("/login")
async def login(User:UserCreate):
    user = await db.User.find_unique(where={"email":User.email})
    if not user or not verify_password(user.password, User.password):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    access_token = create_access_token({"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserResponse)
async def register(User:UserCreate):
    existing_user = await db.User.find_unique(where={"email":User.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hash_password = hash_password(User.password)
    user = await db.User.create(data={"username":User.username, "email":User.email, "password":hash_password})
    return user