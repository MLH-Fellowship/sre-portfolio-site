import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow",
                           bodytext="it me", url=os.getenv("URL"))

@app.route('/experience/')
@app.route('/experience/<page>')
def experience(page=None):
    return render_template('index.html', title="Experience",
                           bodytext="experience?", url=os.getenv("URL"))

@app.route('/projects/')
@app.route('/projects/<page>')
def projects(page=None):
    return render_template('index.html', title="Projects",
                           bodytext="projects?", url=os.getenv("URL"))

@app.route('/accomplishments/')
@app.route('/accomplishments/<page>')
def accomplishments(page=None):
    return render_template('index.html', title="Accomplishments",
                           bodytext="accomplishments?", url=os.getenv("URL"))

@app.route('/skills/')
@app.route('/skills/<page>')
def skills(page=None):
    return render_template('index.html', title="Skills",
                           bodytext="skills?", url=os.getenv("URL"))

        
