
def getanswer(msg,query):
	if msg == "<train status>":
		ans = train(query)
	elif msg == "<weather status>":
		ans = weather(query)
	elif msg == "<stock status>":
		ans = stock(query)
	elif msg == "<mineral status>":
		ans = mineral(query)
	elif msg == "<sports status>":
		ans = sports(query)
	elif msg == "<movie review>":
		ans= movie(query)
        elif msg == "<exam status>":
                ans= exam(query)
        elif msg == "<locationcentric module>":
                ans= location(query)
                



	return ans



def location(query):
        ans="<NA>"
        
        import locentric as location
        ans = location.main(query)
	if ans :
           ans=[{"location":ans}]
	#print ans
	return ans



def exam(query):
        ans="<NA>"
        import exam
        ans = exam.main(query)
        if ans :
           ans=[{"exam":ans}]
        return ans


def movie(query):
	ans="<NA>"
	import movieretrieve1 as mv
	
	ans = mv.new_movies(query)

	if ans :
	   ans[0]={"movie":ans[0]}
	
	return ans 
	
def train(query):
	ans = "<NA>"
        import train
        ans = list(train.main(query))
        #print ans
        if ans:
           ans={"train":ans}
        #print ans
	return [ans]

def weather(query):
        import weatherRetriv as wr
        
	ans = "<NA>"
	ans=wr.queryRetriv(query)
	#print ans
	if ans.has_key('time'):
		ans.pop('time')
	if ans.has_key('id'):
		ans.pop('id')
	
	
	return [{"weather":ans}]

def stock(query):
	import stockRetriv as sr
	ans = "<NA>"
	ans= sr.getResults(query)
	if ans:
	   ans[0]={"stock":ans[0]}
	return ans

def mineral(query):
	ans = "<NA>"
	return ans

def sports(query):
	ans = "<NA>"
	
	import score 
	
	ans= score.scoreRetriv(query)
	if ans:
	   ans[0]={"sports":ans[0]}
	return ans

