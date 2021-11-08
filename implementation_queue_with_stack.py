# ================================================ implementation stack class ====================================
# implement a queue by the stack structure 

class stack:
    def __init__(self):
        self.__list= []
        self.__top= -1


    @property
    def stack(self):
        # O(1)
        return self.__list


    @stack.setter
    def stack(self, vacentString):
        # O(1)
        self.__list.append(vacentString)


    def push(self, item):
        # O(1)
        self.stack= ''
        self.__top += 1
        last= len(self.__list) - 1
        self.__list[last]= item # inserts a item to top of stack


    def pop(self):
        # big O: O(1)
        if self.isEmpty():
            return "stack is empty"
        
        self.__top += (-1)
        delTop= self.__list.pop()
        return delTop
    

    def isEmpty(self):
        # O(1)
        return self.__list == []


class Queue:
    def __init__(self):
        self.__valueStack= stack()
        self.__queueStack= stack()

    
    def enQueue(self, item):
        # big O: O(1)
        self.__valueStack.push(item)


    def deQueue(self):
        # big O: O(1)
        self.__reverse()
        frontQueue= self.__queueStack.pop()
        return frontQueue
        

    def __reverse(self):
        for i in range(len(self.__valueStack._stack__list) - 1, -1, -1):
            self.__queueStack.push(self.__valueStack.pop())


# ================================================ create some objects ====================================


obj= Queue()

obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(30)
obj.enQueue(40)

print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
