#Run using:
# FLASK_APP=webdemo.py python -m flask run
#

from flask import Flask, url_for, render_template, Response

from m3twitter import M3Twitter

app = Flask(__name__)

m3twitter=M3Twitter()

#url_for('static', filename='index.html')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/infer/<screen_name>')
def infer_screen_name(screen_name):
	global m3twitter
	output=m3twitter.infer_screen_name(screen_name)
	return Response(output, mimetype='text/json')


