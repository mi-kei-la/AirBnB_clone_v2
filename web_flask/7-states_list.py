#!/usr/bin/python3
""" This is a single module script that starts Flask.
"""
from flask import Flask, escape, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def print_states():
    """Print all states and their names."""
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)

@app.teardown_appcontext
def close_sqlalchemy_session(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
