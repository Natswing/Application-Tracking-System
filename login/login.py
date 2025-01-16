from database.mysql_reader_and_writer import *
from utility.utils import *
import datetime
from loguru import logger


def user_login_logic(user_input):
    email=user_input['email']
    password=user_input['password']
    select_query=f''' select id,username from user_info where email = '{email}' and password = '{password}' '''
    user_details=mysql_connection_obj.reader(select_query)
    logger.info(user_details)
    result = login_checker(user_details[0]['username'],password)
    if len(result)==0:
        return {"Message": "Invalid email or password"}
    else:
        return {"Message": "Login Succesful"}
