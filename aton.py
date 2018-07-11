n=int(input())
sum=0
for i in range(0,n):
	str=input()
	if (str=="Tetrahedron"):
		j=4
	if (str=="Cube"):
		j=6
	if (str=="Octahedron"):
		j=8
	if (str=="Dodecahedron"):
		j=12
	if (str=="Icosahedron"):
		j=20

	sum=sum+j

print(sum)