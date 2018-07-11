

n=int(input())
str=""
for i in range(0,n):
	k=int(input())
	string=bin(k)

	sum=0
	i=string.find("1")
	while(i>=0):
		string=string[:i]+string[i+1:]
		sum=sum+1
		i=string.find("1")
	if(sum%2==0):
		str=str+"0"
	else :
		str=str+"1"
 


print(str)



