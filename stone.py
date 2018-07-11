n= int(input())

s=list(input())

r=0
k=s[0]
for i in range(1,n):
	if(s[i]==k):
		r=r+1

	k=s[i]

print(r)

