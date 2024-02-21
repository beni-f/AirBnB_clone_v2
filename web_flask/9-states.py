#!/usr/bin/python3
"""
    Starts a flask web app
"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)
app.strict_slashes = False

@app.teardown_appcontext
def close(exception):
    """
    Remove the current session after each request
    """
    storage.close()

@app.route('/states')
def states():
    """
        Displays a HTML page
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)

@app.route('/states/<id>')
def get_state(id):
    """
        Displays a HTML page
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
             return render_template("9-states.html", state=state)  

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")