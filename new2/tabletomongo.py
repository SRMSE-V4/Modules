import MySQLdb
import pymongo
import datetime
import sys
from decimal import *

#Get the table name
#Read record by record
#For special rows identify delimiter and put it in array
#Do the type casting and add the property which is the unti
#Upload the dictory record by record

db = MySQLdb.connect("127.0.0.1","root","4faces","pending")
mdb = pymongo.MongoClient()
cursor = db.cursor()
mcursor = mdb['rig']

fields = []
checkers = [""," "]
replacers = ["\n","\r","\0","&amp;"]
table_name = raw_input("Table Name : ")
doc = mcursor[table_name]
delimiter = raw_input("Delimiter : ")
n = input("Enter number of columns to be delimited : ")

for i in range(0,n):
	temper = input("Delimited Field : ")
	fields.append(temper)

def getfilter(string,delimiter,field):
	string = string.lower()
	if field in fields:
		string = string.split(delimiter)
	return string

sql = "SELECT * FROM `"+table_name+"`;"
cursor.execute(sql)
results = cursor.fetchall()
for i in range(0,len(results)):
	cols = []
	sql = "SHOW COLUMNS FROM `"+table_name+"`;"
	cursor.execute(sql)
	resultz = cursor.fetchall()
	for row in resultz:
		cols.append(row[0])
	dict = {}
	for j in range(0,len(results[i])):
		if(results[i][j]!=None):
			flag = True
			temp = results[i][j] 
			if temp is str:
				temp = temp.strip()
			for k in checkers:
				if k == temp:
					flag = False
			if flag:			
				if type(results[i][j]) is str:
					temp = temp.decode('unicode_escape')
					temp = temp.encode('ascii','ignore')
					for k in replacers:
						temp = temp.replace(k,"")
					temp = getfilter(temp,delimiter,j)
					dict[str(cols[j])] = temp
				else:
					if type(temp) is datetime.timedelta:
						continue
					elif type(temp) is datetime.date:	
						continue
					elif Decimal(temp):
						temp = float(temp)
					elif Decimal(0.00)==temp:
						temp = 0
					dict[str(cols[j])] = temp
	doc.insert(dict)
print "DONE!"
