#Get the list if collections in a database (done)
#Get all their fields and store them in an array (done)
#Check if the collection is already present in database or not (done)
#insert/update if not present/changed (done)
#Append in the wordgraph if not present (done)

import pymongo
client = pymongo.MongoClient()
mdb = client['kb']
cols = mdb.collection_names()
remove = ['retriv','system.indexes','wordgraph']
notused = ['_id','SNo','id',' id']
doc2 = mdb['retriv']
doc3 = mdb['wordgraph']
for i in remove:
	try:
		cols.remove(i)
	except:
		continue
exists = []
try:
	results = doc2.find()
	for record in results:
		exists.append(record['collection'])
except:
	pass
graph = []
results = doc3.find()
for record in results:
	graph.append(record['word'])
flag = False
for i in cols:
	prop = []
	temp = []
	dict = {}
	doc = mdb[i]
	results = doc.find()
	for record in results:
		temp.extend(record.keys())
	temp = list(set(temp))
	for j in notused:
		try:
			temp.remove(j)
		except:
			continue
	for j in temp:
		prop.append(j.lower())
	if i in exists:
		dict2 = doc2.find({"collection":i})
		for record in dict2:
			temp2 = record['fields']
		if len(list(set(temp2)&set(prop)))!=len(prop):
			dict['collection'] = i
			dict['fields'] = prop
			doc2.insert(dict)				
			for j in notused:
				try:
					prop.remove(j)
				except:
					continue
			for j in prop:
				if j not in graph:
					dict3 = {}
					dict3['word'] = j
					dict3['graph'] = []
					doc3.insert(dict3)
					flag = True
	else:
		dict['collection'] = i
		dict['fields'] = prop
		doc2.insert(dict)
		for j in notused:
			try:
				prop.remove(j)
			except:
				continue
		for j in prop:
			if j not in graph:
				dict3 = {}
				dict3['word'] = j
				dict3['graph'] = []
				doc3.insert(dict3)
				flag = True
if flag:
	print "Wordgraph Updated"
