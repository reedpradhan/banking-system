# This file inserts a test account into the accounts table
import mysql.connector
from db_config import get_connection

connection = get_connection()

cursor = connection.cursor()

# Insert a sample account for testing
cursor.execute("""
INSERT INTO accounts (account_number, name, pin, balance)
VALUES (123456, 'Test User', '1234', 1000.00)
""")

connection.commit()
print("\u2705 Test account added!")

cursor.close()
connection.close()

