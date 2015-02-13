#!/usr/bin/python

import MySQLdb
import json
print "Content-type:text/html\n\r\n\r"
con = MySQLdb.connect("127.0.0.1", "root", "ashwin", "user_defined")
cur = con.cursor()
sql = "SELECT `currency` FROM `currency`"
cur.execute(sql)
data = cur.fetchall()
countries = []
for x in data:
	countries.append(x[0])
print json.dumps(countries)