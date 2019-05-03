import json
import urllib.request
import re
import html

import logging

from m3inference import M3Inference
import pprint

RE_IMG_NAME=re.compile('<img class="photo" src="https://pbs.twimg.com/profile_images/(.*?)".*?>(.*?)</a>',re.DOTALL)
RE_BIO=re.compile('<p class="note">(.*?)</p>')
TAG_RE = re.compile(r'<[^>]+>')

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class M3Twitter(M3Inference):
	def __init__(self):
		super(M3Twitter, self).__init__()
	

	def infer_screen_name(self,screen_name):
		#If a json file exists, we'll use that. Otherwise go get the data.
		try:
			with open("static/m3/{}.json".format(screen_name),"r") as fh:
				logger.info("Results from cache.")
				return fh.read()
		except:
			logger.info("Results not in cache. Fetching from Twitter.")

		data=urllib.request.urlopen("https://twitter.com/intent/user?screen_name={}".format(screen_name))
		data=data.read().decode("UTF-8")
		with open("static/m3/{}.txt".format(screen_name),"w") as fh:
			fh.write(data)
		
		img_name=RE_IMG_NAME.findall(data)
		bio=RE_BIO.findall(data)

		if len(img_name)==0:
			name=""
			img_file=""
			logger.info("Name and img not found")
		else:
			img="https://pbs.twimg.com/profile_images/{}".format(img_name[0][0])
			img=img.replace("_200x200","_400x400")
			img_data=urllib.request.urlopen(img)
			img_data=img_data.read()
			img_file="static/m3/{}.{}".format(screen_name,img[-3:])
			with open(img_file,"wb") as fh:
				fh.write(img_data)
			name=img_name[0][1].strip()
		
		if len(bio)==0:
			bio=""
			logger.info("No bio")
		else:
			bio=html.unescape(TAG_RE.sub('', bio[0]))

		#BUG! M3 errs when data has only one element. Duplicate for now.
		data=[{
			"description": bio,
			"id": "1",
			#"img_path": img,
			"img_path": img_file,
			"lang": "en",
			"name": name,
			"screen_name": screen_name
		},
		{
			"description": bio,
			"id": "1",
			#"img_path": img,
			"img_path": img_file,
			"lang": "en",
			"name": name,
			"screen_name": screen_name
		}]

		pred = self.infer(data)#,batch_size=1, num_workers=1)

		output=json.dumps({
			"input":data[0], #FIX LATER
			"output":pred["1"]
		})
		with open("static/m3/{}.json".format(screen_name),"w") as fh:
			fh.write(output)
		return output

if __name__=="__main__":
	m3Twitter=M3Twitter()
	print(m3Twitter.infer_screen_name("computermacgyve"))
