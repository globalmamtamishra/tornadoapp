import pymysql.cursors

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='shopping_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
