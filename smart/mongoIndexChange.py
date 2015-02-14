from pymongo import MongoClient as mc
import re
import getword
client=mc()

db = client.rig #this is to select the database

nolist=['id','sno','SNo','Sno','_id']
notable=['hotels','placesindia','newretriv','newretriv1','atms','wordmatrix','rlink','train','map','map1','stackoverflow','stackoverflow1','bankdetails','banklink','bankterms','food','religious','pubs','retriv','retriv1']

dicti={}
def runFun():
    collections=db.collection_names()
    collections.pop(0)
    
    for collection in collections:
        if collection not in notable:
            print collection

            data=db[collection].find()

            getDataFromCollections(str(collection),data)

            


def getDataFromCollections(collection,data):

    k=[]
    global dicti
    for dat in data :
        
      #  print dat
        k=dat.keys()
        for key in dat.keys():
            key=str(key)
            if key not in nolist and dat[key]:
                regex=re.compile('[%s]'% re.escape('!"#$%&\'()*+,-.:;<=>?@[\\]^_`{|}~'))
                content=str(dat[key]).lower()
                content=re.sub(regex," ",content)
                addToDict(collection,content,key)
                
    
    addToDbase()
    print dicti
    #returnData=list(set(cont.split()+k))
    
   # return returnData

def addToDbase():
    global dicti

    for key in dicti.keys():
        checkDict={}
        checkDict["keyword"]=key
        newDict=dicti[key]
        newDict.update({"keyword":key})
    #    print newDict
        
        db.newIndex1.update(checkDict,{"$set":newDict},True)
    
    dicti={}

def addToDict(collection,content,key):

    global dicti
    words=content.split()

    for word in words :
        word=str(word)
        if dicti.has_key(word):
            subDict=dicti[word]
            if subDict.has_key(collection):
                superSubDict=dicti[word][collection]
                if superSubDict.has_key(key):
                    dicti[word][collection][key]=int(superSubDict[key])+1
            
                else:
                    dicti[word][collection][key]=1
            else:
                dicti[word][collection]={}
                dicti[word][collection][key]=1
        else:
            dicti[word]={}
            dicti[word][collection]={}
            dicti[word][collection][key]=1
        pop=[]
        pop.append(word)
        varKeys=getword.getwordtonum(pop)

        if varKeys:

            k=varKeys.pop(0)
            for word1 in varKeys:
                if dicti.has_key(word1):
                    subDict=dicti[word1]
                    if subDict.has_key(collection):
                        superSubDict=dicti[word1][collection]
                        if superSubDict.has_key(str(k)):
                            subSuperSubDict=dicti[word1][collection][str(k)]
                            if subSuperSubDict.has_key(key):
                                dicti[word1][collection][str(k)][key]=int(subSuperSubDict[key])+1
                                    
                            else:
                                dicti[word1][collection][str(k)][key]=1
                        else:
                            dicti[word1][collection][str(k)]={}
                            dicti[word1][collection][str(k)][key]=1        
                    else:
                        dicti[word1][collection]={}
                        dicti[word1][collection][str(k)]={}
                        dicti[word1][collection][str(k)][key]=1
                else:
                    dicti[word1]={}
                    dicti[word1][collection]={}
                    dicti[word1][collection][str(k)]={}
                    dicti[word1][collection][str(k)][key]=1

                            
            
            

        
runFun()

#print dicti
