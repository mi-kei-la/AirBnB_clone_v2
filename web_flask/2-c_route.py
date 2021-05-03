#!/usr/bin/python3
""" This is a single module script that starts Flask.
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """This function displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_input(text):
    """This function displays C and the user input"""
    string = escape(text)
    return "C {}".format(string.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
