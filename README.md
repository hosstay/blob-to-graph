# Blob Data to Graph Example

Takes a byte encoded hex string blob which represents 601 distinct data points
from MySql, converts it to its 32 signed integer representation and plots
it. It does this for each record and then repeats.

## Getting Started

### Database

Import included test_data.sql dump to get table and data.

### Installing

* Install MySql v5.7.21
* Install Python (I used 3.7)
* Install MySql/Python Connector (pip install mysql-connector-python)
* Install Matplotlib (pip install matplotlib)
* Clone this repository
* Import test_data.sql into MySql database
* Change connection information in connect function to connect to your database
  I used:
    host='localhost',
    database='lp_test',
    user='root',
    password='password'

## Deployment

In some CLI (I used Powershell) run 'python lp_test.py'
Ctrl + C in Powershell to exit

## Built With

* [Python](https://www.python.org/) - Main Language
* [MySql](https://www.mysql.com/) - Database
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - Integration between Python and Mysql
* [Matplotlib](https://matplotlib.org/) - Python Module for Graphing

## Authors

* **Taylor Hoss** - [hosstay](https://github.com/hosstay)

## Other Credits

Based on SWE prompt by LP Technologies

## Goal

The Test was to be completed within 4 hours. While making it I ran a timer
and collected how long it too me to complete the various tasks

Installing MySql/Python: 39 minutes (39)

Importing dump file into MySql: 16 minutes (55)

Getting data into Python from MySql: 27 minutes (82)

Convert BLOB data to list of 32 bit signed integers: 55 minutes (137)

Find and install graphing module, get each blob to print each sec: 36 minutes (173)

Add timestamps, cleanup code, write more comments: 25 minutes (198)

Write README: 25 minutes (223)

---

Time Usage (223/240)