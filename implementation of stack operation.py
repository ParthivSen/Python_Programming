def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isempty(stk):
        return 'underflow'
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if isempty(stk):
        return 'underflow'
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
    if isempty(stk):
        return 'underflow'
    else:
        top=len(stk)-1
        print(stk[top],'<-top')
        for a in range(top-1,-1,-1):
            print(stk[a])
#__Main__
S=[]
top=None
while True:
    print("STACK OPERATION")
    print('1.Push')
    print('2.Pop')
    print('3.Peek')
    print('4.Display Stack')
    print('5.Exit')
    ch=int(input('enter your choice(1-5): '))
    if ch==1:
        item=int(input('enter item: '))
        Push(S,item)
    elif ch==2:
        item=Pop(S)
        if item=='underflow':
            print('underflow! Stack is empty')
        else:
            print('Popped item is',item)
    elif ch==3:
        item=Peek(S)
        if item=='Underflow':
            print('Underflow! Stack is empty')
        else:
            print('topmost item is',item)
    elif ch==4:
        Display(S)
    elif ch==5:
        break
    else:
        print('Invalid Choice')
              
