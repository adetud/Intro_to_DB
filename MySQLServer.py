  GNU nano 8.6                     MySQLServer.py
#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS alx_book_store"
            )
            print("Database 'alx_book_store' created successfully!")

                               [ Read 30 lines ]
^G Help      ^O Write Out ^F Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^/ Go To Line
