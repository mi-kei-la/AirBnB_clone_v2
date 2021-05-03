#!/usr/bin/python3
""" This is a single module script that starts Flask.
"""
from flask import Flask, escape, render_template
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
def print_c_input(text):
    """This function displays 'C' and the user input"""
    string = escape(text)
    return "C {}".format(string.replace('_', ' '))


@app.route('/python/', strict_slashes=False,
           defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def print_python_input(text):
    """This function displays 'Python ' and user or default input"""
    string = escape(text)
    return "Python {}".format(string.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """This function prints a given number only if int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_template(n):
    """This function returns an HTML template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
