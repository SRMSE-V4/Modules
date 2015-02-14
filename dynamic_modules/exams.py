from bs4 import BeautifulSoup

import urllib2

import time

import MySQLdb

print (time.strftime("%m"))

# This is to get the details about the exam
def getExams(source):

    db=MySQLdb.connect('127.0.0.1','root','root','test')
    cursor=db.cursor()
    

    soup=BeautifulSoup(source)

    div = soup.findAll('div',{'class':'exam-det'})

    for d in div :

        examsoup = BeautifulSoup(str(d))
 
        nametag = examsoup.find('h2')

        # to get the name of the exam
        namesoup = BeautifulSoup(str(nametag))

        name=namesoup.find('a').text

        course=namesoup.find('span',{'class':'course-box'}).text

        course=course.replace('(','').replace(')','')


        print "Name: "+name
        print "Course: "+course

        #to get the fullform of exam 
        full = examsoup.find('p',{'class':''}).text
        print "Full : "+full

        #to get the exam type

        lis = examsoup.findAll('p',{'class':'exams-p'})

        pattern = lis[0].text

        date = lis[1].text

        collegessoup= BeautifulSoup(str(lis[2]))

        collegelink = collegessoup.find('a').attrs['href']

        print "Patterns : "+ pattern

        print "Date : "+ date
        lis=[]
        try:

            lis=getColleges(str(collegelink))

        except Exception as x:

            print x


        sql = """INSERT INTO exams(name,course,fullform,pattern,date,colleges) VALUES ("%s","%s","%s","%s","%s","%s")"""%(name,course,full,pattern,date,str(lis))
        cursor.execute(sql)
        db.commit()
        print " \n\n\n======================== \n\n\n "
    db.close()


def getColleges(url):

    page=urllib2.urlopen(url)

    source = page.read()

    lis=[]

    soup = BeautifulSoup(source)

    colleges=soup.findAll('h2',{'class':'college_name'})

    for college in colleges:

        lis.append(str(college.text))

    print lis

    return lis


def urlFun(i):

    page=urllib2.urlopen("http://www.indiacollegesearch.com/exams?month="+str(i))

    source =page.read()

    getExams(source)
    


def callFun():
    db=MySQLdb.connect('127.0.0.1','root','root','test')
    cursor=db.cursor()
    
    sql = "TRUNCATE exams"
    cursor.execute(sql)
    db.commit()

    month= int(time.strftime("%m"))

    for i in range(month,13):
        try:
            print "\n Month %s Started \n"%str(i)
            urlFun(i)
            print "\n Month %s Completed \n"%str(i)
        except Exception as x:
            print x
            print "----"
    
    
            
callFun()
            
        

        

            


        

        
