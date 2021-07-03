import os
from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')

@app.route('/')
def index():
    return render_template('index.html', title="Leeia Isabelle | Software Developer", url=os.getenv("URL"), name="LEEIA")

@app.route('/health', methods=['GET'])
def health():
    return "200"
