from datetime import date 
import calendar

r=[]
n=int(input())
for i in range(0,n):
	y=int(input())

	x=date(y,3,8).weekday()
	z=calendar.day_name[x]

	r.append(z)


for i in range(0,n):
	print(r[i])
