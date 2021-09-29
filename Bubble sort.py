#Bubble sort
#for increasing, we use '>' and for decreasing, we use '<'

#Increasing
a=eval(input('enter a list: '))
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]: 
            a[j],a[j+1]=a[j+1],a[j]
print('List after sorting(ascending): ',a)

#Decreasing
a=eval(input('enter a list: '))
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print('List after sorting(descending): ',a)

