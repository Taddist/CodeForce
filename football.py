s=input()
l=list(map(int,s))
n=len(l)
start=l[0]
c=0
k=1
r=[]
for i in range(1,n):
	if(l[i]==start):
		if(k<7):
			k=k+1
			if(k>=7):
				c=1
				r.append(10)
				
	else :
		k=1
		
	start=l[i]

if(len(r)!=0):
    print("YES")
if (c== 0 ): 
	print("NO")