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

@app.route('/states_list')
def list_of_states():
    """
    Displays all states present in DBStorage
    """
    return render_template('7-states_list.html', states=storage.all(State).values())

@app.route('/cities_by_states')
def cities_by_states():
    """
        Display all cities present
    """
    return render_template('8-cities_by_states.html', states=storage.all(State).values())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5500")
