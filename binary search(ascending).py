a=eval(input('enter a list: '))
a.sort()
n=len(a)
p=0
l=0
u=n
s=int(input('enter no. to searched: '))
print('list after sort: ',a)
while l<=u:
    m=(l+u)//2
    if a[m]==s:
        x=m+1
        print('found at:',x)
        break
    elif a[m]>s:
        u=m
    elif a[m]<s:
        l=m
    else:
        print('Not Found')
