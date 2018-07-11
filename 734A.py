n=int(input())

l=list(input())

a=0
d=0

for i in range(0,n):

	if(l[i]=="A"):
		a=a+1
	else :
		d=d+1



if(a==d):
	print("Friendship")


if(a>d):
	print("Anton")

if(a<d):
	print("Danik")