#!/usr/bin/python3 # shebang line

from flask import Flask  # import Flask class
app = Flask(__name__) # create Flask app instance 
app.url_map.strict_slashes = False # disable strict slashes 

import re # import regex module

@app.route('/') # root route
def hello(): # hello function 
    return 'Hello HBNB!' # return string

@app.route('/hbnb') # hbnb route
def hbnb(): # hbnb function
    return 'HBNB' # return string

@app.route('/c/<text>') # c route with variable 
def c(text): # c function 
    text = text.replace('_', ' ') # replace underscores
    return 'C ' + text # return string

@app.route('/python') # python route 
@app.route('/python/<text>') # python route with variable
def python(text='is cool'): # python function
    text = text.replace('_', ' ') # replace underscores
    return 'Python ' + text # return string 

@app.route('/number/<n>') # number route with variable
def number(n): # number function
    if re.match(r'^-?\d+$', n): # check if n is integer
        return '{} is a number'.format(n) # return string
    else:
        return 'Illegal input!' # return string
        
if __name__ == '__main__': # entry point
    app.run(host='0.0.0.0', port=5000) # run app
