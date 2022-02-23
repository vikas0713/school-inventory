"""
All the project related configuration will be included in this file
"""
import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'db_school'


def get_db_cursor():
    """Create connection and return db cursor"""
    connection = mysql.connector.connect(
        host=MYSQL_HOST, user=MYSQL_USER, database=MYSQL_DATABASE
    )
    return connection
