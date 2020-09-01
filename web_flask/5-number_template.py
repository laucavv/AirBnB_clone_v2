#!/usr/bin/python3
"""Script that starts a Flask web application """

from flask import Flask, render_template
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


@app.route('/python')
@app.route('/python/text')
def Python_is_fun(text='is cool'):
    """display python is <text>"""
    new_t = text.replace("_", " ")
    return 'Python {}'.format(new_t)


@app.route('/number/<int:n>')
def Is_integer(n):
    """ Is integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def template_num(n):
    """ Is integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
