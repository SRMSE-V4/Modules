
from pymongo import MongoClient as mc
import re
import string

client=mc()
db=client.rig


def removePandS(content):
    re.sub(r'\b\w{,2}\b',' ', content)
    re.sub(r'\b\w{15,}\b',' ', content)
    regex=re.compile('[%s]'% re.escape(string.punctuation))
    content=re.sub(regex," ",content)
    stop_words=set(["a","a's","belongs","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","just","keep","keeps","kept","know","known","knows","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","que","quite","qv","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","value","various","very","via","viz","vs","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","would","wouldn't","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"])
    a=" ".join(word for word in content.split() if word not in stop_words)
    return a.split()




def queryRetriv(query):
    #keys=removePandS(query)
    keys=query.lower().split()
    #print keys
    get=db.newIndex.find({"keyword":{"$in":keys}})
    sendDict={}
    get=list(get)
    store=get
    for ge in store:
        ge.pop('_id')
        keyword=ge["keyword"]
        lis=ge.keys()     
        lis.pop(lis.index("keyword"))
        sendDict[keyword]=lis

    keyword=[]
    fieldKeyword=[]
    if sendDict:
        data=getIntersection(sendDict)
        anotherDict={}
        for key in keys:

            for dat in data:
                
                for st in store:
                   
                    if st["keyword"]==key:
                        if not anotherDict.has_key(dat):
                            anotherDict[dat]={}
                        dt={key:st[dat]}
                        anotherDict[dat].update(dt)
                        #print st[dat]
                        if str(st[dat])=="field":
                            fieldKeyword.append(key)
                            if not anotherDict[dat].has_key("priority"):
                                anotherDict[dat]["priority"]=10
                            else:
                                anotherDict[dat]["priority"]+=10
                        elif str(st[dat])=="categories":
                            fieldKeyword.append(key)
                            if not anotherDict[dat].has_key("priority"):
                                anotherDict[dat]["priority"]=30
                            else:
                                anotherDict[dat]["priority"]+=30
                            
                        else:
                            if not anotherDict[dat].has_key("priority"):
                                anotherDict[dat]["priority"]=1
                            else:
                                anotherDict[dat]["priority"]+=1
                            keyword.append(key)
                            

        return retrieveResults(anotherDict,keyword,fieldKeyword,keys)
            

def getIntersection(sendDict):
    k=[]

    k=map(set,sendDict.values())

    inter=set(k[0]).intersection(*k)

    return list(inter)
    



def retrieveResults(anotherDict,keyword,fieldKeywords,keys):

    prio={} 
    part={}
    
    for key in anotherDict.keys():
        a=[]
        prio[key]=anotherDict[key]["priority"]
        if (key!='priority' and anotherDict[key]!='field'):
            k=anotherDict[key].keys()
            for field in anotherDict[key].keys():
                if anotherDict[key][field]=="field" or anotherDict[key][field]=="categories" :
                    k.pop(k.index(field))
                elif field!="priority":
                    prio[key]-=sum(anotherDict[key][field].values())
            k.pop(k.index("priority"))
            part[key]=k
            
    return retrivAnswer(anotherDict,part,prio,keys)



def retrivAnswer(anotherDict,part,prio,keys):
    
    reqCollections=sortDict(prio) # these are the required collections with priority
    
    for collection in reqCollections:
        
        keywords=part[collection]
        interList=[]    
        for keyword in keywords:
            interList+=anotherDict[collection][keyword].keys()
        
       
        break
    tempKey={}
    
    coll=reqCollections[0]
     
    interList=list(set(interList))
    
    returnresult={}
    for key in keys:
        
        for field in interList:
            try:
                if not returnresult.has_key(field):
                    returnresult[field]=[]
                if type(anotherDict[coll][key]) is dict:
                    if anotherDict[coll][key].has_key(field):
                    
                        returnresult[field].append(key)
            except Exception as x:
                print x
     
    ans=printResult(reqCollections[0],returnresult,sortDictLen(returnresult),part[reqCollections[0]],keys)
    return ans
        

        
            

def printResult(collection,returnresult,sodict,keys,keywords):
    
    mainQuery={}
    mainQuery[collection]={}
    checkList=[]
    temp=[]
    for key in sodict:

        lis=returnresult[key]
        if not temp:
            temp+=lis
            mainQuery[collection][key]=" ".join(lis)
            mainQuery[collection][key]={}
            mainQuery[collection][key]['$regex']="(?=.*"+(".*)(?=.*".join(lis))+".*)"
            mainQuery[collection][key]['$options']='-i'
        elif not list(set(temp) & set(lis)):
            temp+=lis
            mainQuery[collection][key]={}
            mainQuery[collection][key]['$regex']="(?=.*"+(".*)(?=.*".join(lis))+".*)"
            mainQuery[collection][key]['$options']='-i'
        if len(list(set(temp)))==len(keys):
            break

    
    collection=mainQuery.keys()[0]    
    #print collection
    #print mainQuery[collection]
    
    ans = list(db[collection].find(mainQuery[collection]))
    #print ans
    return ans

    
    

def sortDict(dicti):
    lis=sorted(dicti, key=lambda key: dicti[key],reverse=True)
    return lis


def sortDictLen(dicti):
    lis=sorted(dicti, key=lambda key: len(dicti[key]),reverse=True)
    return lis



    
    
