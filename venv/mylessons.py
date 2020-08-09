from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Hello</h1>"
@app.route("/user/<Lee>")
def user(Lee):
    return "<h1>Hello %s </h1>"   % Lee
    