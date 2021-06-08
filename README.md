# Flask-Blog

Minimal Flask template to get started on your blog application for MLH Fellowship Production Engineering track.
 

## Installation

Make sure you have python3 and pip installed.  On Ubuntu/Debian, it looks something like this:


```bash
apt install python3
apt install pip
# replace "apt" with the package manager of your choice.
```

You may also need to install venv:
```bash
apt install python3-venv
```

Create and activate virtual environment using virtualenv.
```bash
~/your/path/here$ python -m venv python3-virtualenv

# creates a directory python3-virtual env in the current directory,
# which contains all the files for a new virtual environment.

~/your/path/here$ source python3-virtualenv/bin/activate

# tells the command line to enter the above virtual environment.
```

Afterwards, your command prompt might look something like this:
```bash
(python3-virtualenv) name@computer:~/your/path/here$
```

And you can make extra sure it's working properly in the Python interpreter:
```
>>> import sys
>>> sys.path
[..., '~/your/path/here/python3-virtualenv/lib/python3.8/site-packages']
```

While using the virtual environment, use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.
```bash
pip install -r requirements.txt
```

This should install click, Flask, itsdangerous, Jinja2, MarkupSafe, python_dotenv,  and Werkzeug.

## Usage

Create a .env file using the example.env template.

Start flask development server:
```bash
$ export FLASK_ENV=development
$ flask run
```

You should see a message that specifies the IP at which the app is hosted: 127.0.0.1:5000.  Open that address in your browser to confirm that the app is working.


## A Beginner's Guide to Flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/) is a micro web framework written in Python.  The idea behind Flask is to convert HTTP requests into function calls Python can understand; this is accomplished through the use of `routes`, as in [our init file](app/__init__.py):

```python
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))
```

The above code translates as follows: when we receive a request with the URL '/', give the user the HTML resulting from the `render_template()` call.

`render_template()` is a function that takes a template (`'index.html'`), some arguments to the template (`title="MLH Fellow", url=os.getenv("URL")`), and returns a complete HTML file.  The "template" in question is a [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) template, which basically lets you insert `{{ variables }}` into an a reusable HTML template.  (Other features and file formats are supported as well.)  You can check out [this repo's index page](app/templates/index.html) for an example.

This project will involve writing new routes and templates to grow this simple placeholder code into a fully-fledged portfolio.  See [this demo](https://mlh-fellowship.github.io/portfolio-template/) for an example of how it might look.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
