n=int(input())
r=[]
for i in range(0,n):
	m=int(input())
	t=[]
	s=0
	l=list(map(int,input().split()))
	for j in range (0,m-1):
		for k in range(j+1,m):
			if(l[j]>l[k]):
				s=s+1
	r.append(s)


for i in range(0,n):
	print(r[i])


