import MySQLdb
import pymongo
import datetime
import sys
from decimal import *

tabs = []
typer = []

db = MySQLdb.connect("127.0.0.1","root","4faces","rig")
mdb = pymongo.MongoClient()
cursor = db.cursor()
mcursor = mdb['rig']

cursor.execute('SHOW TABLES;')
tables = cursor.fetchall()
for table in tables:
	tabs.append(table[0])
tabs.remove('wordmatrix')
for i in range(0,len(tabs)):
	cols = []
	sql = "SHOW COLUMNS FROM `"+tabs[i]+"`;"
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		cols.append(row[0])
	sql = "SELECT * FROM `"+tabs[i]+"`;"
	cursor.execute(sql)
	results = cursor.fetchall()
	doc = mcursor[tabs[i]]
	for j in range(0,len(results)):
		try:
			dict = {}
			for k in range(0,len(results[j])):
				if(results[j][k]!=None):
					temp = results[j][k]
					if type(results[j][k]) is str:
						temp = temp.decode('unicode_escape')
						temp = temp.encode('ascii','ignore')
						temp = temp.replace("\n","")
						temp = temp.replace("\r","")
						temp = temp.replace("\0","")
						dict[str(cols[k])] = temp.lower()
					else:
						if type(temp) is datetime.timedelta:
							continue
						elif type(temp) is datetime.date:	
							continue
						elif Decimal(temp):
							temp = float(temp)
						elif Decimal(0.00)==temp:
							temp = 0
						dict[str(cols[k])] = temp
			doc.insert(dict)
		except Exception as e:
			print type(temp)
			print dict
			print e
			sys.exit()
