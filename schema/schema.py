from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class SignupBody(BaseModel):
    username:str
    password:str
    email:str
    role:str 
    