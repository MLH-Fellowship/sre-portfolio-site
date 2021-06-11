import os
from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime
import json

load_dotenv()
app = Flask(__name__)

#Initialize Firestore DB
firebase_creds = json.loads(os.getenv("FIREBASE_CREDS"))
cred = credentials.Certificate(firebase_creds)
default_app = initialize_app(cred)
db = firestore.client()
posts_ref = db.collection('posts')

@app.route('/')
def index():
    return render_template('index.html', url=os.getenv("URL"))

@app.route('/add-blog-post', methods=['GET', 'POST'])
def addBlogPost():
    try: 
        if request.method == 'POST':
            postdata = dict(request.form)
            new_post = {
                "title": postdata["title"],
                "content": postdata["content"],
                "date": datetime.now()
            }
            posts_ref.add(new_post)

            return redirect(os.getenv("URL") + 'blog')
        else:
            return render_template('add-blog-post.html', url=os.getenv("URL"))
    except (Exception) as e:
        return f"An error Ocurred: {e}"

@app.route('/blog', methods=['GET'])
def blog():
    try: 
        all_posts = [doc.to_dict() for doc in posts_ref.stream()]
        return render_template('blog.html', posts=all_posts, url=os.getenv("URL"))
    except (Exception) as e:
        return f"An error Ocurred: {e}"