import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = "",
                            db = "Chinook") 

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        for row in cursor:
            print(row)                             
finally:
    connection.close()        