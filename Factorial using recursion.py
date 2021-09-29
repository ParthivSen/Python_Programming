def fact(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
#__main___
n=int(input('enter a no. '))
print('factorial of',n,'is',fact(n))
