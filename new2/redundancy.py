import pymongo

client = pymongo.MongoClient()
gdb = client['kbgraph']
doc = gdb['nodes']
newdoc = gdb['node']

def redundancy():
	doc = gdb['nodes']
	results = doc.find()
	for row in results:
		count = doc.find({'data':row['data']}).count()	
		if int(count)>1:
			keys = []
			docs = doc.find({'data':row['data']})
			for rec in docs:
				keys.extend(rec['property'])
			for i in range(0,len(keys)):
				temp = keys[i]
				temp = temp.lower()
				keys[i] = temp
			keys = list(set(keys))
			newdoc.insert({'data':row['data'],'property':keys})
			print {'data':row['data'],'property':keys}
			doc.remove({'data':row['data']})
		else:
			newdoc.insert({'data':row['data'],'property':row['property']})
			doc.remove({'data':row['data'],'property':row['property']})
redundancy()
