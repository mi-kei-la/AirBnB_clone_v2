#!/usr/bin/python3
""" This is a single module script that starts Flask.
"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_by_states():
    """display a HTML page"""
    new_dict = storage.all(State)
    return render_template('8-cities_by_states.html', states=new_dict)


@app.teardown_appcontext
def close_sqlalchemy_session(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
