#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states_id():
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_states_id(id):
    for states_id in storage.all(State).values():
        if states_id.id == id:
            return render_template("9-states.html", states_id=states_id)
        else:
            return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """closes the sql session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
