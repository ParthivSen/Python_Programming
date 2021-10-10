def rev(s,n):
    if n>0:
        k=len(s)-n
        rev(s,n-1)
        print(s[k],end='')
    elif n==0:
        return
        
#__main__
s=str(input('enter a string: '))
rev(s,len(s))
