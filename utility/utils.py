from database.mysql_reader_and_writer import *
from loguru import logger

def login_checker(username,password):
    logger.info(mysql_connection_obj)
    select_query =f"select * from user_info where username = '{username}' and password ='{password}'"
    rows=mysql_connection_obj.reader(select_query)
    return rows