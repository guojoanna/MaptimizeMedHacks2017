# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:57:28 2017

@author: dariu
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #decorator
def index():
    return render_template('hello.html')
    
if __name__ == '__main__': 
    app.run()