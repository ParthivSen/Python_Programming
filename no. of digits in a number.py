a=int(input('enter a no. '))
s=0
while a>0:
    d=a%10
    a=a//10
    b=len(str(d))
    s=s+b
print('no. of digits in  the number',s)
