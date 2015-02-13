import pymongo
import MySQLdb
client = pymongo.MongoClient()
mdb = client['rig']
db=MySQLdb.connect('127.0.0.1','root','4faces','rig')
cursor = db.cursor()
cursor.execute('SHOW TABLES;')
tables = cursor.fetchall()
tabs = []
for table in tables:
	tabs.append(table[0])
exceptions = ["bse","currency","earthquake","expressways","neft","people","tv_channels","weather","animals","highcourts","isd","party"]
for i in exceptions:
	tabs.remove(i)
for i in range(0,len(tabs)):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	sql = "SELECT * FROM `"+tabs[i]+"`;"
	cursor.execute(sql)
	dictlist = cursor.fetchall()
	dictlist = list(dictlist)
	dictlist = str(dictlist)
	dictlist = dictlist.decode('unicode_escape')
	dictlist = dictlist.encode('ascii','ignore')
	dictlist = dictlist.replace("\n","")
	dictlist = dictlist.replace("\r","")
	dictlist = dictlist.replace("\0","")
	dictlist = dictlist.lower()
	mcursor = mdb[tabs[i]]
	try:
		dictlist = eval(str(dictlist))
		mcursor.insert(dictlist)
	except Exception as e:
		print e
		print tabs[i]
		continue
