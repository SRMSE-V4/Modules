import MySQLdb
import pymongo

db = MySQLdb.connect("127.0.0.1","root","4faces","rig")
mdb = pymongo.MongoClient()
cursor = db.cursor()
mcursor = mdb['kb']
doc = mcursor['wordgraph']
query = "SELECT * FROM `wordmatrix`;"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
	dict = {}
	temp = row[0]
	key = temp.replace("`","")
	temp = row[1]
	temp = temp.split("|")
	temp = list(set(temp))
	temp.remove("")
	dict['word'] = key
	dict['graph'] = temp
	doc.insert(dict)
print "Done"

