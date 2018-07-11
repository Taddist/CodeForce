s=input().split()
a=int(s[0])
b=int(s[1])
s=0


for i in range (1,8):
	if(a<=b):
		s=s+1
		a=3*a
		b=2*b 
	else :
		print(s)
		break


   

    


