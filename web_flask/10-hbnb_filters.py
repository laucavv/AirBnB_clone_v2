#!/usr/bin/python3
"""Script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def db_close(db):
    """Close sessions """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """ List State and List Amenity """

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
