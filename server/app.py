#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    num = range(parameter)
    new_list = ''
    for i in num:
        new_list += f'{i}\n'
    return f'{new_list}'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    if operation == 'div':
        operator = '/'
    else:
        operator = operation
    result = eval(f'{num1}{operator}{num2}')
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
