#
import flask;
import sqlite3 as sql;
from flask import Flask;

#
app = Flask(__name__);

#
@app.route("/")
def main_route():
    return flask.render_template("index.html");

@app.route("/list")
def list_route():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row
    cur = conn.cursor();
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall();
    print(rows)
    return flask.render_template("list.html", rows=rows);

@app.route("/newrec", methods=["GET", "POST"])
def create_route():
    msg = "";
    if flask.request.method == "POST":
        try:
            tt = flask.request.form["tt"];
            at = flask.request.form["at"];
            yr = flask.request.form["yr"];
        
            with sql.connect("database.db") as conn:
                conn.cursor();
                conn.execute("INSERT INTO books VALUES (?, ?, ?)", (tt, at, yr));
                conn.commit();
                msg = "Created successfully!!"
        except:
            conn.rollback()
            msg = "Oops... Problems with the creation... please try again."
        finally:
            conn.close();
        return flask.render_template("msg.html", msg=msg);
    else:
        return flask.render_template("newrec.html")


#
if __name__ == "__main__":
    app.run(debug=True);