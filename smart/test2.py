#!usr/bin/python
import gla
import stats
import special
import retriv1
import cgi
#print "Content-type:text/html\r\n\r\n"
def get(query):
	query = gla.gaiml(query)
	#print "#------------------------AIML------------------#"
	#print query
	for i in query:
		query = gla.gdisc(i)
		#print "#------------------------DISC------------------#"
		#print "Rest :",query
		msg = gla.gspl(query)
		
		if msg!="":
			#print "here"
			#print "#------------------------SPL-------------------#"
			ans = special.getanswer(msg,query)
			#return ans
			#print msg,":",ans
		else:
			query,cols = gla.wordmatrix(query)
			#print "#-----------------------WM---------------------#"
			#print "Rest :",query
			#print "Fields :",cols
			#print "#-----------------------TAB---------------------#"
			tabs = gla.gettable(query,cols)
			#print "Tables :",tabs
			#print "#----------------------STATS--------------------#"
			flag,field,table = gla.getstats(query)
			if flag:
				ans = stats.grapher(table,field)
			else:
				print ""
			#print "#-----------------------LOG---------------------#"
			query,symbol,wtn,date = gla.logic(query)
			#print wtn

			#print "Rest :",query
			#print "Symbol :",symbol
			#print "Values :",wtn
			#print "Date :",date
			#print "#---------------------RETRIV--------------------#"
			ans = retriv1.getanswer(query,symbol,wtn,date)
			ans[0]={"general":ans[0]}
			#print "Ans :",ans		
		#print "#---------------------END----------------------#" 
		return ans
