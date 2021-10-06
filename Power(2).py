try:
    def Pow(a,b):
        if b==1:
            return a
        if b==0:
            return 1
        else:
            return a*Pow(a,b-1)
except b<0:
    
a=int(input('enter a no.'))
b=int(input('enter a no.'))
print(Pow(a,b))
