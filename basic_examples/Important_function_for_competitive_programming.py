def isLeap(year):
  if year%4==0 or (year%400==0 and year%100!=0):
    return True
  return False

def primeList(r):
    #seive method/algorithm
    prime=[True]*(r+1)
    prime[1]=False
    prime[0]=False
    for i in range(2,int(r**0.5)+1):
        if prime[i]:
            for j in range(2*i,r+1,i):
                prime[j]=False
    return prime

def isPrime(n):
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    i=2
    while(i*i <= n):
        if n%i==0:
            return False
        i+=1
    return True

def binarySearch(llist,value,low,high):
    if low>high:
        return False
    mid=(low+high)//2
    if llist[mid]==value:
        return True
    if llist[mid]>value:
        return binarySearch(llist,value,low,mid-1)
    else:
        return binarySearch(llist,value,mid+1,high)
    
def pascalTriangle(max_n):
    #This pascaltriangle is a dynamic approch of finding nCr
    pascals =[[0 for i in range(max_n+1)] for j in range(max_n+1)]
    pascals[0][0]=1
    for i in range(1,len(pascals)):
        pascals[i][0]=1
        for j in range(1,i+1):
            pascals[i][j] = (pascals[i-1][j-1] + pascals[i-1][j])
    return pascals


#mulInv(x) is multiplicative inverse of x under modulo 1000000007. 
def mulInverse(x):
    prime=10**9+7
    return pow(x,prime-2,prime)

#(p*mulInv(q)) modulo 1000000007
def mult(a,b):
    # Here p is a  and b is mulInv of q
    prime=10**9+7
    ans = (a%prime * b%prime)%prime
    return ans
    
