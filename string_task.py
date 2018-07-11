l=list(input())
str=""
for i in range(0,len(l)):
	if(l[i]!="A") and (l[i]!="a") and (l[i]!="O") and (l[i]!="o") and (l[i]!="Y")  and (l[i]!="y")  and (l[i]!="E") and (l[i]!="e") and (l[i]!="U") and (l[i]!="u") and (l[i]!="I") and (l[i]!="i")  :
		str=str+"."+l[i].lower()

print(str)
