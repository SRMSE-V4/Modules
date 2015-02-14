#!/usr/bin/python
import MySQLdb
import cgi
import json
data = cgi.FieldStorage()
print "Content-type:text/html\n\r\n\r"
con = MySQLdb.connect("127.0.0.1", "root", "ashwin", "user_defined")
cur = con.cursor()
country = data['country'].value
conversion = int(data['con'].value)
inr = float(data['value'].value)
def con(country, value):
	sql = "SELECT `conv` FROM `currency` WHERE `currency` = '%s'"%(country)
	cur.execute(sql)
	data = cur.fetchone()
	return float(data[0])*float(value)
def incon(country, value):
	sql = "SELECT `invconv` FROM `currency` WHERE `currency` = '%s'"%(country)
	cur.execute(sql)
	data = cur.fetchone()
	return float(data[0])*float(value)
condition = {
	0:con, 
	1:incon
	}
print json.dumps({"value":condition[conversion](country, inr), "conversion":conversion})