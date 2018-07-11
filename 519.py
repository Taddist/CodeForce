r=[]

white=0
black=0
for k in range(0,8):

	l=list(input())
	r.append(l)


for i in range(0,8):
	for j in range(0,8):
		if(r[i][j].isalpha()==True):
			if(r[i][j].islower()==True):
				if(r[i][j]=="q"):
					black=black+9
				if(r[i][j]=="r"):
					black=black+5
				if (r[i][j]=="b" or r[i][j] == "n" ) :
					black=black+3
				if(r[i][j]=="p"):
					black=black+1
			if(r[i][j].isupper()==True):
				r[i][j]=r[i][j].lower()
				if(r[i][j]=="q"):
					white=white+9
				if(r[i][j]=="r"):
					white=white+5
				if (r[i][j]=="b") or r[i][j] == "n" :
					white=white+3
				if(r[i][j]=="p"):
					white=white+1


if(white>black):
	print("White")

if(black>white):
	print("Black")

if(black==white):
	print("Draw")



