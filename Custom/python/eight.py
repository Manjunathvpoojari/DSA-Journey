# Using sieve approach for prime 

def sieve(n):
    prime=[True]*(n+1)
    prime[0]=prime[1]=False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1,i):
                prime[j]=False 
    return prime

def twin_pair(m):
    prime =sieve(m)
    pairs=[]
    for i in range(2,m-1):
        if prime[i] and prime[i+2]:
            pairs.append((i, i+2))
    return pairs

print(f"Twin pairs up to 50: {twin_pair(50)}")


def goldbach(n): 
    prime=sieve(n)          
    for p in range(2, n//2 + 1):
        if prime[p] and prime[n-p]:
            return (p, n-p)

print(f"Goldbach pairs for 28: {goldbach(28)}")
