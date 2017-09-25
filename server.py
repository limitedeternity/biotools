# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, send_from_directory, request, jsonify
from flask_sslify import SSLify
from random import choice
from os import chdir
from os.path import dirname, abspath
from subprocess import check_output
from flask_wtf.csrf import CSRFProtect
from os import environ

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = environ.get("SECRET_KEY", "".join(choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(50)))
csrf = CSRFProtect(app)
sslify = SSLify(app)


'''
Template handling
'''


@app.route("/", methods=['GET'])
def index():
	response = make_response(render_template('index.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


@app.route("/it", methods=['GET'])
def it():
	response = make_response(render_template('it.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' fonts.googleapis.com 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


@app.route("/biology", methods=['GET'])
def biology():
	response = make_response(render_template('biology.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' fonts.googleapis.com 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


@app.route("/chemistry", methods=['GET'])
def chemistry():
	response = make_response(render_template('chemistry.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' fonts.googleapis.com 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


@app.route("/webapp", methods=['GET', 'POST'])
def webapp():
	if request.method == 'GET':
		response = make_response(render_template('webapp.html'))
		response.headers['X-Content-Type-Options'] = 'nosniff'
		response.headers['X-Frame-Options'] = 'DENY'
		response.headers['X-XSS-Protection'] = '1; mode=block'
		response.headers['Strict-Transport-Security'] = 'max-age=31536000'
		response.headers['Cache-Control'] = 'no-cache'
		response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' fonts.googleapis.com 'unsafe-inline'; object-src 'none'; font-src 'self'"
		return response

	elif request.method == 'POST':
		string = request.form.get('seq_in', None).strip().upper()

		if string is not None:
			command = None

			# DNA
			if request.form['action'] == 'DNA to protein':
				command = 'dna-to-protein.py'
			elif request.form['action'] == 'DNA to m-RNA':
				command = 'dna-to-messenger-rna.py'
			elif request.form['action'] == 'DNA to t-RNA':
				command = 'dna-to-transport-rna.py'
			elif request.form['action'] == 'DNA complement':
				command = 'dna-complement.py'
			elif request.form['action'] == 'Reverse sequence':
				command = 'just-reverse.py'

			# Molar mass calculation
			elif request.form['action'] == 'Protein molar mass':
				command = 'molar-mass-protein.py'
			elif request.form['action'] == 'DNA molar mass':
				command = 'molar-mass-dna.py'
			elif request.form['action'] == 'RNA molar mass':
				command = 'molar-mass-rna.py'

			# RNA
			elif request.form['action'] == 't-RNA to m-RNA':
				command = 'transport-rna-to-messenger-rna.py'
			elif request.form['action'] == 't-RNA to protein':
				command = 'transport-rna-to-protein.py'
			elif request.form['action'] == 't-RNA to DNA':
				command = 'transport-rna-to-dna.py'
			elif request.form['action'] == 'm-RNA to t-RNA':
				command = 'messenger-rna-to-transport-rna.py'
			elif request.form['action'] == 'm-RNA to protein':
				command = 'messenger-rna-to-protein.py'
			elif request.form['action'] == 'm-RNA to DNA':
				command = 'messenger-rna-to-dna.py'

			# Amount calculation
			elif request.form['action'] == 'DNA nucleotides count':
				command = 'nucleotides_count_dna.py'
			elif request.form['action'] == 'RNA nucleotides count':
				command = 'nucleotides_count_rna.py'
			elif request.form['action'] == 'DNA trinucleotides count':
				command = 'trinucleotides_count_dna.py'
			elif request.form['action'] == 'RNA trinucleotides count':
				command = 'trinucleotides_count_rna.py'
			elif request.form['action'] == 'Aminoacids count':
				command = 'aminoacids_count_protein.py'

			if command is not None:
				output = check_output(['python', 'static/scripts/' + command, string]).strip().decode("utf-8")
				return jsonify(str(output))

			else:
				return "<ul><li>Unable to identify command.</li></ul>"

		else:
			return "<ul><li>Invalid input.</li></ul>"


@app.route("/example", methods=['GET'])
def example():
	response = make_response(render_template('example.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


@app.route("/protein_reading", methods=['GET'])
def protein_iupac():
	response = make_response(render_template('protein_iupac.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


@app.route("/offline", methods=['GET'])
def offline():
	response = make_response(render_template('offline.html'))
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'DENY'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=31536000'
	response.headers['Cache-Control'] = 'no-cache'
	response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; font-src 'self'; object-src 'none'"
	return response


'''
Frontend handling
'''


@app.route('/config/<path:path>', methods=['GET'])
def serve_config(path):
	return send_from_directory('static/config', path)


@app.route('/sw.js', methods=['GET'])
def serviceworker():
	return send_from_directory('static/js', 'sw.js')


@app.route('/js/<path:path>', methods=['GET'])
def serve_js(path):
	if path != 'sw.js':
		return send_from_directory('static/js', path)


@app.route('/css/<path:path>', methods=['GET'])
def serve_css(path):
	return send_from_directory('static/css', path)


@app.route('/images/<path:path>', methods=['GET'])
def serve_image(path):
	return send_from_directory('static/images', path)


@app.route('/fonts/<path:path>', methods=['GET'])
def serve_fonts(path):
	return send_from_directory('static/fonts', path)


if __name__ == "__main__":
	chdir(dirname(abspath(__file__)))
	app.run(debug=False, use_reloader=True)
