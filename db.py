import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='coffee_order_platform'
    )
