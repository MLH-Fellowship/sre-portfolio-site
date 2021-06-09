import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

dummy_info = {
    "work": [
        {
            "summary": "lorem ipsum",
            "details": "longer lorem ipsum",
        },
        {
            "summary": "lorem ipsum 2",
            "details": "longer lorem ipsum 2",
        }
    ],
}

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow",
                           content="it me", url=os.getenv("URL"))

@app.route('/experience/')
def experience():
    return render_template('data.html', title="Experience",
                           content=dummy_info["work"], url=os.getenv("URL"))

@app.route('/projects/')
def projects():
    return render_template('index.html', title="Projects",
                           content="projects?", url=os.getenv("URL"))

@app.route('/accomplishments/')
def accomplishments():
    return render_template('index.html', title="Accomplishments",
                           content="accomplishments?", url=os.getenv("URL"))

@app.route('/skills/')
def skills():
    return render_template('index.html', title="Skills",
                           content="skills?", url=os.getenv("URL"))

        
