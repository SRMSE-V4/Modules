#use the command mongodump --db <database_name>
#it will be saved in the home directory /home/<name>/<database_name>/*.bson
#use this code to convert bson files to json files

import glob
import bson
db = raw_input("Enter the database name")
files = glob.glob("/home/abhay/dump/"+db+"/*.bson")
for i in files:
	i = i[::-1]
	i = i.split("/",1)
	i = i[0]
	i = i[::-1]
	bs = open("/home/abhay/dump/"+db+"/"+i, 'r').read()
	i = i.split(".bson",1)
	i = i[0]
	f = open("/home/abhay/dump/"+db+"/"+i+".json","a+")
	print i
	for valid_dict in bson.decode_all(bs):
		f.write(str(valid_dict))
	f.close()
