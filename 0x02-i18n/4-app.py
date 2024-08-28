#!/usr/bin/env python3
"""a basic Flask app
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext as _


class Config:
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """to determine the best
    match with our supported languages.
    """
    local = None
    if request.args:
        local = request.args.get('local')
    if local and local in Config.LANGUAGES:
        return local
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def hello() -> str:
    """Create a single / route and an
    index.html template that simply
    outputs “Welcome to Holberton”
    as page title (<title>) and
    “Hello world” as header (<h1>).
    """
    return render_template(
        '2-index.html',
        title=_("home_title"),
        header=_("home_header"))


if __name__ == "__main__":
    """ Main Function """
    app.run()
