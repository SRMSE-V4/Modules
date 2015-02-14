import pymongo
import time
t = time.time()

client = pymongo.MongoClient()
gdb = client['kbgraph']
doc = gdb['nodes']
newdoc = gdb['node']
pipeline = []
pipeline.append({"$group":{"_id":"$data"}})
results = doc.aggregate(pipeline)
red = results['result']
for i in range(0,len(red)):
	pipeline[:] = []
	findic = {}
	pipeline.append({"$match":{"data":red[i]['_id']}})
	pipeline.append({"$unwind":"$property"})
	pipeline.append({"$group":{"_id":"$data","final":{"$addToSet":"$property"}}})
	results = doc.aggregate(pipeline)
	arr = results['result']
	dict = arr[0]
	findic['property'] = dict['final']
	findic['data'] = red[i]['_id']
	newdoc.insert(findic)
print time.time()-t

