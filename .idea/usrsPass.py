from pprint import pprint
import sqlite3

conn = sqlite3.connect('example.db')

# Create table
# conn.execute('''CREATE TABLE users
#          (username text, lastname text, phone text)''')

c = conn.cursor()

with open('/tmp/ksiazka-adresowa.json') as file:
    lines = file.readlines()

    for line in lines:
        items = line.split(':')

        # --- TEST
        #print(items[0])
        #print(items[1])
        #print(items[2])
        #print(items[3])
        # ---

        # Insert a row of data
        #query =  "INSERT INTO users VALUES ('{username}','{lastname}','{phone}')".format(username=items[0], lastname=items[1], phone=items[2])
        query = "INSERT INTO users VALUES ('{username}','{phone}','{lastname}')".format(username=items[0],
                                                                                        phone=items[1],
                                                                                        lastname=items[2])
        c.execute(query)

# Read table rows
query = "SELECT username, lastname, phone FROM users"
rows = c.execute(query)
pprint(list(rows))
