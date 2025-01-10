from fastapi import HTTPException
from database.mysql_reader_and_writer import *
from utility.utils import *
from loguru import logger

def user_signup_logic(user_input):
    logger.info(f"{user_input}")
    username=user_input['username']
    password=user_input['password']
    result = login_checker(username,password)
    logger.info(f"{len(result)}")
    if len(result)!=0:
        raise HTTPException(status_code=406, detail="User already exists.")
    else:
        logger.info("Inserting data into table.")
        insert_query=f"insert into "
        MySqlConnection.writer()
        return {"Message": "Signup Succesful"}