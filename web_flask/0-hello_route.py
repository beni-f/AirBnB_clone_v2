#!/usr/bin/python3
"""
 A script that starts a Flask web app
"""
from flask import Flask

app = Flask(__name__)
app.strict_slashes =False

@app.route('/')
def hello_hbnb():
    """
        Return desired string
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
