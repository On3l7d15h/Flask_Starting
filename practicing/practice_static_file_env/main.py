# importing important modules...
import flask;
from flask import Flask;

# initialize app
app = Flask(__name__);

# routes
@app.route("/")
def main_route():
    return flask.render_template("index.html");

@app.route("/login")
def login_route():
    return flask.render_template("login.html");

@app.route("/login/place/<name>")
def place_route(name):
    return flask.render_template("place.html", value=name);

@app.route("/logout")
def logout_route():
    return flask.redirect(flask.url_for("main_route"))

# running our app!
if __name__ == "__main__":
    app.run(debug=True)
