import os
import re
import json
from flask import Flask, render_template, request

# from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from . import db
# from app.db import get_db

# load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
Markdown(app)
# app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    user=os.getenv("POSTGRES_USER"),
    passwd=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    table=os.getenv("POSTGRES_DB"),
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserModel(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


f = open("./lavina.json")
data = json.load(f)
f.close()

POSTDIR = "./posts/"


@app.route("/")
@app.route("/blog/")
@app.route("/blog/<post>")
def blog(post=None):
    p = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}.+\\.md$")
    posts = list(filter(p.match, os.listdir(POSTDIR)))
    posts.sort()
    posts.reverse()
    post_titles = []
    for s in posts:
        with open(POSTDIR + s) as f:
            post_titles.append(f.readline().replace("## ", "").strip())
    text = ""
    title = "Autumn Chiu"

    if request.path == "/":
        post = posts[0]
    if post is not None:
        posts = posts[:5]
        with open(POSTDIR + post, "r") as f:
            text = f.read()
            title = text.partition("\n")[0].replace("## ", "") + " | " + title
    return render_template(
        "blog.html",
        title=title,
        text=text,
        posts=posts,
        post_titles=post_titles,
    )


@app.route("/health/")
def health():
    return "im healthy!"


# mlh routes


@app.route("/mlh/")
@app.route("/mlh/Experience/")
def index():
    return render_template(
        "data.html",
        data=data,
        main="Experience",
        side1="Projects",
        side2="Accomplishments",
        url=os.getenv("URL"),
    )


@app.route("/mlh/Projects/")
def projects():
    return render_template(
        "data.html",
        data=data,
        main="Projects",
        side1="Experience",
        side2="Accomplishments",
        url=os.getenv("URL"),
    )


@app.route("/mlh/Accomplishments/")
def accomplishments():
    return render_template(
        "data.html",
        data=data,
        main="Accomplishments",
        side1="Experience",
        side2="Projects",
        url=os.getenv("URL"),
    )


# database shenanigans


@app.route("/mlh/register/", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else:
            return error, 418
    # TODO: return a register page
    return render_template("login.html", data=data, mode="register")


@app.route("/mlh/login/", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        user = UserModel.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        if error is None:
            return "Login successful", 200
        else:
            return error, 418
        # TODO: Return a login page
    return render_template("login.html", data=data, mode="login")
