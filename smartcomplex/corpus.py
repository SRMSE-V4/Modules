disc = ["a","an","the","of","is","was","in","during","got","are","did","took","belongs","to","has","at","on","and"
        ,"or","me","around","near","celebrated","celebrate","regarding","into","came","action","existence","exist","rule","legal","become"
	,"became","does","political","records","any","home","located","total","how","much","with","my","nearest","based","as","being"
	,"done","found","under","can","you","get","for","offered","offer","by","many","that","have","draw","it","so","draws"
	,"whome","included","include","through","go","said","happened","whom","whose","who","this","water","body","neft","having"
	,"what","overall","moving","travelling","travel","go","going","goes","moves"
	,"if","then","than","be","could","been","weapon","belong"
        ,"shown","hit","come","happen","strike","earthquake","related","relate","relates","relating","called","tell","known"
	, "famous","famously","prize","national","most","read","both","record","recorded","live","will","goes","stretch","run","over",
	  "pass","through","number","numbers","where","from","performed","won","olympics","university","talks","were"]
t = ["train","trains","passenger","express"]
w = ["weather","weathers","climate","climates","climatic"]
s = ["stock"]#other stock terms if required
m = ["gold","silver","oil"]#other mineral terms if required
sp = ["score","cricket"]#other sports terms if required
low = ["less","lesser","lower","smaller"]
high = ["high","higher","more","greater"]
maxi = ["maximum","highest","tallest","largest","longest"]
mini = ["minimum","least","smallest","tiniest","deepest"]
avg = ["average","mean"]
summ = ["total","sum","aggregate"]
ordins = ["hundred","thousand","million","billion","trillion","lakh","crore"]
normal = {"one":"first","two":"second","three":"third","four":"fourth","five":"fifth","six":"sixth",
	  "seven":"seventh","eight":"eighth","nine":"ninth","ten":"tenth","eleven":"eleventh","twelve":"twelfth","thirteen":"thirteenth",
	  "fourteen":"fourteenth","fifteen":"fifteenth","sixteen":"sixteenth","seventeen":"seventeenth","eighteen":"eighteenth", 		  "ninteen":"ninteenth","twenty":"twentieth","thirty":"thirtieth","forty":"fortieth","fifty":"fiftieth","sixty":"sixtieth",
	  "seventy":"seventieth","eighty":"eightieth","ninty":"ninetieth","hundred":"hundredth","thousand":"thousandth","million":"millionth",
	  "billion":"billionth","trillion":"trillionth","lakh":"lakth","crore":"croreth"}
endins = ["st","nd","rd","th"]
extras = ["and"]
totalnum = []
totalnum.extend(normal.keys())
totalnum.extend(normal.values())
totalnum.extend(extras)
calender = ["day","days","week","weeks","year","years","month","months","decade","century","decades","centuries"]
yearbox = ["year","years","decade","decades","century","centuries"]
negetive = ["previous","yesterday","before","back","less","earlier"]
positive = ["next","tomorrow","after","forthcoming","later","more"]
daters = []
daters.extend(calender)
daters.extend(yearbox)
daters.extend(negetive)
daters.extend(positive)
