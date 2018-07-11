T=int(input())
for i in range(0,T):

  	s=input()
  	l=list(s)
  	n=len(l)
  	if(n>10):

  		R=l[0]+str(n-2)+l[n-1]
  		print(R)
  	else :
  		print(s)