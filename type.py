if __name__ == '__main__':
    N = int(input())
    s=[]
    list=[]
    for i in range (0,12):
        s=input().split()
      
        if(s[0]=="insert"):
            a=int(s[1])
            b=int(s[2])
            list.insert(a,b)
            print(list)
        if(s[0]=="print"):
            print(list)
        if(s[0]=="remove"):
            a=int(s[1])
            print(list)
            list.remove(a)
        if(s[0]=="append"):
            a=int(s[1])
            list.append(a)
            print(list)
        if(s[0]=="sort"):
            list.sort()
            print(list)
        if(s[0]=="pop"):
            list.pop()
            print(list)
        if(s[0]=="reverse"):
            list.reverse()
            print(list)
            
