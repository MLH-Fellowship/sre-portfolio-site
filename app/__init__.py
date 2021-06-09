import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow",
                           content="it me", url=os.getenv("URL"))

@app.route('/experience/')
def experience():
    return render_template('data.html', title="Experience",
                           content=dummy_info["experience"], url=os.getenv("URL"))

@app.route('/projects/')
def projects():
    return render_template('index.html', title="Projects",
                           content="projects?", url=os.getenv("URL"))

@app.route('/accomplishments/')
def accomplishments():
    return render_template('index.html', title="Accomplishments",
                           content="accomplishments?", url=os.getenv("URL"))

dummy_info = {
    "name": "Lavina Stella Harper",
    "title": "Web Developer",
    "education": {
        "degree": "B.S. Computer Science",
        "school": "University of the People",
        "date": "2016-2020"
        },
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",

    "skills": ["HTML", "CSS", "JavaScript", "React.js", "Bootstrap"],
    
    "experience": [
        {
            "name": "Front-End Web Development",
            "date": "2020-Present",
            "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",
        },
        {
            "name": "Back-End Web Development",
            "date": "2019-2020",
            "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",
        }
    ],
    "projects":  [
        {
            "name": "Web Design",
            "date": "2020-Present",
            "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",
        },
        {
            "name": "Bright Ideas",
            "date": "2019-2020",
            "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",
        }
    ],
    "Accomplishments":  [
        {
            "name": "Whatever it is",
            "date": "2018",
            "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",
        },
        {
            "name": "Accomplishment 2",
            "date": "2019",
            "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada, velit eget dictum gravida, quam neque ultricies massa, eget dignissim tortor libero vel tortor. Fusce vitae dui molestie, vulputate augue sit amet, faucibus mauris. Quisque at erat orci. Vestibulum porta mauris id metus scelerisque dapibus. Suspendisse in varius sem, in dictum diam. Ut auctor aliquam blandit. Fusce sed ullamcorper tortor, vitae ultricies augue. Duis rutrum, massa ut egestas pharetra, nulla sem volutpat nibh, id vulputate augue lacus ac ante.",
        }
    ]
}
