# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, send_from_directory, redirect
from flask_sslify import SSLify
from random import choice
from os import chdir, environ
from os.path import dirname, abspath
from whitenoise import WhiteNoise


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = environ.get("SECRET_KEY", "".join(choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(50)))

sslify = SSLify(app)

app = WhiteNoise(app, root="static/")


'''
Template handling
'''


@app.route("/", methods=['GET'])
def index():
    response = make_response(redirect('/webapp'))
    return response


@app.route("/webapp", methods=['GET'])
def webapp():
    response = make_response(render_template('webapp.html'))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000'
    response.headers['Cache-Control'] = 'no-cache'
    return response


@app.route("/example", methods=['GET'])
def example():
    response = make_response(render_template('example.html'))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000'
    response.headers['Cache-Control'] = 'no-cache'
    return response


@app.route("/protein_reading", methods=['GET'])
def protein_iupac():
    response = make_response(render_template('protein_iupac.html'))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000'
    response.headers['Cache-Control'] = 'no-cache'
    return response


@app.route("/offline", methods=['GET'])
def offline():
    response = make_response(render_template('offline.html'))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000'
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/sw/<path:path>', methods=['GET'])
def serve_sw(path):
    if path != 'sw.js':
        return send_from_directory('sw', path)

@app.route('/sw.js', methods=['GET'])
def serviceworker():
    return send_from_directory('sw', 'sw.js')


if __name__ == "__main__":
    chdir(dirname(abspath(__file__)))
