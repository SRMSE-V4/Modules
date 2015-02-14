from pymongo import MongoClient as MC

client = MC()

db = client.kbcomplex

import stage1test
import stage2test


def retrivstage1(query):

    #print query

    ans1= stage1test.getQuery(query)

    #print ans1
    return ans1 

def complexQueryRetriv(query):

    queries = query.split("when")

    query1 = queries[0]

    query2 = queries[1]

    outputQuery1 = retrivstage1(query2)

    ans1=outputQuery1[0]

    dates= ans1['complexwhen']

    getMainQuery= stage2test.getQuery(query1)
    collection=getMainQuery.keys()[0]
    getMainQuery[collection]['complexwhen']={"$in":dates}
    
    
    ans = list(db[collection].find(getMainQuery[collection]))
    print ans
    

    #print getMainQuery
    #for date in dates:

    
query = raw_input("Enter Complex Query: ")
complexQueryRetriv(query)
    
    
