#!/usr/bin/python3
"""Script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def db_close(db):
    """Close sessions """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_cities(id=None):
    """ List State """
    states = None
    states_all = storage.all(State)
    state_id = "State.{}".format(id)
    if state_id in states_all.keys():
        states = states_all[state_id]
    return render_template('9-states.html', states=states,
                           id=id, states_all=states_all)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
