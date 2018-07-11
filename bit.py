n=int(input())
sum=0
for i in range(0,n):

	str=input()
	if(str.find("+")!=-1):
		sum=sum+1
	else :
		sum=sum-1

print(sum)