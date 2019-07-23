import os
import pymysql
import getpass
import cryptography

username = getpass.getuser()

connection = pymysql.connect(
    host='localhost', user='root', password='', db='Chinook')


try:
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
