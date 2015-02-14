import pymongo
client = pymongo.MongoClient()
mdb = client['kb']
tabs = mdb.collection_names()
tabs.remove("system.indexes")
for i in tabs:
	i.ensure_index({"$**":"text"},{"name":"TextIndex"})
	print i,": indexed"
print "Indexed all collections"
