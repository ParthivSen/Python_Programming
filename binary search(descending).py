a=eval(input('enter a list: '))
a.sort(reverse=True)
n=len(a)
p=0
l=0
u=n
s=int(input('enter no. to searched: '))
print('list after sort: ',a)
while l<=u:
    m=(l+u)//2
    if a[m]==s:
        p=m+1
        print('found at:',p)
        break
    elif a[m]<s:
        u=m
    else:
        l=m
