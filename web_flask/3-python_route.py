#!/usr/bin/python3
"""
    A script that starts a flask web app
"""
from flask import Flask, render_template

app = Flask(__name__)
app.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """
        returns the desired string at the home page
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """
        returns the desired string at the hbnb page
    """
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    text = text.replace('_',' ')
    return 'C {}'.format(text)

@app.route('/python/<text>')
@app.route('/python')
def python(text='is  cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
