n=int(input('enter a no.: '))
a=0
b=1
print(a,b)
for i in range(1,n+1):
	c=a+b
	a,b=b,c
	print(c,end=' ')
