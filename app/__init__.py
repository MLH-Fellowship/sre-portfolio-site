import os
import json
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

from app.db import get_db

f = open("./lavina.json")
data = json.load(f)
f.close()

@app.route('/')
@app.route('/Experience/')
def index():
    return render_template('data.html',
                           data=data,
                           main="Experience",
                           side1="Projects",
                           side2="Accomplishments",
                           url=os.getenv("URL"))

@app.route('/Projects/')
def projects():
    return render_template('data.html',
                           data=data,
                           main="Projects",
                           side1="Experience",
                           side2="Accomplishments",
                           url=os.getenv("URL"))

@app.route('/Accomplishments/')
def accomplishments():
    return render_template('data.html',
                           data=data,
                           main="Accomplishments",
                           side1="Experience",
                           side2="Projects",
                           url=os.getenv("URL"))

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/health")
def health():
    return "im healthy!"

# database shenanigans

@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif db.execute(
                "SELECT id FROM user WHERE username = ?", (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418
    # TODO: return a register page
    return render_template("login.html", data=data, mode="register")

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        error = None

        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            return "Login successful", 200
        else:
            return error, 418
        # TODO: Return a login page
    return render_template("login.html", data=data, mode="login")
