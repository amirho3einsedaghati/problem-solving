# ================================================ stack with two queues ====================================
# problem: implement a stack using two queues, the stack contains push, pop, peek and size methods.


class Queue:
    def __init__(self):
        self.__list= []
        self.__end= -1 # self.__end points to the end of the queue 
        self.__start= -1 # self.__start points to the front of the queue 


    def __reset_list_end(self):
        self.__list= []
        self.__end= -1


    def __reset_start(self):
        self.__start= -1


    @property
    def queue(self):
        return self.__list


    @queue.setter
    def queue(self, val):
        self.__list.append(val)


    def enQueue(self, item): # the method adds an item to the end of the queue
        # big O: O(1)
        self.queue= ""
        self.__end += 1
        self.__list[self.__end]= item


    def deQueue(self): # the method deletes an item from the front of the queue and returns the value of it
        # big O: O(1)
        if self.isEmpty():
            return "queue is empty"

        self.__start += 1
        frontQueue= self.__list.pop(self.__start)
        self.__start= -1
        return frontQueue


    def peek(self): # returns the value of an item from the front of the queue 
        # big O: O(1)
        if self.isEmpty():
            return "queue is empty"

        self.__start += 1
        front= self.__list[self.__start]
        self.__start= -1
        return front


    def isEmpty(self): # checks queue is empty or not 
        # big O: O(1)
        return self.__list == []


class Stack:
    def __init__(self):
        self.__queue1= Queue()
        self.__queue2= Queue()


    def getStack(self):
        return self.__queue1._Queue__list


    def push(self, item):
        # big O: O(1)
        self.__queue1.enQueue(item)


    def pop(self):
        # big O: O(n)
        for i in range(len(self.__queue1._Queue__list) - 1, -1, -1):
            self.__queue2.enQueue(self.__queue1._Queue__list[i])

        top_of_stack= self.__queue2.deQueue()

        self.__queue1._Queue__reset_list_end()
        for i in range(len(self.__queue2._Queue__list) - 1, -1, -1):
            self.__queue1.enQueue(self.__queue2._Queue__list[i])

        return top_of_stack
  

    def peek(self):
        # big O: O(n)
        self.__queue2._Queue__reset_list_end()
        for i in range(len(self.__queue1._Queue__list) - 1, -1, -1):
            self.__queue2.enQueue(self.__queue1._Queue__list[i]) 

        self.__queue2._Queue__reset_start()
        return self.__queue2.peek()

    
    def size(self):
        # big O: O(n)
        length= 0
        for item in self.__queue1._Queue__list:
            length += 1

        return length


# ================================================ create some objects ====================================

    
obj= Stack()
print(obj.pop())
print(obj.peek())

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(obj.getStack())
print(obj.size())

print(obj.pop())
print(obj.getStack())

print(obj.peek())
print(obj.getStack())
print(obj.size())