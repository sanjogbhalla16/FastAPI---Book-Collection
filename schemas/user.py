# this will help,  Pydantic is the most widely used data validation library for Python.
from pydantic import BaseModel , EmailStr


class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    

