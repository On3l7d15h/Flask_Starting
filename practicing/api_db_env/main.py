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

@app.route("/api/get/users/<id>")
def get_specific_user(id):
     
    ans = [];

    try:
        with sql.connect("database.db") as conn:
            cur = conn.execute("SELECT * FROM users WHERE id = ?", (id));
            ans = cur.fetchall();
    except:
        conn.rollback();
        print("Error... please check your code.")
    finally:
        conn.close()

    if len(ans) == 0:
        return "There is not a register with that id";
    
    return ans;

@app.route("/api/get/users/<id>/update", methods=['POST'])
def update_specific_user(id: int):
    utu = flask.request.get_json();
    was_updated = False;

    try:
        with sql.connect("database.db") as conn:
            conn.execute("UPDATE users SET name = ?, last = ?, title = ? WHERE id = ?;", (utu['name'], utu['last'], utu['title'], id))
        was_updated = True;
    except:
        conn.rollback();
        print("Error... please check your code.")
    finally:
        conn.close();

    return "Updated Successfully" if was_updated else "Oops! Try again later..."

@app.route("/api/get/users/<id>/delete", methods=['POST'])
def delete_specific_user(id: int):
    utd = flask.request.get_json();
    was_deleted = False;

    if utd["answer"] == 'NO':
        return "You decided to not delete this register!"

    try:
        with sql.connect("database.db") as conn:    
            conn.execute("DELETE FROM users WHERE id = ?;", (id))
            conn.commit();
            was_deleted = True;
    except:
        conn.rollback();
        print("Error...  please check your code.")
    finally:
        conn.close();

    return "Deleted Successfully" if was_deleted else "Oops! The server have had problems with your request!";

@app.route("/api/post/newuser", methods=["POST"])
def create_user_route():
    new_user = flask.request.get_json();
    was_created = False;

    try:
        with sql.connect("database.db") as conn:
            conn.execute("INSERT INTO users(name, last, title) VALUES(?, ?, ?)", (new_user["name"], new_user["last"], new_user["title"]));
            conn.commit();
            was_created = True;
    except:
        conn.rollback();
        print("Error... please check your code.")
    finally:
        conn.close();
    
    return "Created Successfully" if was_created else "Oops! try again later, we had some troubles..."

# 
if __name__ == "__main__":
    app.run(debug=True, port=7000)
