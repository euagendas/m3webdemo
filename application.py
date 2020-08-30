# This file is part of m3webdemo.

# m3webdemo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# m3webdemo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with m3webdemo.  If not, see <https://www.gnu.org/licenses/>.


from flask import Flask, url_for, render_template, Response, request

from m3inference import M3Twitter
import json
import glob
import urllib
import os

app = Flask(__name__)

m3twitter=M3Twitter(cache_dir="static/m3/",model_dir="./")
m3twitter.twitter_init(
    api_key=os.environ["api_key"],
    api_secret=os.environ["api_secret"],
    access_token=os.environ["access_token"],
    access_secret=os.environ["access_secret"]
)
screen_name_list=[x.replace(".json","").replace("static/m3/","") for x in glob.glob("static/m3/*.json")]

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/infer/<screen_name>')
def infer_screen_name(screen_name):
	if len(screen_name)>15:
		#Invalid screen_name don't even bother
		return Response(json.dumps({"input":{"screen_name":screen_name}}), mimetype='text/json')
	else:
		global m3twitter
		try:
			output=m3twitter.infer_screen_name(screen_name)
			if output==None:
				#this is a bad hack and should be pushed into m3inference
				#output==none when there is an error with the Twitter API
				try:
					os.remove("static/m3/{}.json".format(screen_name))
				except:
					pass
				with open("static/m3/empty.txt","r") as fh:
					return Response(fh.read(), mimetype='text/json')
			if "tw_default_profile.png" in output["input"]["img_path"]:
				output["input"]["img_path"]="static/placeholder.png"
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
