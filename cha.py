t=int(input())

for i in range(0,t):
	l=list(map(int,input().split()))
	a=l[0]
	b=l[1]
	
	sum=0
	g=0
	

	l1=list(map(int,input().split()))
	l1.sort(reverse=True)
	print(l1)
	c=0
	for k in range(0,b):
		if(c==0):
			sum=sum+l1[k]
			g=g+1
			

		if(sum>=a):
			c=1
	print(g)


