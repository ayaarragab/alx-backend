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
def get_locale():
    """_summary_

    Returns:
            _type_: _description_
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


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
