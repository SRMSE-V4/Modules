import pymongo
client = pymongo.MongoClient()
mdb = client['rig']
wm = mdb['wordmatrix']
regex = 'change'
results = wm.find({'matrix':{'$regex':regex}})
#results = wm.find()
for row in results:
	print row['word']
