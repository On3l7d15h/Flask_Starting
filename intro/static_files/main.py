import flask;
from flask import Flask, render_template;

# initialize app
app = Flask(__name__);

@app.route("/")
def main_route():
    return "Hello World!"

@app.route("/<name>")
def display_name(name: str):
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)