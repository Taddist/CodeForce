n=int(input())

l=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,n):
	if(l[i]%2==0):
		e.append(i+1)
	else :
		o.append(i+1)


if(len(e)<=1):
	print(e[0])


if(len(o)<=1):
	print(o[0])