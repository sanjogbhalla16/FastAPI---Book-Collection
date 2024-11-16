# here we write the code to hash the password
from passlib.context import CryptContext
from jose import jwt
from config import JWT_SECRET_KEY

# Configure CryptContext to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# This will hash the password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str)-> bool:
    return pwd_context.verify(password, hashed_password)

def create_access_token(data: dict) -> str:
    return jwt.encode(data, JWT_SECRET_KEY, algorithm="HS256")
    