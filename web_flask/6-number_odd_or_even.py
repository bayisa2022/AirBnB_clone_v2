#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb')  
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c_text(text):
    text = text.replace('_', ' ')
    return 'C ' + text

@app.route('/python/<text>')
def python_text(text='is cool'):
    text = text.replace('_', ' ') 
    return 'Python ' + text

@app.route('/number/<int:n>')
def number_n(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    parity = 'odd' if n % 2 else 'even'
    return render_template('odd_or_even.html', n=n, parity=parity)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

