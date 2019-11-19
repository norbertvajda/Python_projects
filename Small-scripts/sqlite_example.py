#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

cursor = conn.execute("SELECT customer_ID, customer_name, address FROM customers")

for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Address = ", row[2], "\n")

print("Operation done successfully")

conn.close()
