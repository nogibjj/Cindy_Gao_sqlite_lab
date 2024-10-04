"""
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/murder_2015_final.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("Murder2015.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Murder2015")
    c.execute("CREATE TABLE Murder2015 (city,state,murders_2014,murders_2015,change)")
    # insert
    c.executemany("INSERT INTO Murder2015 VALUES (?,?,?,?,?)", payload)
    conn.commit()
    conn.close()
    return "Murder2015.db"
