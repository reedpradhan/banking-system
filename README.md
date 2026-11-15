# Banking System

A simple banking app that runs in the terminal. It is written in Python and uses a MySQL database.

You log in with an account number and a PIN. Then you can check your balance, deposit money, and withdraw money.

> This is a learning project. It is not for real money. See \[Known Limits](#known-limits).

## Features

* Log in with an account number and PIN
* Check your balance
* Deposit money
* Withdraw money (blocked if you do not have enough funds)
* Friendly messages with ✅ and ❌ icons
* Code split into small files, each with one job

## How It Looks

```
Welcome to my very own Banking System!
Enter your account number: 123456
Enter your PIN: 1234
✅ Welcome, Test User!
-------- Main Menu ---------
1. Check balance
2. Deposit
3. Withdraw
4. Exit
Select an option: 1
✅ Your balance is $1000.00
```

## What You Need

* Python 3.8 or newer
* MySQL Server, running on your computer
* The `mysql-connector-python` package

## Project Files

|File|What it does|
|-|-|
|`db\_config.py`|Makes the database connection. It reads the settings from environment variables.|
|`banking\_system\_funcs.py`|The main app. Shows the menu and handles balance, deposit, and withdraw.|
|`login\_stuff.py`|Asks for the account number and PIN. Checks them in the database.|
|`create\_tables.py`|Makes the `accounts` table.|
|`seed\_data.py`|Adds one test account so you can try the app.|
|`db\_test.py`|Checks that Python can connect to MySQL.|
|`requirements.txt`|The list of Python packages.|
|`.gitignore`|Tells Git to skip private files like `.env`.|

## Setup

### 1\. Get the code

```bash
git clone https://github.com/Rybes10/banking-system.git
cd banking-system
```

### 2\. Install the MySQL package

```bash
pip install -r requirements.txt
```

### 3\. Make the database

Open MySQL and run this:

```sql
CREATE DATABASE banking\_system;
```

### 4\. Set your MySQL password

The app reads your MySQL password from an environment variable. **Never write it in the code.**

Windows (PowerShell):

```powershell
$env:DB\_PASSWORD="your-mysql-password"
```

Mac or Linux:

```bash
export DB\_PASSWORD="your-mysql-password"
```

You must do this in every new terminal window.

Optional settings. These have defaults, so you can skip them:

|Variable|Default|
|-|-|
|`DB\_HOST`|`localhost`|
|`DB\_USER`|`root`|
|`DB\_NAME`|`banking\_system`|

### 5\. Test the connection (optional)

```bash
python db\_test.py
```

You should see: `✅ Successfully connected to MySQL database!`

### 6\. Make the table and add a test account

```bash
python create\_tables.py
python seed\_data.py
```

Run `seed\_data.py` only once. Running it again will fail, because the account number already exists.

## Run the App

```bash
python banking\_system\_funcs.py
```

Use the test account to log in:

|Account Number|PIN|Starting Balance|
|-|-|-|
|`123456`|`1234`|$1000.00|

## How It Works

1. `banking\_system\_funcs.py` starts and calls `login()` from `login\_stuff.py`.
2. `login()` checks your account number and PIN in the `accounts` table.
3. If they match, the main menu appears. If not, the app stops.
4. Each menu choice runs one function. It opens a connection, runs one SQL query, and closes the connection.
5. Choosing `4` exits the app.

### Database Table

The `accounts` table has these columns:

|Column|Type|Meaning|
|-|-|-|
|`account\_number`|`INT` (primary key)|The unique account ID|
|`name`|`VARCHAR(100)`|The account holder's name|
|`pin`|`VARCHAR(10)`|The PIN used to log in|
|`balance`|`DECIMAL(10, 2)`|The money in the account|

## Known Limits

This project is for learning. Here are the things that are not safe or finished yet:

* **PINs are stored as plain text.** A real bank would hash them.
* **There is no input checking.** Typing letters instead of a number for an amount will crash the app. Negative amounts are not blocked.
* **There is no login attempt limit.** Someone could keep guessing PINs.
* **There is no transaction history.** The app only keeps the current balance.
* **There is only one login attempt.** If it fails, the app exits.

## Ideas for the Future

* \[ ] Hash PINs with `bcrypt`
* \[ ] Check that amounts are positive numbers
* \[ ] Add a `transactions` table and a history option
* \[ ] Add transfers between accounts
* \[ ] Add a way to create new accounts
* \[ ] Lock an account after too many wrong PINs
* \[ ] Make a separate MySQL user for the app, so it does not use `root`

## Author

Made by [Reeddhiman Pradhan](https://github.com/reedpradhan).

