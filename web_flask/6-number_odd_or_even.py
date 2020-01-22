#!/usr/bin/python3
# Starts a Flask web app. Listen on 0.0.0.0:5000. Route: /hbnb display "HBNB"
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_number(n):
    """Serve 'HTML template, <h1>Number n</h1> iff n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_number(n):
    """Serve 'HTML template, Number n is odd/even, iff n is an integer."""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
