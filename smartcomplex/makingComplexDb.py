from pymongo import MongoClient as MC

client = MC()

dbkb = client.kb

dbcomplex = client.kbcomplex

#configDict={'acts':'date','carprodstats':'year','nationalparks':'Founded','noble':'year','party':'year','pastmps':'Year','psu':'founded','amendments':{'field':'date','delimiter':' ','position':2},'articles':{'field':'date','delimiter':' ','position':2},'movies_reviews':{'field':'release','delimiter':',','position':1},'highcourts':{'field':'founded','delimiter':'-','position':0}}
configDict={'earthquake':{'field':'Date','delimiter':'/','position':2}}
def getFromCollection(collection):

    coll=dbkb[collection] # this is the collection

    content = list(coll.find())

    return content


# complexwhen = some field value 
def equalType(collection,field):
    print "Started "+collection
    contents = getFromCollection(collection)
    newcontent= []
    
    for content in contents :
        try:
            content['complexwhen']=[int(content[field])]

            newcontent.append(content)
        except Exception as x:
            print x
    dbcomplex[collection].insert(newcontent)


# when some split operation has to be performed

def splitType(collection,details):
    print "Started "+collection 
    contents = getFromCollection(collection)
    newcontent=[]

    for content in contents :
        try:

            field = details['field']
            delimiter=details['delimiter']
            position= details['position']

            fieldContent = content[field]
            splitContent=fieldContent.split(delimiter)
            complexwhen=splitContent[position].strip()

            if (len(complexwhen)!=4):
                complexwhen = "20"+complexwhen

            complexwhen = int(complexwhen)
            content['complexwhen']= [complexwhen]
            newcontent.append(content)
        except Exception as x:
            print x
        
    dbcomplex[collection].insert(newcontent)
        
        
        
def main():
    
    keys = configDict.keys()

    for key in keys:

        if type(configDict[key]) is dict:
            splitType(key,configDict[key])
        else:
            equalType(key,configDict[key])

        print "Completed "+ key

