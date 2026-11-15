# This script handles logging a user into the banking system
import mysql.connector
from db_config import get_connection

def login():
    print("Welcome to my very own Banking System! ")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    connection = get_connection()

    cursor = connection.cursor() # Connect to the database

    # Verify the account number and PIN
    query = "SELECT * FROM accounts WHERE account_number = %s AND pin = %s"
    cursor.execute(query, (account_number, pin))

    account = cursor.fetchone() # Fetch the account details

    if account:
        print(f"\u2705 Welcome, {account[1]}!")
        return account_number
    else:
        print("\u274C Invalid account number or PIN.")
        return None

    cursor.close()
    connection.close()

# Login function can be called from other scripts
if __name__ == "__main__":
    login()