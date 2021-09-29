 def cls():
    print("\n")
def isempty(qu):
    if qu==[]:
        return True
    else:
        return False
def Enqueue(qu,item):
    qu.append(item)
    if len(qu)==1:
        front=rear=0
    else:
        rear=len(qu)-1
def Dequeue(qu):
    if isempty(qu):
        return 'underflow'
    else:
        item=qu.pop()
    if len(qu)==0:
        front=rear=None
    return item
def Peek(qu):
    if isempty(qu):
        return 'underflow'
    else:
        front=0
    return qu[front]
def Display(qu):
    if isempty(qu):
        print('Queue Empty!')
    elif len(qu)==1:
        print(qu[0],'<==front,rear')
    else:
        front=0
        rear=len(qu)-1
        print(qu[front],'<-front')
        for a in range(1,rear):
            print(qu[a])
        print(qu[rear],'<-rear')    
#___Main___
q=[]
front=None
while True:
    cls()
    print("QUEUE OPERATION")
    print('1.Enqueue')
    print('2.Dequeue')
    print('3.Peek')
    print('4.Display Queue')
    print('5.Exit')
    ch=int(input('enter your choice(1-5): '))
    if ch==1:
        item=int(input('enter item: '))
        Enqueue(q,item)
        input('Please enter to continue...')
    elif ch==2:
        item=Dequeue(q)
        if item=='underflow':
            print('underflow! Queue is empty')
        else:
            print('Dequeued item is',item)
        input('Please enter to continue...')
    elif ch==3:
        item=Peek(q)
        if item=='Underflow':
            print('Underflow! Queue is empty')
        else:
            print('Frontmost item is',item)
        input('Please enter to continue...')
    elif ch==4:
        Display(q)
        input('Please enter to continue...')
    elif ch==5:
        break
    else:
        print('Invalid Choice')
        input('Please enter to continue...')

        
