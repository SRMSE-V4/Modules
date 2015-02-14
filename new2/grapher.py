#Read from mysql and store in array
#Create a collection in a new db
#Start identifying unique id's to given data and create records
#Create a collection which contains the relations and corresponding id's
#there are two types of dictionaries
#Type-1 {ID:0001,data:United States of America,property:[name,country]},{ID:0002,data:21-03-1994,property:[date]},{ID:0003,data:200,Units:Rupee,property:[value,money]},{ID:0004,data:U.S.A,property:[shortform,short notation]}
#Type-2 {relation:[abbreviation,fullform,abbr],ID:0001,ID:0004} - Bidirectional Graph
#Read a document from the collection
#Get the two set of fields and make an edge(type-2 record) which is birectional (or) first->second,second->first unidirectional
#Remove the repetetions and find relations

import pymongo
from itertools import combinations

client = pymongo.MongoClient()
gdb = client['kbgraph']
mdb = client['kb']
newdoc = gdb['nodes']
cols = mdb.collection_names()
cols.remove("system.indexes")

def getcomb(inp): #Getting possible combinations of the given input array
	comb = []
	for i in combinations(inp,2):
		comb.append(i)
	return comb

#--------------------------------Getting nodes-------------------------------------------------------------------------------------------#
def generate_nodes():
	for i in cols:
		doc = mdb[i]
		results = doc.find()
		for row in results:
			keys = []
			keys.extend(row.keys())
			try:
				keys.remove(u'_id')
			except:
				print i
				pass
			for i in range(0,len(keys)):
				dict = {}
				dict['data'] = row[keys[i]]
				dict['property'] = [keys[i]]
				newdoc.insert(dict)
generate_nodes()
#-------------------------------Getting edges--------------------------------------------------------------------------------------------#
def generate_edges():
	for i in cols:
		doc = mdb[i]
		results = doc.find()
		for row in results:
			keys = []
			keys.extend(row.keys())
			try:
				keys.remove(u'_id')
			except:
				pass
			comb = getcomb(keys)
			for i in range(0,len(comb)):
				first = newdoc.find({"data":row[comb[i][0]]})			
				second = newdoc.find({"data":row[comb[i][1]]})
				for f in first:
					left = f[u'_id']
				for s in second:
					right = s[u'_id']
				print left,"<->",right,"Relation :",comb[i]
			break
#generate_edges()
#start the edge connections
