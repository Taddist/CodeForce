

r=[]
n=int(input())
t=[0,3,2,5,0,3,5,1,4,6,2,4]
for i in range(0,n):
	y=int(input())
	
	
	g=(y+(y/4)-1+t[2]+8)%7
	
	r.append(int(g))


for j in range(0,n):

	if(r[j]==1):
		print("Monday")
	if(r[j]==2):
		print("Tuesday")
	if(r[j]==3):
		print("Wednesday")
	if(r[j]==4):
		print("Thursday")
	if(r[j]==5):
		print("Friday")
	if(r[j]==6):
		print("Saturday")
	if(r[j]==0):
		print("Sunday")
	