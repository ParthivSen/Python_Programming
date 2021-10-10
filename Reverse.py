a=eval(input('enter a list: '))
n=len(a)
if (n%2==0):
    for i in range(0,n//2):
        a[i],a[n//2+i]=a[n//2+i],a[i]
    print('after swap:',a)
else:
    for i in range(0,n//2):
        a[i],a[n//2+i+1]=a[n//2+i+1],a[i]
    print('after swap:',a)
