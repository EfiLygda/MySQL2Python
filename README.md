# MySQL2Python
Simple script for converting MySQL code to a Python script. Run from the command line.

--------------

## Requirements

```
python==3.8.18
```

## Usage

**Step 1:** Download the Python script `MySQL2Python.py`.

**Step 2:** Navigate to the directory of the SQL file through the command line (i.e. using `cd`).

**Step 3:** For Windows users, run the command as:
```
py /path/to/script/MySQL2Python.py -sql SQL_filename.sql -u username -pwd password -host hostname
```
The new script will then be created in the same directory as the original SQL file.


In case of wanting to add another directory for the new script then use the -pdir argument, as below: 
```
py /path/to/script/MySQL2Python.py -sql SQL_filename.sql -u username -pwd password -host hostname -pdir /directory/for/script
```

And for naming the script:
```
py /path/to/script/MySQL2Python.py -sql SQL_filename.sql -u username -pwd password -host hostname -pdir /directory/for/script -pname new_code.py
```


## Help

```
usage: MySQL2Python.py [-h] --sql_filename SQL_FILENAME --username USERNAME --password PASSWORD --host HOST --python_directory
               PYTHON_DIRECTORY [--python_filename PYTHON_FILENAME]

options:
  -h, --help            show this help message and exit
  --sql_filename SQL_FILENAME, -sql SQL_FILENAME
                        (str) SQL File Name
  --username USERNAME, -u USERNAME
                        (str) MySQL Username
  --password PASSWORD, -pwd PASSWORD
                        (str) MySQL password
  --host HOST, -host HOST
                        (str) MySQL host name.
  --python_directory PYTHON_DIRECTORY, -pdir PYTHON_DIRECTORY
                        (str) Python directory name.
  --python_filename PYTHON_FILENAME, -pname PYTHON_FILENAME
                        (str) Python script filename. In case none is given the original SQL file's name will be used.

```
