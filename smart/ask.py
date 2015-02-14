#!/usr/bin/python
import cgi,cgitb
form = cgi.FieldStorage()
f = form.getvalue("f","") #Gets input from the form
import test2
#print "Content-type:text/html\r\n\r\n"
result = test2.get(f) #Gets result out of the smart answer module
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h5>%s</h5>" % (str(result))
print "</body>"
print "</html>" 
