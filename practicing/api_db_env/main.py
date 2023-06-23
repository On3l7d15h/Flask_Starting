import flask;
import sqlite3 as sql;
import json;
from flask import Flask;

#
app = Flask(__name__);

#
@app.route("/api/get")
def main_route():
    return "USERS API MAIN";

@app.route("/api/get/users")
def get_users_route():
    
    ans = []

    try:

        with sql.connect("database.db") as conn:

            cur = conn.execute("SELECT * FROM users;");
            ans = cur.fetchall();

    except:
        conn.rollback();
        print("Error... please check your code.")

    finally:
        conn.close();

    return ans;

# 
if __name__ == "__main__":
    app.run(debug=True)