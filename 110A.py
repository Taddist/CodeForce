l=list(map(int,input()))
n=len(l)
c=0
for i in range (0,n):

	if((l[i]!=4) and (l[i]!=7) ):
		
		c=1
		break


if(c==0):
	print("YES")

else : 
	print("NO")


