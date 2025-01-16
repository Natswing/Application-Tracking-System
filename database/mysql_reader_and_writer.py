from loguru import logger
import mysql.connector

class MySqlConnection:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password=password
        self.database=database
        self.connection=mysql.connector.connect(host=self.host,
                                    user=self.user,
                                    password =self.password,
                                    database = self.database)
    def reader(self,query):
        logger.info(f"Running query {query}")
        cursor=self.connection.cursor()
        result=cursor.execute(query)
        # rows=cursor.fetchall()
        results = [dict(zip([column[0] for column in cursor.description], row)) 
                    for row in cursor.fetchall()]
        return results
    
    def writer(self, query):
        logger.info(f'Running query: {query}')
        cursor = self.connection.cursor()
        cursor.execute(query)
        affected_rows = cursor.rowcount  # Number of rows affected by the query
        self.connection.commit()
        cursor.close()

        if affected_rows > 0:
            logger.info("Query ran successfully")
            return {'message':"Query ran successfully"}  # Return the number of affected rows
        else:
            logger.warning("No rows were affected by the query")
            return 0



mysql_connection_obj = MySqlConnection(host="localhost",user='root',password='12345',
                    database='app_track_sys')
