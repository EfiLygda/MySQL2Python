import os
import re
import argparse

# ----------------------------------------------------------------------------------------------------------------------
# --- Building Command ---

# Defining the argument parser for the command
parser = argparse.ArgumentParser()

# SQL file name
parser.add_argument('--sql_filename', '-sql',
                    help='(str) SQL File Name',
                    type=str,
                    required=True)

# MySQL username
parser.add_argument('--username', '-u',
                    help='(str) MySQL Username',
                    type=str,
                    required=True)

# MySQL password
parser.add_argument('--password', '-pwd',
                    help='(str) MySQL password',
                    type=str,
                    required=True)

# MySQL host name
parser.add_argument('--host', '-host',
                    help='(str) MySQL host name.',
                    type=str,
                    required=True)

# Python script directory name
parser.add_argument('--python_directory', '-pdir',
                    help='(str) Python directory name.',
                    type=str,
                    required=True)

# Python script file name
parser.add_argument('--python_filename', '-pname',
                    help="""(str) Python script filename. 
                    In case none is given the original SQL file's name will be used.""",
                    type=str)


# Parse arguments to extract user inputs
args = parser.parse_args()
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# --- Preparing User Inputs for Command ---

# SQL file path
SQL_DIR = './'
SQL_FILENAME = args.sql_filename
SQL_FILE = os.path.join(SQL_DIR, SQL_FILENAME)

# Python script file path
PYTHON_DIR = args.python_directory

# In case no name was given for the script, then the original SQL file's name will be used
if args.python_filename:
    PYTHON_FILENAME = args.python_filename
else:
    PYTHON_FILENAME = SQL_FILENAME.replace('.sql', "") + '.py'

PYTHON_FILE = os.path.join(PYTHON_DIR, PYTHON_FILENAME)
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# --- Extract the queries ---

# Open SQL file and extract all text
with open(SQL_FILE, 'r') as f:
    text = f.read()

# RegEx for extracting the queries
QUERY = r'(?:USE|SELECT|WITH).*?;'

# Explanation:
# 1. `(?:USE|SELECT|WITH)`: Match USE or SELECT or WITH but as non-capturing group, meaning do not return only them
# 2. `.*?`: Match as many characters as you can after the before-mentioned group.
# 3. `;`: Stop at ; and capture it.

# TODO: Expand the pattern for all SQL commands

# Find all queries using the pattern
queries = re.findall(QUERY, text, re.DOTALL)

# Open python file for writing the code
with open(PYTHON_FILE, 'w') as p:

    # Write preliminary code for connecting to the MySQL database
    p.write(f"""import mysql.connector

# Define MySQL connector
mydb = mysql.connector.connect(
  host='{args.host}',
  user='{args.username}',
  password='{args.password}'
)

# Define MySQL cursor
cursor = mydb.cursor()
    """)
    p.write(2 * '\n')

    # Write the queries inside the cursor.execute() method
    for q in queries:
        p.write(f'cursor.execute("""\n{q}\n""")')
        p.write(2*'\n')
# ----------------------------------------------------------------------------------------------------------------------

# TODO: Give options for other databases, other than MySQL

print(f"\n\nScript is located at: {os.path.abspath(PYTHON_FILE)}\n\n")
