import bisect
l=eval(input('enter a list: '))
i=int(input('enter a no. to be inserted: '))
iin=bisect.bisect(l,i)
bisect.insort(l,i)
print('no. to be inserted at:',iin)
print('list after insertion')
print(l)
