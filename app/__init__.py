import os
import re
import json
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.markdown import Markdown

from . import db

load_dotenv()
app = Flask(__name__)
Markdown(app)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

from app.db import get_db

f = open("./lavina.json")
data = json.load(f)
f.close()

POSTDIR = "./posts/"

@app.route("/")
@app.route("/blog/")
@app.route("/blog/<post>")
def blog(post=None):
    p = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}.+\.md$")
    posts = list(filter(p.match, os.listdir(POSTDIR)))
    posts.sort()
    posts.reverse()
    post_titles = []
    for s in posts:
        with open(POSTDIR+s) as f:
            post_titles.append(f.readline().replace("## ", "").strip())
    text=""
    title="Autumn Chiu"
    
    if request.path == "/":
        post=posts[0]
    if post != None:
        posts=posts[:5]
        with open(POSTDIR+post, "r") as f:
            text=f.read()
            title=text.partition("\n")[0].replace("## ", "") + " | " + title
    return render_template("blog.html",
                           title=title,
                           text=text,
                           posts=posts,
                           post_titles=post_titles)

@app.route("/health")
def health():
    return "im healthy!"

# mlh routes

@app.route('/mlh/')
@app.route('/mlh/Experience/')
def index():
    return render_template('data.html',
                           data=data,
                           main="Experience",
                           side1="Projects",
                           side2="Accomplishments",
                           url=os.getenv("URL"))

@app.route('/mlh/Projects/')
def projects():
    return render_template('data.html',
                           data=data,
                           main="Projects",
                           side1="Experience",
                           side2="Accomplishments",
                           url=os.getenv("URL"))

@app.route('/mlh/Accomplishments/')
def accomplishments():
    return render_template('data.html',
                           data=data,
                           main="Accomplishments",
                           side1="Experience",
                           side2="Projects",
                           url=os.getenv("URL"))

# database shenanigans

@app.route("/mlh/register", methods=("GET", "POST"))
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

@app.route("/mlh/login", methods=("GET", "POST"))
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
