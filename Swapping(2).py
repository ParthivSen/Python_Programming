#[2,7,8,1,4,6]=>[7,2,1,8,6,4]
a=eval(input('enter a list: '))
n=len(a)
for i in range(0,n,2):
    a[i],a[i+1]=a[i+1],a[i]
print('after swap ',a)    
