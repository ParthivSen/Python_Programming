a=eval(input('enter a list '))
n=len(a)
p=0
s=int(input('enter no. to seearched: '))
for i in range(n):
    if a[i]==s:
        p=i+1
        print('found at:',p)
if p==0:
    print('not found')
