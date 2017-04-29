#!/usr/bin/env python3
# MIT License 2017, James Edington <codegeek98@gmail.com>

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
