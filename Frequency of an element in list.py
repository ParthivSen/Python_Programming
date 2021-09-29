a=eval(input('enter a list: '))
m=max(a)
for i in range(1,m+1):
    print('frequency of',i,'is: ',a.count(i))
