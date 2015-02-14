import pymongo

client = pymongo.MongoClient()
gdb = client['kbgraph']
doc = gdb['nodes']
results = doc.find().distinct("data")
count = 0
for row in results:
	temp = doc.find({'data':row}).count()
	count = count+temp
print count	
