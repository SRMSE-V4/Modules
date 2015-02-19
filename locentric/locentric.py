#!/usr/bin/python

import cgi, cgitb

cgitb.enable()

from pymongo import MongoClient
print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage()

latitude = form['lat'].value
longitude = form['long'].value

def locentric(logitude, latitude, database):
	client = MongoClient('127.0.0.1', 27017)
	db = client.locentric
	collection = db[database]
	for x in collection.find({'loc':{'$near':{'$geometry':{'type':"Point",'coordinates':[float(longitude),float(latitude)]}}}}).limit(4):
		print x

locentric(longitude, latitude, "earthquake")