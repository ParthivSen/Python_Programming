def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 'no. is not prime'
    else:
        return 'no.is prime'
n=int(input('enter a no. '))
print(prime(n))
