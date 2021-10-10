#Selection Sort
#for increasing, we use '>' and for decreasing, we use '<'
a=eval(input('enter a list: '))
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:    
            a[i],a[j]=a[j],a[i]
print('ascending',a)            
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]<a[j]:    
            a[i],a[j]=a[j],a[i]
print('descending',a) 
