def findpos(a,i):
    s=len(a)
    if i<a[0]:
        return 0
    else:
        p=-1
        for j in range(s-1):
            if (a[j]<=i and i<a[j+1]):
                p=j+1
                break
        if p==-1 and i<=s-1:
            p=s
        return p
def shift(a,p):
    a.append(None)
    s=len(a)
    i=s-1
    while i>=p:
        a[i]=a[i-1]
        i-=1
#__Main__
m=eval(input('enter a list: '))
m.sort()
i=int(input('enter a no. to be insert '))
p=findpos(m,i)
shift(m,p)
m[p]=i
print('list after inserting',i,'is: ',m)

