n=int(input())

l=list(map(int,input().split()))

l.sort()

s=0

if(n==1) : s=0
else :

	for i in range(0,n-1):
		s=s+l[n-1]-l[i]


print(s)