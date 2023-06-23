# import Flask
import flask;
from flask import Flask;

# initiliaze app
app = Flask(__name__);

# our routes with binding
# we are going to simulate we are doing a login...

@app.route("/")
def main_route():
    return "Hello user!\nWelcome to our program";

@app.route("/admin/<name>")
def admin_route(name):
    return f"Hello {name}, we're glad to see you here as a admin"

@app.route("/guest/<name>")
def guest_route(name):
    return f"Hello {name}, we're glad to see you here as a guest"

@app.route("/login/<name>")
def login_route(name):
    if name != "Onell":
        return flask.redirect(flask.url_for("guest_route", name=name))
   

    return flask.redirect(flask.url_for("admin_route", name=name))

# starting our application:

if __name__ == "__main__":
    app.run(debug=True)

