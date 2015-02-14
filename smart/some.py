#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
print """
<html>
<form action="./ask.py" method="get">
Ask Smartly: <input type="text" name="f">  <br />
<input type="submit" value="Submit" />
</form>
</html>
"""
