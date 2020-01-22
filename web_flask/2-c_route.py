#!/usr/bin/python3
# Starts a Flask web app. Listen on 0.0.0.0:5000. Route: /hbnb display "HBNB"
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB!'

@app.route('/c/<string:text>', strict_slashes=False)
def cisfun(text):
    return 'C %s' % text.replace("_", " ")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
