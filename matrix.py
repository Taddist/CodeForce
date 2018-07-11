#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
result=0
result1=0
sum=0
b=n%2
j=0
if(b==0):  
   
    for i in range(0,int(n/2)):
        result=result+a[i][j]-a[i][n-1-j]
        j=j+1
        
    for i in range (int(n/2),n)  :
        j=j-1
        result=result+a[i][n-1-j]-a[i][j]
        
        
if(b!=0):  
    
    for i in range(0,int(n//2)):
        result=result+a[i][j]-a[i][n-1-j]

        j=j+1
   
      
    for i in range (int(n/2)+1,n)  :
        j=j-1 
     
        result1=result1+a[i][n-1-j]-a[i][j]
        
    
       
              
sum=result+result1
k=abs(sum)  
print(k)
        