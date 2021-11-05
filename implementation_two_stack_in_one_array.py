# question: implement two stacks in one array. support these operations:
# push1()
# push2()
# pop1()
# pop2()
# isEmpty1()
# isEmpty2()
# isFull1()
# isFull2()

# answer: we have to create an array that implemented by two stack and is fill by two stack.
# stack 1: it fills array left to right. 
# stack 2: if fills array right to left. 

# ================================================ implementation two stacks in a array class ====================================


class twoStack:
    def __init__(self, stackCapacity):
        self.__list= [0] * stackCapacity
        self.__top1= -1
        self.__top2= stackCapacity

     
    def getlist(self):
        return self.__list
    

    def push1(self, item):
        if self.isFull1(): 
            return "stack is full"

        self.__top1 += 1
        self.__list[self.__top1]= item


    def pop1(self): # to delete from first stack
        if self.isEmpty1(): return "stack is empty"
        
        self.__top1 += -1
        delTop= self.__list.pop()
        return delTop
     

    def isEmpty1(self):
        return self.__top1 == -1 # if a stack be vacant returns True 


    def isFull1(self):
        return self.__top1 + 1 == self.__top2 # if a stack be full returns True


    def push2(self, item):
        if self.isFull2():
            return "stack is full"
        
        self.__top2 += -1
        self.__list[self.__top2]= item


    def pop2(self): # to delete from first stack
        if self.isEmpty2(): return "stack is empty"

        self.__top2 += 1
        top= self.__list.pop()
        return top
    

    def isEmpty2(self):
        return self.__top2 == self.__list.__len__() # if a stack be vacant returns True 


    def isFull2(self):
        return self.__top2 - 1 == self.__top1 # if a stack be full returns True


# ================================================ create some objects ====================================


instance1= twoStack(3)
print(instance1.isEmpty1())
print(instance1.isFull1())
print(instance1.pop1())
instance1.push1(100)
instance1.push1(200)
instance1.push1(300)
print(instance1.getlist())
print(instance1.isEmpty1())
print(instance1.isFull1())
print(instance1.pop1())
print(instance1.getlist())

print('========================')
instance2= twoStack(5)
print(instance2.isEmpty2())
print(instance2.isFull2())
print(instance2.pop2())
instance2.push2(50)
instance2.push2(100)
instance2.push2(150)
instance2.push1(700)
instance2.push1(600)
print(instance2.getlist())
print(instance2.isEmpty2())
print(instance2.isFull2())
print(instance2.pop2())


print('========================')
print(instance1.getlist())
print(instance2.getlist())

