t=int(input())

v=[]
for i in range(0,t):
	s=list(map(int,input().split()))
	r=[0]
	r.append(s[2])
	r.append(s[1])
	r.append(s[0])
	n=s[3]

	for j in range(4,n+1):

		r.append(28*r[j-1]-175*r[j-2]+300*r[j-3])

	v.append(r[n]%1000000007)


for k in range(0,t):
	print(v[k])
