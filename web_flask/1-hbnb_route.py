#!/usr/bin/python3
"""
	A script that starts a Flask web app
"""
from flask import Flask

app = Flask(__name__)
app.strict_slashes = False

@app.route('/')
def hello_hbnb():
	"""
		Returns desired string to the home page
	"""
	return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
	"""
		Returns desired string to the hbnb page
	"""
	return 'HBNB'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)