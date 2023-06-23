import sqlite3;

# making connection
conn = sqlite3.connect("database.db")
print("connected!")

# more actions
conn.execute("CREATE TABLE student ( name TEXT, surname TEXT, country TEXT )");
print("created!")

conn.close();