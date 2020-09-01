#!/usr/bin/python3
"""Script that starts a Flask web application """

from flask import Flask
app = Flask(__name__)
strict_slashes = False


@app.route('/')
def Hello():
    """ display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def Hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def C_is_fun(text):
    """display c is <text>"""
    new_t = text.replace("_", " ")
    return 'C {}'.format(new_t)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
