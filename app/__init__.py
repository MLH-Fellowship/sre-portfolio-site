import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', url=os.getenv("URL"))

@app.route('/add-blog-post', methods=['GET', 'POST'])
def addBlogPost():
    if request.method == 'POST':
        # Create function create post that
            # Sends data to firebase
            # Redirects to all existing posts 
        return create_post()
    else:
        return render_template('add-blog-post.html', url=os.getenv("URL"))

@app.route('/blog')
def blog():
    #Pass blog posts parameter so it actually renders all of them
    return render_template('blog.html', url=os.getenv("URL"))