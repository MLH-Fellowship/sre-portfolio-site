import os
import json
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

f = open("./lavina.json")
data = json.load(f)
f.close()

@app.route('/')
def index():
    return render_template('data.html',
                           data=data,
                           main="Projects",
                           side1="Experience",
                           side2="Accomplishments",
                           url=os.getenv("URL"))

# @app.route('/experience/')
# def experience():
#     return render_template('data.html', title="Experience",
#                            content=data["experience"], url=os.getenv("URL"))

# @app.route('/projects/')
# def projects():
#     return render_template('index.html', title="Projects",
#                            content="projects?", url=os.getenv("URL"))

# @app.route('/accomplishments/')
# def accomplishments():
#     return render_template('index.html', title="Accomplishments",
#                            content="accomplishments?", url=os.getenv("URL"))
