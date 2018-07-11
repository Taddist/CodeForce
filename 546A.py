l=list(map(int,input().split()))

k=l[0]
n=l[1]
w=l[2]

sum=0
for i in range(1,w+1):
	sum=sum+i*k

if(sum-n>=0):
	print(sum-n)

else:
	print(0)