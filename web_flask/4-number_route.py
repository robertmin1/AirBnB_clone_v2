#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C' followed by the value of the text variable
    /python/(<text>): Displays 'Python' followed by the value of the text
    /number/<n>: Displays 'n is a number' only if n is an integer
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Displays 'C' followed by the value of the text variable

    Replaces any underscores in the text with spaces.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    Displays 'Python' followed by the value of the text variable

    Replaces any underscores in the text with spaces.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays 'n is a number' only if n is an integer

    If n is not an integer, returns a 404 error.
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
