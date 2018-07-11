l=list(input())
n=len(l)
low=0
up=0
for j in range(0,n):

	if(l[j].islower()==True):
		low=low+1

	else :
		up=up+1

f = ''.join(map(str, l))

if(low >= up):

	print(f.lower())

if(up>low):

	print(f.upper())