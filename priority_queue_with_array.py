# ================================================ implementation priority queue ====================================
# implement a priority queue with array

from typing import Iterable


class PriorityQueue:
    def __init__(self, arrayCapacity):
        self.__list= [0] * arrayCapacity
        self.__countter= 0
        self.__front= -1


    @property
    def priorityQueue(self):
        return self.__list


    @priorityQueue.setter
    def priorityQueue(self, val: Iterable[str]): 
    # big O: O(n)
    # this method by adding each item to a static array and shifting the each item to the left, can change the size and turn the static attribute of objects to a dynamic attribute.
        for i in range(0, len(val)):
            self.__list.append(val[i])
        
        for item in self.__list:
            if item == 0:
                self.__list.remove(item)
            
            break
        
        sorted= self.__sortpriorityQueue(self.__list)
        self.__list= sorted


    def __sortpriorityQueue(self, li: list):
        # this method first gets the created queue, and then sorts the items of the queue from small to large.
        # big O: O(n)
        lis= []
        min= li[0]
        lis.append(min)

        i= 1
        while i < len(li):
            if li[i] <= min:
                min= li[i]
                lis.insert(i - i, min)
                i += 1
            else:
                lis.append(li[i])
                i += 1

        final= self.__displacement_items(lis)
        return final


    def __displacement_items(self, l: list): # checks the items and then if the items weren't in the correct place, changes the place of them.
        # big O: O(1)
        lis= l
        length= len(lis) - 1

        if lis[length] < lis[length - 1]:
            copy= lis[length - 1]
            lis[length - 1]= lis[length]
            lis[length]= copy

        if lis[length - 1] < lis[length - 2]:
            copy= lis[length - 2]
            lis[length - 2]= lis[length - 1]
            lis[length - 1]= copy

        if lis[length - 2] < lis[length - 3]:
            copy= lis[length - 3]
            lis[length - 3]= lis[length - 2]
            lis[length - 2]= copy

        if lis[length - 3] < lis[length - 4]:
            copy= lis[length - 4]
            lis[length - 4]= lis[length - 3]
            lis[length - 3]= copy

        return lis


    def add(self, item): # the method, adds an item to a dynamic array, li.
        # big O: O(n)
        li= []
        while True:
            if li == []:
                li.append(item)
                break

            if li != [] and li[self.__countter - 1] >= item:
                li.append(item)
                break
             
            else:
                break
        
        self.priorityQueue= li
        self.__countter += 1


    def remove(self):
        # big O: O(1)
        if self.isEmpty():
            print("priority queue is empty!")
        
        elif self.__list[0] == 0:
            print("None")

        else:
            self.__front += 1
            small= self.__list.pop(self.__front)
            self.__front= -1
            return  small


    def peek(self):
        # big O: O(1)
        if self.isEmpty():
            print("priority queue is empty!")
        
        elif self.__list[0] == 0:
            print("None")

        else:
            self.__front += 1
            small= self.__list[self.__front]
            self.__front= -1
            return  small


    def isEmpty(self):
        # big O: O(1)
        return self.__list == [] or self.__list[0] == 0


# ================================================ create some objects ====================================


obj= PriorityQueue(5)
print(obj.remove())
print(obj.peek())
obj.add(16)
obj.add(9)
obj.add(15)
obj.add(3)
obj.add(5)
print(obj.priorityQueue)
print(obj.remove())
print(obj.peek())
print(obj.priorityQueue)

obj.add(19)
obj.add(3)
print(obj.priorityQueue)
print(obj.remove())
print(obj.peek())
print(obj.priorityQueue)

