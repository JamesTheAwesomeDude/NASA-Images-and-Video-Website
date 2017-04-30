#!/usr/bin/env python3
# MIT License 2017, James Edington <codegeek98@gmail.com>

import cgi,cgitb
cgitb.enable()

import urllib.request
import urllib.parse
import json

API_ROOT='https://images-api.nasa.gov'
API_ENDPOINTS={
 'srch': "/search",
 'asst': "/asset/{}",
 'meta': "/metadata/{}",
 'capt': "/captions/{}"
}

def allimages_NASA():
	items_cumulative=[]
	page=0
	while True:
		page+=1
		try:
			json=_search({
			 'media_type': 'image',
			 'page': page
			})['collection']
		except urllib.error.HTTPError:
			break
		items_cumulative+=json['items']
		if not [link for link in json['links'] if link['rel']=='next']:
		 break
	return items_cumulative

def _search(data):
	with urllib.request.urlopen(
	 ''.join([
	  API_ROOT,
	  API_ENDPOINTS['srch'],
	  '?',
	  urllib.parse.urlencode(data)
	 ])
	) as response:
		return json.loads(
		 response.read().decode()
		)

def _asset(nasa_id):
	with urllib.request.urlopen(
	 ''.join([
	  API_ROOT,
	  API_ENDPOINTS['asst'].format(nasa_id)
	 ])
	)as response:
		return json.loads(
		 response.read().decode()
		)

if __name__=="__main__":
	x=_search({'q': "orange"})['collection']['items']
	print("""Content-type:text/html\r\n\r\n
<!DOCTYPE HTML>
<html>
<head>
<title>TEST PAGE LMAO</title>
<body>""")
	for link in x:
		print('<img src="{src}" title="{title}" />'.format(
		 src=[l for l in link['links'] if l['rel']=='preview'][0]['href'],
		 title=link['data'][0]['title']
		))
	print("""</body>
</html>""")
