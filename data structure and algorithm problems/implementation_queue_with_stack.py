# ================================================ implementation queue with stack ====================================
# problem: implement a queue by the stack structure that covers followig method:
# enqueue(), dequeue()


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


class stackQueue:
    def __init__(self):
        self.__valueStack= stack() # it's just for the enqueue method
        self.__queueStack= stack() # it's just for dequeue method
        

    def getEnqueue(self):
        return self.__valueStack._stack__list


    def getDequeue(self):
        return self.__queueStack._stack__list


    def enQueue(self, item):
        # big O: O(1)
        self.__valueStack.push(item)
        # print(f"{self.__valueStack._stack__list}")


    def deQueue(self):
        # big O: O(n)
        self.__reverse()
        frontQueue= self.__queueStack.pop()
        return frontQueue
        

    def __reverse(self):
        while not self.__valueStack.isEmpty():
            self.__queueStack.push(self.__valueStack.pop())


# ================================================ create some objects ====================================


obj= stackQueue()

obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(30)
obj.enQueue(40)
print(obj.getEnqueue())

print('====== delete of the item of the front of the queue ======')
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
print(obj.getDequeue())

obj.enQueue(50)
obj.enQueue(60)
obj.enQueue(70)
print(obj.getEnqueue())

print('====== delete of the item of the front of the queue ======')
print(obj.deQueue())
print(obj.deQueue())
print(obj.getDequeue())


