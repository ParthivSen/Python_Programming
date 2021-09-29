a=int(input('enter a no. '))
b=int(input('enter a no. '))
c=a*b
for i in range(1,c+1):
    if i%a==0 and i%b==0:
        lcm=i
        break
print('LCM: ',lcm)
