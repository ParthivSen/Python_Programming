n=int(input('enter a no.: '))
c=n
s=0
while n>0:
    d=n%10
    n=n//10
    s=s*10+d
if c==s:
    print('no. is palindrome')
else:
    print('no. is not palindrome')
