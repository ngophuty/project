from pydantic import BaseModel, validator
from typing import Optional
from fastapi.exceptions import HTTPException


class CreateUser(BaseModel):
    email: str
    username: str
    password: str
    re_password: str

    @validator('re_password')
    def validate_password(cls, value, values):
        username = values.get('username')
        if any(not c.isalnum() for c in username):
            raise HTTPException(
            detail="username must be not contain spaces or special characters",
            status_code= 400
            )
        if len(values.get('password')) < 6 :
            raise HTTPException(
            detail="password at least 6 characters",
            status_code= 200
            )
        if value != values.get('password'):
            raise HTTPException(
            detail="password do not match",
            status_code= 200
            )