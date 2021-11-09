# ================================================ implementation priority queue ====================================
# implement a priority queue with array

from typing import Iterable


class priorityQueue:
    def __init__(self, arrayCapacity):
        self.__list= [0] * arrayCapacity
        self.__countter= 0
        # self.__start= -1
        # self.__end= -1


    @property
    def Queue(self):
        return self.__list


    @Queue.setter
    def Queue(self, val: Iterable[str]):
        for i in range(0, len(val)):
            self.__list.append(val[i])
        
        for item in self.__list:
            if item == 0:
                self.__list.remove(item)
            
            break
        
        sorted= self.__sortpriorityQueue(self.__list)
        self.__list= sorted


    def __sortpriorityQueue(self, li: list):
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


    def __displacement_items(self, l: list):
        # lis= l
        # length= len(lis)
        # for i in range(length - 1, -1, -1):
        #     if lis[i] < lis[i - 1]:
        #         copy= lis[i - 1]
        #         lis[i - 1]= lis[i]
        #         lis[i]= copy

        # return lis

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


    def add(self, item):
        li= []
        while True:
            if li == []:
                li.append(item)
                break

            if li != [] and li[self.__countter - 1] >= item: #  and li[self.__countter - 1] > item
                li.append(item)
                break
             
            else:
                break
        
        self.__countter += 1
        self.Queue= li

        
# ================================================ create some objects ====================================


obj= priorityQueue(5)
obj.add(16)
obj.add(9)
obj.add(15)
obj.add(3)
obj.add(5)
print(obj.Queue)

obj.add(19)
obj.add(3)
print(obj.Queue)

