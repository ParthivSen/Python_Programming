def Bin(a,k,l,h):
    if l>h:
        return 'Error 404'
    m=(l+h)//2
    if k==a[m]:
        return m+1
    elif k<a[m]:
        h=m-1
        return Bin(a,k,l,h)
    else:
        l=m+1
        return Bin(a,k,l,h)
#__main__
a=eval(input('enter a asc./dsc. list: '))
i=int(input('enter a no. to be searched: '))
r=Bin(a,i,0,len(a)-1)
a.sort()
print('list after sort: ',a)
print(i,'found at index',r)
