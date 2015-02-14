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
	return ans

def train(query):
	ans = "<NA>"
	return ans

def weather(query):
        import weatherRetriv as wr
        
	ans = "<NA>"
	ans=wr.queryRetriv(query)
	ans.pop('time')
	ans.pop('_id')
	return ans

def stock(query):
	ans = "<NA>"
	return ans

def mineral(query):
	ans = "<NA>"
	return ans

def sports(query):
	ans = "<NA>"
	return ans

