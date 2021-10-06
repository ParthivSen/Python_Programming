def Pow(a,b):
    if b==0:
        return 1
    else:
        return a*Pow(a,b-1)
a=int(input('enter a no. '))
b=int(input('enter a no. '))
print(Pow(a,b))
