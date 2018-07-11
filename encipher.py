n=int(input())
r=[]
for i in range(0,n):
	l=list(map(int,input().split()))
	a=int(l[0])
	b=int(l[1])
	str=list(input())


	string=""
	for j in range(0,b):
		if(j%2==0) or (j%3==0):

			if(str[j]=="@"):
				string=string+"#"
			else :
				p=ord(str[j]) + a
				print("Calcul:",p)
				
				sub=p-122
				if(sub>0):
					st=chr(ord("a")+sub-1)
				else:
					
					st=chr(p)
					print("somme: ",st)
				string=string+st
		else :
			string= string+str[j]
			print("il n'est pas traite",str[j])
	r.append(string)

for i in range(0,n):
	print(r[i])

