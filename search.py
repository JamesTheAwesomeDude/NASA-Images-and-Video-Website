#!/usr/bin/env python3
# MIT License 2017, James Edington <codegeek98@gmail.com>

#import cgi,cgitb
#cgitb.enable()

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
MEDIA_TYPES=['image', 'video', 'audio']

def sitemap():
	for item in allitems_NASA():
		print(_details_url(item['data'][0]['nasa_id']))

def allitems_NASA():
	items_cumulative=[]
	for media_type in MEDIA_TYPES:
		page=0
		while True:
			page+=1
			try:
				json=_search({
				 'media_type': media_type,
				 'page': page
				})['collection']
			except urllib.error.HTTPError:
				break
			items_cumulative+=json['items']
			if 'links' not in json or not [link for link in json['links'] if link['rel']=='next']:
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

def _details_url(nasa_id):
	return 'https://images.nasa.gov/#/details-{}.html'.format(nasa_id)

if __name__=="__main__":
#	sitemap()
	pass
