n=int(input())
r=0
for i in range(0,n):
	s=list(map(int,input().split()))
	if(s[0]!=s[1]):
		if(s[1]-s[0]>=2):
			r=r+1


print(r)