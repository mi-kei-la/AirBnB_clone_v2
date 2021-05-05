""" This is a single module script that starts Flask."""
from flask import Flask, render_template
from models import storage, State, Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def static_filters():
    """Display all states and cities.
    Display all amenities.
    """
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=all_states,
                           amens=all_amenities)


@app.teardown_appcontext
def close_sqlalchemy_session(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
