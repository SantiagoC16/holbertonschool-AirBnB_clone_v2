#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_by_states():
    from models import storage
    from models.state import State
    states = storage.all(State)

    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """closes the sql session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
