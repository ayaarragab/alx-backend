#!/usr/bin/env python3
"""a basic Flask app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Create a single / route and an
    index.html template that simply
    outputs “Welcome to Holberton”
    as page title (<title>) and
    “Hello world” as header (<h1>).
    """
    return render_template('templates/0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
