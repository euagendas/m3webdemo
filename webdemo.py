#Run using:
# export PATH=/home/shale/anaconda3/bin:$PATH
# FLASK_APP=webdemo.py python -m flask run
#

from flask import Flask, url_for, render_template, Response, request

from m3inference import M3Twitter
import json
import glob

app = Flask(__name__)

m3twitter=M3Twitter(cache_dir="static/m3/")
screen_name_list=[x.replace(".json","").replace("static/m3/","") for x in glob.glob("static/m3/*.json")]

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/infer/<screen_name>')
def infer_screen_name(screen_name):
	global m3twitter
	try:
		output=m3twitter.infer_screen_name(screen_name)
		add_screen_name(screen_name)
		return Response(json.dumps(output), mimetype='text/json')
	except urllib.error.HTTPError:
		return Response(json.dumps({"input":{"screen_name":screen_name}}), mimetype='text/json')


def add_screen_name(screen_name):
	global screen_name_list
	if not screen_name in screen_name_list:
		screen_name_list.append(screen_name)

@app.route('/autocomplete/screen_name')
def list_screen_names():
	global screen_name_list
	query=request.args.get('query')
	if query!=None:
		query=query.lower()
		matches=[x for x in filter(lambda sn : query in sn,screen_name_list)]
	else:
		matches=screen_name_list
	print(matches)
	return json.dumps({
		"query": "Unit",
		"suggestions": matches
	})