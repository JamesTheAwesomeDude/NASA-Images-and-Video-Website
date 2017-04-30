#!/usr/bin/env python3

from NASA_API import allitems_NASA,_details_url

def sitemap():
	for item in allitems_NASA():
		print(_details_url(item['data'][0]['nasa_id']))

if __name__=="__main__":
	sitemap()
