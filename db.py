import mysql.connector as mysql
from flask import Flask
from mysql.connector.pooling import PooledMySQLConnection


def get_connection(app: Flask):
    try:
        db_conn = mysql.connect(
            host=app.config['DB_HOST'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            database=app.config['DB_NAME'],
            port=app.config['DB_PORT']
        )
        return db_conn
    except mysql.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def close_connection(db_connection: PooledMySQLConnection):
    db_connection.close()
