import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url="localhost:5000")

@app.route('/health')
def health():
   return "Works"
