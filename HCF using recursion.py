def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
#__main__
a=int(input('enter a no. '))
b=int(input('enter a no. '))
print(hcf(a,b))
