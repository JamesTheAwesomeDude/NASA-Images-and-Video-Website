#!/usr/bin/env python3
# MIT License 2017, James Edington <codegeek98@gmail.com>

import urllib.request
import urllib.parse
import json
import cgi,cgitb
cgitb.enable()

API_ROOT='https://images-api.nasa.gov'
API_ENDPOINTS={
 'srch': "/search",
 'asst': "/asset/{}",
 'meta': "/metadata/{}",
 'capt': "/captions/{}"
}

def search_NASA(search_term):
	return _url_json(''.join([
	 API_ROOT,
	 API_ENDPOINTS['srch'],
	 '?',
	 urllib.parse.urlencode({
	  'q': search_term
	 })
	]))

def _url_json(url):
	with urllib.request.urlopen(url) as response:
		return json.loads(
		 response.read().decode()
		)
if __name__=="__main__":
	x=search_NASA('orange')['collection']['items'][8]
	print("""Content-type:text/html\r\n\r\n
<!DOCTYPE HTML>
<html>
<head>
<title>TEST PAGE LMAO</title>
<body>
<img src="{src}" title="{title}" />
</body>
</html>""".format(
	 src=[link for link in x['links'] if link['rel']=='preview' and link['render']=='image'][0]['href'],
	 title=x['data'][0]['title']
	))
