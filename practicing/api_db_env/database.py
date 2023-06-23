import sqlite3 as sql;

try:
    conn = sql.connect("database.db");

    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, last TEXT, title TEXT)");
    conn.commit();
    print("Created Table users;")

    conn.execute("INSERT INTO users(name, last, title) VALUES (?, ?, ?)", ("Admin", "istrator", "CEO"));
    conn.commit();
    print("Admin User by Default")

except:
    conn.rollback();
    print("Oops... please check the code.")
    
finally:
    conn.close()