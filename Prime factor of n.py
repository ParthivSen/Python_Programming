n=int(input('enter a no. '))
i=2
while(i<=n):
    if n%i==0:
        print(i)
        n=n/i
        i=i-1
    i=i+1
