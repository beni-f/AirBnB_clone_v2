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
    """
        display “C ”, followed by the value of the text variable
    """
    text = text.replace('_',' ')
    return 'C {}'.format(text)

@app.route('/python/<text>')
@app.route('/python')
def python(text='is  cool'):
    """
        display “Python ”, followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def number(n):
    """
        display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """
       display a HTML page only if n is an integer 
    """
    return render_template('5-number.html', n=n)
    
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)