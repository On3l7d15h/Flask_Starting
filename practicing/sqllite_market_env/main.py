import flask;
from flask import Flask;
import sqlite3 as sql;

# initializing my app
app = Flask(__name__);

# routes
@app.route("/")
def main_route():
    return flask.render_template("index.html");

@app.route("/about")
def about_route():
    return flask.render_template("about.html");

@app.route("/list")
def list_route():
    rows = [];
    try:
        conn = sql.connect("database.db");
        conn.row_factory = sql.Row;
        cur = conn.execute("SELECT * FROM meals;")
        rows = cur.fetchall();
    except:
        conn.rollback();
        print("Error... please check the code...")
    finally:
        conn.close();

    if len(rows) > 0 :
        return flask.render_template("list.html", meals=rows);
    else:
        return flask.render_template("message.html", msg="Actually, yo don't have any meals here so... please... create one before come up here again.")

@app.route("/create", methods=['GET', 'POST'])
def create_route():

    # initializing our apps.
    categories = [];
    msg = "";

    if flask.request.method == 'POST':
        try:
            with sql.connect("database.db") as conn:
                nm = flask.request.form["nm"];
                ig = flask.request.form["ig"];
                ct = flask.request.form["ct"];
            
                conn.execute("INSERT INTO meals(name, image, category) VALUES(?, ?, ?)", (nm, ig, ct));
                conn.commit();
                msg = "New Meal Created Successfully"
        except:
            conn.rollback();
            msg = "Oops! Something bad happened... please try again...."
        finally:
            conn.close();
        
        return flask.render_template("message.html", msg=msg);
    else:
        try:
            with sql.connect("database.db") as conn:
                conn.row_factory = sql.Row;
                cur = conn.execute("SELECT * FROM category_meal;");
                categories = cur.fetchall();
        except:
            print("Error... please check your code...")
        finally:
            conn.close();

        
        return flask.render_template("create.html", categories=categories);

@app.route("/list/<id_meal>/update", methods=['GET', 'POST'])
def update_route(id_meal):

    # initializing our apps.
    categories = [];
    ans = [];
    msg = "";

    if flask.request.method == 'POST':
        try:
            with sql.connect("database.db") as conn:

                nm = flask.request.form["nm"];
                ig = flask.request.form["ig"];
                ct = flask.request.form["ct"];
            
                conn.execute("UPDATE meals SET name = ?, image = ?, category = ? WHERE id_meal = ?", (nm, ig, ct, id_meal));
                conn.commit();
                msg = "New Meal Updated Successfully"
        except:
            conn.rollback();
            msg = "Oops! Something bad happened... please try again...."
        finally:
            conn.close();
        
        return flask.render_template("message.html", msg=msg);
    else:

        try:
            with sql.connect("database.db") as conn:
                conn.row_factory = sql.Row;
                cur = conn.execute("SELECT * FROM category_meal;");
                categories = cur.fetchall();
        
                cur = conn.execute("SELECT * FROM meals WHERE id_meal = ?;", (id_meal))
                ans = cur.fetchall();
        except:
            print("Error... please check your code...")
        finally:
            conn.close();

        if len(ans) > 0: 
            return flask.render_template("update.html", categories=categories, meal=ans);

        return flask.render_template("message.html", msg="There is not exists a meal with that id");

@app.route("/list/<id_meal>/delete", methods=['GET', 'POST'])
def delete_route(id_meal):

     # initializing our apps.
    categories = [];
    ans = [];
    msg = "";

    if flask.request.method == 'POST':
        try:
            with sql.connect("database.db") as conn:
            
                conn.execute("DELETE FROM meals WHERE id_meal = ?", (id_meal));
                conn.commit();
                msg = "Meal Deleted! Successfully"
        except:
            conn.rollback();
            msg = "Oops! Something bad happened... please try again...."
        finally:
            conn.close();
        
        return flask.render_template("message.html", msg=msg);
    else:

        try:
            with sql.connect("database.db") as conn:
                conn.row_factory = sql.Row;
                cur = conn.execute("SELECT * FROM category_meal;");
                categories = cur.fetchall();
        
                cur = conn.execute("SELECT * FROM meals WHERE id_meal = ?;", (id_meal))
                ans = cur.fetchall();
        except:
            print("Error... please check your code...")
        finally:
            conn.close();

        if len(ans) > 0: 
            return flask.render_template("delete.html", categories=categories, meal=ans, msg=f"Do you want to delete the meal: ");

        return flask.render_template("message.html", msg="There is not exists a meal with that id");

# running our app
if __name__ == "__main__":
    app.run(debug=True);