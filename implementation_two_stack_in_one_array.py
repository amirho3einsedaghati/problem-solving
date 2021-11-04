# question: implement two stacks in one array. support these operations:
# push1()
# push2()
# pop1()
# pop2()
# isEmpty1()
# isEmpty2()
# isFull1()
# isFull2()

# ================================================ implementation two stacks in a array class ====================================


class array:
    def __init__(self):
        self.__list1= list()
        self.__list2= list()
    

    @property
    def stack1(self):
        return self.__list1


    @stack1.setter
    def stack1(self, val):
        self.__list1.append(val)


    @property
    def stack2(self):
        return self.__list2


    @stack2.setter
    def stack2(self, val):
        self.__list2.append(val)


    def push1(self, item):
        self.stack1= ''
        last= len(self.__list1) - 1
        self.__list1[last]= item # inserts a item to top of first stack


    def pop1(self): # to delete from first stack
        if self.isEmpty1(): return "stack is empty"

        li= []
        count= len(self.__list1)
        i= 0
        while i != count - 1:
            li.append(self.__list1[i])
            i += 1

        backup= self.stack1
        self.__list1= li # delete a item from top of the stack 
        return backup[i] # and returns the deleted item from top of the stack
        
    
    def isEmpty1(self):
        return self.__list1 == list() # if a stack be vacant returns True 


    def isFull1(self):
        return self.__list1 != list() # if a stack be full returns True


    def push2(self, item):
        self.stack2= ''
        last= len(self.__list2) - 1
        self.__list2[last]= item # inserts a item to top of first stack


    def pop2(self): # to delete from first stack
        if self.isEmpty2(): return "stack is empty"

        li= []
        count= len(self.__list2)
        i= 0
        while i != count - 1:
            li.append(self.__list2[i])
            i += 1

        backup= self.stack2
        self.__list2= li # delete a item from top of the stack 
        return backup[i] # and returns the deleted item from top of the stack
        
    
    def isEmpty2(self):
        return self.__list2 == [] # if a stack be vacant returns True 


    def isFull2(self):
        return self.__list2 != [] # if a stack be full returns True


# ================================================ create some objects ====================================


instance1= array()
print(instance1.isEmpty1())
print(instance1.isFull1())
print(instance1.pop1())
instance1.push1(100)
instance1.push1(200)
instance1.push1(300)
print(instance1.stack1)
print(instance1.isEmpty1())
print(instance1.isFull1())
print(instance1.pop1())
print(instance1.stack1)

print('========================')
instance2= array()
print(instance2.isEmpty2())
print(instance2.isFull2())
print(instance2.pop2())
instance2.push2(50)
instance2.push2(100)
instance2.push2(150)
print(instance2.stack2)
print(instance2.isEmpty2())
print(instance2.isFull2())
print(instance2.pop2())
print(instance2.stack2)

print('========================')
print(instance1.stack1)
print(instance2.stack2)