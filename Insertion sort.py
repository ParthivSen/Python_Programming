#Insertion Sort
#in k_a[j], for increasing we use '<'
#for decreasing we use '>'

#Increasing
a=eval(input('enter a list: '))
n=len(a)
for i in range(1,n):
	k=a[i]
	j=i-1
	while j>=0 and k<a[j]:  
		a[j+1]=a[j]     
		j=j-1
	else:
		a[j+1]=k
print('List after sorting(ascending): ',a)

#Decreasing
a=eval(input('enter a list: '))
n=len(a)
for i in range(1,n):
	k=a[i]
	j=i-1
	while j>=0 and k>a[j]:  
		a[j+1]=a[j]     
		j=j-1
	else:
		a[j+1]=k
print('List after sorting(descending): ',a)
