# This file basically connects to MySQL and creates the 'accounts' table
import mysql.connector
from db_config import get_connection

# Establish connection to MySQL
connection = get_connection()

cursor = connection.cursor()

# Create table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_number INT PRIMARY KEY,
    name VARCHAR(100),
    pin VARCHAR(10),
    balance DECIMAL(10, 2)
)
""")

connection.commit()  # Save the changes
print("\u2705 Table 'accounts' created successfully!")

cursor.close()
connection.close()

