# Banking System

A simple banking app that runs in the terminal. It is written in Python and uses a MySQL database.

You log in with an account number and a PIN. Then you can check your balance, deposit money, and withdraw money.

> This is a learning project. It is not for real money. See [Known Limits](#known-limits).

## Features

- Log in with an account number and PIN
- Check your balance
- Deposit money
- Withdraw money (blocked if you do not have enough funds)
- Friendly messages with ✅ and ❌ icons
- Code split into small files, each with one job

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

- Python 3.8 or newer
- MySQL Server, running on your computer
- The `mysql-connector-python` package

## Project Files

| File | What it does |
| --- | --- |
| `banking_system_funcs.py` | The main app. Shows the menu and handles balance, deposit, and withdraw. |
| `login_stuff.py` | Asks for the account number and PIN. Checks them in the database. |
| `create_tables.py` | Makes the `accounts` table. |
| `seed_data.py` | Adds one test account so you can try the app. |
| `db_test.py` | Checks that Python can connect to MySQL. |

## Setup

### 1. Get the code

```bash
git clone https://github.com/Rybes10/banking-system.git
cd banking-system
```

### 2. Install the MySQL package

```bash
pip install mysql-connector-python
```

### 3. Make the database

Open MySQL and run this:

```sql
CREATE DATABASE banking_system;
```

### 4. Set your MySQL password

Each Python file connects to MySQL. Open these files and put in **your own** MySQL username and password:

- `banking_system_funcs.py`
- `login_stuff.py`
- `create_tables.py`
- `seed_data.py`
- `db_test.py`

Look for this block in each file:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD_HERE",
    database="banking_system"
)
```

### 5. Test the connection (optional)

```bash
python db_test.py
```

You should see: `✅ Successfully connected to MySQL database!`

### 6. Make the table and add a test account

```bash
python create_tables.py
python seed_data.py
```

Run `seed_data.py` only once. Running it again will fail, because the account number already exists.

## Run the App

```bash
python banking_system_funcs.py
```

Use the test account to log in:

| Account Number | PIN | Starting Balance |
| --- | --- | --- |
| `123456` | `1234` | $1000.00 |

## How It Works

1. `banking_system_funcs.py` starts and calls `login()` from `login_stuff.py`.
2. `login()` checks your account number and PIN in the `accounts` table.
3. If they match, the main menu appears. If not, the app stops.
4. Each menu choice runs one function. It opens a connection, runs one SQL query, and closes the connection.
5. Choosing `4` exits the app.

### Database Table

The `accounts` table has these columns:

| Column | Type | Meaning |
| --- | --- | --- |
| `account_number` | `INT` (primary key) | The unique account ID |
| `name` | `VARCHAR(100)` | The account holder's name |
| `pin` | `VARCHAR(10)` | The PIN used to log in |
| `balance` | `DECIMAL(10, 2)` | The money in the account |

## Known Limits

This project is for learning. Here are the things that are not safe or finished yet:

- **PINs are stored as plain text.** A real bank would hash them.
- **The database password is written inside the code.** It is better to store it in an environment variable or a `.env` file.
- **There is no input checking.** Typing letters instead of a number for an amount will crash the app. Negative amounts are not blocked.
- **There is no login attempt limit.** Someone could keep guessing PINs.
- **There is no transaction history.** The app only keeps the current balance.
- **There is only one login attempt.** If it fails, the app exits.

## Ideas for the Future

- [ ] Move database settings to a `.env` file
- [ ] Hash PINs with `bcrypt`
- [ ] Check that amounts are positive numbers
- [ ] Add a `transactions` table and a history option
- [ ] Add transfers between accounts
- [ ] Add a way to create new accounts
- [ ] Lock an account after too many wrong PINs
- [ ] Use one shared connection helper instead of repeating the code

## Author

Made by [Reeddhiman Pradhan](https://github.com/reedpradhan).
