import math

def isPrime(num):


# Returns True if num is a prime number, otherwise False.

# Note: Generally, isPrime() is slower than primeSieve().

# all numbers less than 2 are not prime

	if num < 2:
		return False

	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False

	return True

if __name__ =="__main__":
	t=int(input())
	r=[]
	
	for i in range(0,t):
		v=[]

		f=[]
		n=int(input())
		l=list(map(int,input().split()))

		for j in range(0,n):

			if(isPrime(l[j])==True):
				v.append(j+1)

		if len(v) == 0:
			v.append(-1)

		f.append(v[0])
		f.append(v[len(v)-1])
		r.append(f)




for q in range(0,t):
	if(r[q][0]==-1):
		print(r[q][0])
	else :
		print(r[q][0],r[q][1])


