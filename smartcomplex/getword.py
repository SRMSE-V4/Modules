import corpus
import pymongo
import aiml
import commands
import inflect
import wordtonum 
import datetime
import re
from dateutil.relativedelta import relativedelta


def getwordtonum(query):
	wtn = []
	query = " ".join(query)
	flag,word,typer = idnum(query)
	if flag:
		for i in range(0,len(typer)):
			if(typer[i]=="<T1>"):
				wtnfinal = t1(word[i])
				query = query.replace(word[i],"")#"<number>")
				query = query.strip()
				wtn.append(wtnfinal)
			elif(typer[i]=="<T2>"):
				wtnfinal = t2(word[i])
				query = query.replace(word[i],"")#"<number>")
				query = query.strip()
				wtn.append(wtnfinal)
	flag,word,typer = idword(query)
	if flag:
		for i in range(0,len(typer)):
			if(typer[i]=="<T3>"):
				wtnfinal = t3(word[i])
				query = query.replace(word[i],"")#"<number>")
				query = query.strip()
				wtn.append(wtnfinal)
			elif(typer[i]=="<T4>"):
				wtnfinal = t4(word[i])	
				query = query.replace(word[i],"")#"<number>")
				query = query.strip()
				wtn.append(wtnfinal)
	
	if len(wtn)==0:
		wtn = "<NA>"
		return None
	return map(str,wtn[0])

def idnum(query):
	flag = False
	word = []
	word1 = []
	word2 = []
	typer = []
	reg = r'[0-9]+th|[0-9]+nd|[0-9]+rd|[0-9]+st'
	temp = re.findall(reg,query)
	word1.extend(temp)
	if len(word1)>0:
		flag = True
		for i in range(0,len(word1)):
			query = query.replace(word1[i],"<number>")
			query = query.strip()
			typer.append("<T1>")
	reg = r'[0-9]+'
	temp = re.findall(reg,query)
	word2.extend(temp)
	if len(word2)>0:
		flag = True
		for i in range(0,len(word2)):
			query.replace(word2[i],"<number>")
			query = query.strip()
			typer.append("<T2>")
	word.extend(word1)
	word.extend(word2)
	yield flag
	yield word
	yield typer



def idword(query):
	flag = False
	word = []
	typer = []
	totalnum = corpus.totalnum
	normal = corpus.normal
	temp = ""
	query = query.split()
	for i in range(0,len(query)):
		if query[i] in totalnum:
			temp = temp+" "+query[i]
			temp = temp.strip()
			if i==len(query)-1:
				word.append(temp)
				temp = temp.split()
				if temp[len(temp)-1] in normal.values():
					typer.append("<T3>")
				else:
					typer.append("<T4>")
		else:
			word.append(temp)
			temp = temp.split()
			if len(temp)>0:
				if temp[len(temp)-1] in normal.values():
					typer.append("<T3>")
				else:
					typer.append("<T4>")
			temp = ""
	while "" in word:
		word.remove("")		
	if len(word)>0:
		flag = True
	yield flag
	yield word
	yield typer

def getwords(word,wtnfinal):
	p = inflect.engine()
	temp = p.number_to_words(word)
	temp = temp.replace(",","")
	temp = temp.replace("-"," ")
	temp = temp.strip()
	wtnfinal.append(temp)
	ordins = corpus.ordins
	temp = temp.split()
	if temp[0] in ordins:
		temp.insert(0,"one")
	temp = " ".join(temp)
	temp = p.ordinal(temp)
	wtnfinal.append(temp)
	return wtnfinal


def t1(word):
	p = inflect.engine()
	endins = corpus.endins
	wtnfinal = []
	wtnfinal.append(word)
	for i in endins:
		if i in word:
			word = word.replace(i,"")
			wtnfinal.insert(0,word)
			break
	wtnfinal = getwords(word,wtnfinal)
	return wtnfinal

def t2(word):
	wtnfinal = []
	p = inflect.engine()
	wtnfinal.append(word)
	wtnfinal.append(p.ordinal(word))
	wtnfinal = getwords(word,wtnfinal)
	return wtnfinal

def t3(word):							
	wtnfinal = []
	normal = corpus.normal
	ordins = corpus.ordins
	p = inflect.engine()
	wtnobj = wordtonum.WordsToNumbers()
	word = word.split()
	temp = normal.keys()[normal.values().index(word[len(word)-1])]
	word.remove(word[len(word)-1])
	word.append(temp)
	if word[0] in ordins:
		word.insert(0,"one")
	word = " ".join(word)
	num = wtnobj.parse(word)
	wtnfinal.append(word)
	wtnfinal.insert(0,num)
	wtnfinal.insert(1,p.ordinal(num))
	temp = p.ordinal(word)
	wtnfinal.append(temp)	
	return wtnfinal

def t4(word):
        
        wtnfinal = []
        try:
                ordins = corpus.ordins
                word = word.split()
                if word[0] in ordins:
                        word.insert(0,"one")
                word = " ".join(word)
                wtnfinal.append(word)
                p = inflect.engine()
                wtnobj = wordtonum.WordsToNumbers()
                num = wtnobj.parse(word)
                wtnfinal.insert(0,num)
                wtnfinal.insert(1,p.ordinal(num))
                word = word.split()
                normal = corpus.normal
                if word[len(word)-1] in normal.keys():
                        word.insert(len(word)-1,normal[word[len(word)-1]])
                        word.remove(word[len(word)-1])
                wtnfinal.append(" ".join(word))
        except Exception as x:
                pass

        return wtnfinal
