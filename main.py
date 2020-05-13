# main.py

import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/hello/<name>/')
def hello_name(name):
    return 'Hello, {}!'.format(name)

@app.route('/hola/<name>/')
def hola_name(name):
    return 'Hola, {}!'.format(name)

@app.route('/goodbye/<times>/<name>/')
def goodbye_world(times, name):
    return ('Goodbye, {}!'.format(name))*int(times)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
