# One place for the database settings.
# The password is read from an environment variable. Never write it in the code.
import os
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ["DB_PASSWORD"],
        database=os.environ.get("DB_NAME", "banking_system"),
    )
