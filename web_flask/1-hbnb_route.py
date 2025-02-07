#!/usr/bin/python3
""" This is a single module script that starts Flask.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """This function displays 'HBNB'"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
