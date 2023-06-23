# importing flask
from flask import Flask;

# initialize our project in Flask. 
app = Flask(__name__);

# we can do more routes and bindings also.
@app.route("/")
def main_route():
    return "Main"

@app.route("/hello")
def wave_route():
    return "Hello new User"

if __name__ == "__main__":
    app.run();