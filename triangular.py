n=int(input())

t=[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406,435,465,496]
x=len(t)
j=0
for i in range(0,x):
	if(n==t[i]):
		j=1
		

if(j==1):
	print("YES")
else :
	print("NO")	