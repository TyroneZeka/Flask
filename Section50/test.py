import sqlite3
from sqlite3.dbapi2 import SQLITE_INSERT

# Initialize a connection 
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1,'Chama', 'Password')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query,user)

users = [
    (1,'Chama', 'Password'),
    (2,'Chamat', 'Pass')
]
cursor.executemany(insert_query,users)


select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()