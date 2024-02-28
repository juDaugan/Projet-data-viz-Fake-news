import pandas as pd
import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="db", user="user", password="password", host="host", port="port")

cur = conn.cursor()

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO table_name (column1, column2, column3, column4) VALUES (%s, %s, %s, %s)",
            row
        )

conn.commit()

cur.close()
conn.close()