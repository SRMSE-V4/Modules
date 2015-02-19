import gla
import stats
import special
import retriv2


def getQuery(query):
    
    query = gla.gaiml(query)
    #print"#------------------------AIML------------------#"
    #printquery
    for i in query:
            query = gla.gdisc(i)
            tquery=query
            #print"#------------------------DISC------------------#"
            #print"Rest :",query
            msg = gla.gspl(query)
            if msg!="":
                    #print"#------------------------SPL-------------------#"
                    ans = special.getanswer(msg,query)
                    #printmsg,":",ans
            else:
                    query,cols = gla.wordmatrix(query)
                    #print"#-----------------------WM---------------------#"
                    #print"Rest :",query
                    #print"Fields :",cols
                    #print"#-----------------------TAB---------------------#"
                    tabs = gla.gettable(query,cols)
                    #print"Tables :",tabs
                    #print"#----------------------STATS--------------------#"
                    flag,field,table = gla.getstats(query)
                    if flag:
                            ans = stats.grapher(table,field)
                    else:
                            print"Stats : <NA>"
                    #print"#-----------------------LOG---------------------#"
                    query,symbol,wtn,date = gla.logic(query)
                    #print"Rest :",query
                    #print"Symbol :",symbol
                    #print"Values :",wtn
                    #print"Date :",date
                    #print"#---------------------RETRIV--------------------#"
                    ans = retriv2.getanswer(tquery,symbol,wtn,date)
                    #print"Ans :",ans
                
                    return ans 
            #print"#---------------------END----------------------#" 
