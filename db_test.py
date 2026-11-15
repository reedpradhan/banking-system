# Import the MySQL connector module to interact with MySQL from Python
import mysql.connector
from db_config import get_connection

try:
    # Attempt to connect to the MySQL database with the given credentials
    connection = get_connection()

    # If the connection is successful, print a success message
    if connection.is_connected():
        print("✅ Successfully connected to MySQL database!") # By the way I got the checkmark emoji from https://emojipedia.org/ and the cross mark from https://emojipedia.org/cross-mark/.

# Catch any errors that occur during the connection attempt
except mysql.connector.Error as err:
    print(f"❌ Error: {err}") # Same for the cross mark emoji, I got it from https://emojipedia.org/cross-mark/.

# Always close the connection at the end, if it was successfully created
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()  # Closes the database connection to avoid any resource leaks
