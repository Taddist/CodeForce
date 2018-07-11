T=int(input())


for i in range(0,T):
	r=[]
	s=list(map(int,input().split()))
	l=s[0]
	sum=0
	for j in range(1,l+1):
		sum = sum+s[j]

	v=list(map(int,input().split()))
	
	m=v[0]
	for k in range(1,m+1):
	    if(sum>=v[k]):
	        r.append(v[k])
    
	if (len(r)!=0):
		print("YES")
	else:
		print("NO")



