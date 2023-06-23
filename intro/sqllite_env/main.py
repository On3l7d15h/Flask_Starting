#
import flask;
import sqlite3 as sql;
from flask import Flask;

# 
app = Flask(__name__);

@app.route("/")
def main_route():
    return flask.render_template("index.html")

@app.route("/list")
def list_route():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row;

    cur = conn.cursor();
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall();

    return flask.render_template("list.html", rows=rows)

@app.route("/newrec", methods=["GET", "POST"])
def create_route():
    if flask.request.method == "POST":

        try:
            nm = flask.request.form["nm"];
            sm = flask.request.form["sm"];
            ct = flask.request.form["ct"];
        
            with sql.connect("database.db") as conn:
                conn.cursor();
                conn.execute("INSERT INTO student VALUES (?, ?, ?)", (nm, sm, ct));
                conn.commit();
                print("Excellent")

        except:
            conn.rollback()
            print(f"Problem")
        finally:
            conn.close();

        return flask.redirect(flask.url_for("main_route"))
    else:
        return flask.render_template("newrec.html")

#
if __name__ == "__main__":
    app.run(debug=True)