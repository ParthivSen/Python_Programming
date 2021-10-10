s=0
n=int(input('enter a no.: '))
for a in range(2,n+2):
    t=0
    for b in range(1,a):
    	t+=b
    print('Term',a-1,':',t)
    s+=t
print('Sum of',n,'term is',s)
