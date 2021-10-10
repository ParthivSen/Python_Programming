import random
a=[10,20,30,40]
b=random.randint(1,5)
for i in range(b):
    for j in range(i):
        print(a[j],end=' ')
    print()
