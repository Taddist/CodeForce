s=input()
l=list(s)
if(l[0].islower()==True):
    l[0]=l[0].upper()
           
f = ''.join(map(str, l))
    #f=''.join(str(x) for x in L)

print(f)