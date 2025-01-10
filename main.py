from typing import Union
from loguru import logger
from fastapi import FastAPI
from schema.schema import *
from signup.signup import *
import uvicorn

app = FastAPI()

@app.post("/candidates")
def new_user_signup(user_data:SignupBody):
    user_data=user_data.model_dump()
    logger.info(type(user_data))
    result=user_signup_logic(user_data)
    return result

