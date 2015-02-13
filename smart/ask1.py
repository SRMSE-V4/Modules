#!/usr/bin/python
import cgi,cgitb
form = cgi.FieldStorage()
f = form.getvalue("f","") #Gets input from the form
print "Content-type:text/html\r\n\r\n"
import test2
result = test2.get(f) #Gets result out of the smart answer module
result=result[0]
if result.has_key('_id'):
	result.pop('_id')
result=str(result).replace('"','\\"')
result=result.replace("u'",'"').replace("'",'"')
print result
#print "done"
