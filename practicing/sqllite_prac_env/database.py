# import
import sqlite3;

# 
conn = sqlite3.connect("database.db")
try:
    print("Bookstore v1.0: Open and created database!")

    conn.cursor();
    conn.execute("CREATE TABLE books (title TEXT, author TEXT, year TEXT)")
    print("Bookstore v1.0: Created Table Successfully!")

except:
    print("Bookstore Error...")
finally:
    conn.close()