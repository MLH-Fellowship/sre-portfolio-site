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

@app.route("/health")
def health():
    return {}
