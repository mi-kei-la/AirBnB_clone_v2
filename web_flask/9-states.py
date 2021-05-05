#!/usr/bin/python3
""" This is a single module script that starts Flask."""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def all_states():
    """Display all states."""
    new_dict = storage.all(State)
    return render_template('9-states.html', states=new_dict)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id=None):
    """display a HTML page"""
    all_states = storage.all(State)
    key = 'State.' + id
    if key in all_states.keys():
        state = all_states[key]
        return render_template('9-states.html', states=state)
    else:
        return render_template('9-states.html', states=True)


@app.teardown_appcontext
def close_sqlalchemy_session(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
