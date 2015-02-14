from pymongo import MongoClient as MC

client = MC()

dbkb = client.kb

dbcomplex = client.kbcomplex

def getFromCollection(collection):

    coll=dbkb[collection] # this is the collection

    content = list(coll.find())

    return content

def main():

    contents = getFromCollection('war')
    newcontent=[]
    for content in contents:
        try:
            start = int (content['start'].strip())
            finish= int (content['finish'].strip())+1

            duration = range(start,finish)

            content['complexwhen']=duration
            newcontent.append(content)
        except Exception as x:
            print x
    dbcomplex['war'].insert(newcontent)


main()

        
        
        
    
