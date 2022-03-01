# Production Engineering - Week 1 - Portfolio Site

Welcome to the MLH Fellowship! During Week 1, you'll be working with Flask to build a portfolio site. This site will be the foundation for activities we do in future weeks so spend time this week making it your own and reflect your personality!

## Tasks

Once you've got your portfolio downloaded and running using the instructions below, you should attempt to complete the following tasks.

### Portfolio Tasks
- Add a photo of yourself to the website
- Add an "About youself" section to the website.
- Add your previous work experiences
- Add your hobbies (including images)
- Add your current/previous education
- Add a map of all the cool locations/countries you visited

### Flask Tasks
- Get your Flask app running locally on your machine using the instructions below.
- Add a template for adding multiple work experiences using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- Add a menu bar
- Put all your hobbies on a new page.
- Have new pages get automatically added to the menu bar

## Getting Started

You don't need to submit any pull requests to thie repository. You need to do all your work here.

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
