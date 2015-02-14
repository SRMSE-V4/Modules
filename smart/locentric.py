import cgitb
cgitb.enable()

from pymongo import MongoClient

def locentric(longitude, latitude, database):

#	print longitude,latitude
	client = MongoClient()
	db = client.locationcentric
	collection = db[str(database).strip()]
	#print [database]
	#print [collection.find()]
	#print collection
	#print database
	#print float(longitude)
	results = collection.find({'loc':{'$near':{'$geometry':{'type':"Point",'coordinates':[float(longitude.replace(";","")),float(latitude.replace(";",""))]}}}}).limit(4)
	#print list(results)
	#ans = results

	#print list(results)
	return list(results)


def main(query):
	rm=['near','nearest','nearer','around','close']
	for r in rm :
		query= query.replace(r,"")
#	print query
	import Cookie,os
	cookie = Cookie.SimpleCookie()
	stringCookie = os.environ.get('HTTP_COOKIE')

	cor =cookie.load(stringCookie)
#	print stringCookie
	latlong = stringCookie.split(";")
#	print latlong
	latitude = latlong[0].split("=",1)[1].strip()
	longitude = latlong[1].split("=",1)[1].strip()
#	print latitude,longitude
	ans = locentric(longitude, latitude, query)
#	print latitude,ans
	return ans
