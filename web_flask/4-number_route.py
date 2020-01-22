#!/usr/bin/python3
# Starts a Flask web app. Listen on 0.0.0.0:5000. Route: /hbnb display "HBNB"
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Serve Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Serve HBNB."""
    return 'HBNB!'

@app.route('/c/<string:text>', strict_slashes=False)
def cisfun(text):
    """Serve C + text; replace _ with space."""
    return 'C %s' % text.replace("_", " ")

@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/<string:text>', strict_slashes=False)
def pythoniscool(text):
    """Serve Python + text with default value; replace _ with space."""
    return 'Python %s' % text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Serve 'n is a number iff n is an integer."""
    return '%d is a number' % n

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
