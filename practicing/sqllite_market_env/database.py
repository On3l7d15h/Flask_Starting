import sqlite3 as sql;

try:
    # creating our database, tables and so forth!
    conn = sql.connect("database.db")
    print("Database created successfully!")

    # creating our tables
    conn.execute("CREATE TABLE meals (id_meal INTEGER PRIMARY KEY, name TEXT, category TEXT, image TEXT)");
    conn.commit();
    print("Table meals created successfully!")

    # creating table category
    conn.execute("CREATE TABLE category_meal (id INTEGER PRIMARY KEY, alias TEXT)");
    conn.commit();
    print("Table category_meal created successfully!")

    # filling table
    conn.execute("INSERT INTO category_meal(alias) VALUES ('Fast food'), ('For launch'), ('Healthy')")
    conn.commit();
    print("Values inserted in the category_meals!")

except:
    print("Error... please check the code.")

finally:
    # closing the connection
    conn.close();