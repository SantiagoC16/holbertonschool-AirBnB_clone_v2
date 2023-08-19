#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """documentation states..."""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_states_id(id):
    """documentation states id"""
    states = storage.all(State)
    _dict = {}
    _id = 0
    for key, value in states.items():
        _id = key.split('.')
        if _id[1] == id:
            _dict = {key, value}
    return render_template('9-states-html', states=_dict, id=id)


@app.teardown_appcontext
def teardown(exception):
    """closes the sql session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
