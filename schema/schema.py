from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr,field_validator
from typing import Optional

class SignupBody(BaseModel):
    username: str = Field(..., description="Username is required")
    password: str = Field(..., min_length=8, max_length=20, description="Password must be 8-20 characters long")
    email:EmailStr
    role:str
    phone:Optional[str]=None 

    @field_validator("phone")
    def validate_phone(cls, value: Optional[str]) -> Optional[str]:
        if value and (not value.isdigit() or len(value) != 10):
            raise ValueError("Phone number must be exactly 10 digits.")
        return value
    

class LoginBody(BaseModel):
    email:EmailStr
    password:str

class OptionalFilters(BaseModel):
    name:Optional[str]
    role:Optional[str]

class CandidateSchema(BaseModel):
    id: int
    username: str
    email: str
    role: str
    phone:Optional[str]

class UpdateBody(BaseModel):
    username:Optional[str]=""
    password:Optional[str]=""
    email:Optional[str]=""
    role:Optional[str]=""
    phone:Optional[str]=""


