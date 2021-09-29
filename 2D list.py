l=[]
r=int(input('enter no.of rows: '))
c=int(input('enter no.of columns: '))
for i in range(r):
    row=[]
    for j in range(c):
        elem=int(input('Element'+str(i)+','+str(j)+':'))
        row.append(elem)
    l.append(row)
print('list: ')
print('l=[')
for i in range(r):
    print('\t[',end='')
    for j in range(c):
        print(l[i][j],end=' ')
    print(']')
print('  ]')
