

n=int(input())

ih="I hate "

th="I hate that I love"
t=" it"
s=""


if(n==1):
	print(ih+t)

if(n==2):
	print(th+t)

if(n>=3):
	if(n%2==0):
		n=n//2
		while(n>0):
			
			s=s+th
			n=n-1
			if(n>0):
				s=s+" that "

		print(s+t)
	else :
		n=n-1
		n=n//2
		while(n>0):
			
			s=s+th
			n=n-1
			if(n>=0):
				s=s+" that "

		print(s+ih+"it")


