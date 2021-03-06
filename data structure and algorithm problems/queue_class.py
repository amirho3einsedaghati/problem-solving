# ======================================================== Implementation queue ===========================================
# implement a queue by an dynamic array


class Queue:
    def __init__(self):
        self.__list= []
        self.__end= -1 # self.__end points to the end of the queue 
        self.__start= -1 # self.__start points to the front of the queue 


    @property
    def queue(self):
        return self.__list


    @queue.setter
    def queue(self, val):
        self.__list.append(val)


    def add(self, item): # add method is like enqueue that adds an item to the end of the queue
        # big O: O(1)
        self.queue= ""
        self.__end += 1
        self.__list[self.__end]= item


    def remove(self): # remove method is like dequeue that deletes an item from the front of the queue and returns the value of it
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


    def reverse(self): # reverses the items of queue, and returns the reversed queue for us
        # big O: O(n)
        li= []
        for i in range(len(self.__list) - 1, -1, -1):
            li.append(self.__list[i])
        
        self.__list= li
        return self.__list

    
# ======================================================== Create some objects ===========================================


obj= Queue()

obj.add(10)
obj.add(20)
obj.add(30)

print(obj.queue)
print(obj.reverse())

print('=============')
print(obj.peek())
print(obj.remove())
print(obj.queue)

print('=============')
print(obj.peek())
print(obj.remove())
print(obj.queue)

print('=============')
print(obj.peek())
print(obj.queue)




