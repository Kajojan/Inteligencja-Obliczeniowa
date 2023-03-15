def prime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True



print(prime(4))

def select_primes(x):
    a=[]
    for i in x:
        if( prime(i)):
            a.append(i)
    return a

print(select_primes([3, 6, 11, 25, 19]))  

