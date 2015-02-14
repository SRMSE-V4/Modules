import pymongo
client = pymongo.MongoClient()
pipeline = []
gdb = client['kbgraph']
doc = gdb['node']
pipeline.append()
pipeline.append({"$group":{"_id":"$data","total":{"$sum":1}}})
pipeline.append({"$match":{"total":{"$gte":1}}})
results = doc.aggregate(pipeline)
arr = results['result']
print len(arr)
