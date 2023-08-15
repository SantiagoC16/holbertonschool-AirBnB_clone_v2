#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    from models import storage
    from models.state import State
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """closes the sql session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
