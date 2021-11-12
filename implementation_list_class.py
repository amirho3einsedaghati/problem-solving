# ================================================ implementation array class( or list class in python ) ====================================
from typing import Iterable

class array:
    def __init__(self):
        self.__args_list= [] 
        self.__list= []
        self.__intersection= [] 


    def __resize(self, item): # this is a private method 
        # big O: O(1)
        __resizedList= [""]
        if type(item) == int:
            size= self.len(self.__args_list)
            size += 1 
            __resizedList *= size
            return __resizedList
        elif type(item) == list or type(item) == str or type(item) == tuple:
            itemSize= len(item)
            size= self.len(self.__args_list)
            size += itemSize
            __resizedList *= size
            return __resizedList


    def len(self, iter): # we suppose this method is a private method 
        # big O: O(1)
        return len(iter)


    def append(self, item):
        # big O: O(n)
        res= self.__resize(item)
        for i in range(0, len(res)):
            if i < len(res) - 1:
                res[i] = self.__args_list[i]
            elif i == len(res) - 1:
                res[i]= item
        self.__args_list= res


    def extend(self,__Iterable: Iterable[int]):
        # big O: O(n)
        res= self.__resize(__Iterable)
        index= 0
        for i in range(0, len(res)):
            if i < self.len(self.__args_list):
                res[i] = self.__args_list[i]
            elif self.len(self.__args_list) <= i <= len(res) -1:
                res[i]= __Iterable[index]
                index += 1
        self.__args_list= res


    def insert(self, index: int, item:object):
        # big O: O(n)
        self.append(item) # we are working on such a example list: self.__args_list= [1,2,3,4,5,""]

        if index >= self.len(self.__args_list):
            print(f"the index is out of range, the index must be between 0 and {self.len(self.__args_list) - 1}")

        elif 0 <= index < self.len(self.__args_list):
            for i in range(self.len(self.__args_list)-1, index, -1):
                if index <= self.len(self.__args_list) - 2: # if the user has seen this [1,2,3,4,5] and want to add an item to the last index or previous index, the below commands are run.
                    copy= self.__args_list[i - 1]
                    self.__args_list[i - 1]= self.__args_list[i]
                    self.__args_list[i]= copy
                    if self.__args_list[index] == "":
                        # print(self.__args_list.index([index + 1])
                        # copy= self.__args_list[index + 1]
                        self.__args_list[index]= item
                        # self.__args_list[index]= copy
                elif index == self.len(self.__args_list) - 1: # if the user has seen this [1,2,3,4,5] and want to add an item to the self.len(self.__args_list), the below commands are run.
                    self.__args_list[index]= item


    def pop(self, index: int): #Remove and return item at index
        # big O: O(n) 
        li= []
        if index > len(self.__args_list) - 1:
            print(f"the index must be: index <= {self.len(self.__args_list)}, please enter another index")

        for i in range(0,len(self.__args_list)):
            if i != index:
                li.append(self.__args_list[i])
        self.__args_list= li


    def remove(self, value):
        # big O: O(n)
        indexVal= self.index(value)
        if type(indexVal) == str:
            print(f"the value of {value} is not in the list")
        else:
            self.__args_list.pop(indexVal)


    def reverse(self): # reverse the main list (self.__args_list)
        # big O: O(n)
        # solution 1:
        # with use of []
        self.__args_list= self.__args_list[::-1]


        # solution 2:
        # without use of .appned()
        # n= self.len(self.__args_list)
        # past index= 0   1   2   3   4
        # past index == new index
        # new index= n-5  n-4 n-3 n-2 n-1    
        #            [1 , 2 , 3 , 4 , 5]    ->  reversed:[5 , 4 , 3 , 2 , 1] 
        # how to reach the 'reversed' ingredients?
        # if we want to reach the second item of 'self.__args_list' at 'reversed' list:  past index: 1    ,   new index: n - 4  => answer: new index= n - (i + 1)

        # items= [""]
        # count= self.len(self.__args_list)
        # items *= count
        # for i in range(0,count): 
        #     reversed= self.__args_list[count - i - 1]
        #     items[i]= reversed

        # self.__args_list= items


    def index(self,value):
        # big O: O(n)
        if value in self.__args_list:
            len= self.len(self.__args_list) 
            for i in range(0,len):
               if self.__args_list[i] is value:
                    return i
        else:
            return f"{value} is not in list, please enter another value"


    def max(self): #Return maximum
        # big O: O(n)
        # solution 1:
        # in this solution we used while loop and considered max= 0
        index=0
        while index < self.len(self.__args_list):
            max= 0
            if max < self.__args_list[index]:
                max= self.__args_list[index]
            index += 1
        return max

        # solution 2:
        # in this solution we used for loop and considered max= self.__args_list[0]
        # max= self.__args_list[0]
        # for i in range(0,self.len(self.__args_list)):
        #     if self.__args_list[i] > max:
        #         max= self.__args_list[i]
        # return max

        # solution 3:
        # in this solution we used for loop and considered max= 0
        # max= 0
        # for i in range(0,self.len(self.__args_list)):
        #     if max < self.__args_list[i]:
        #         max= self.__args_list[i]
        # return max
    

    def min(self):
        min= self.__args_list[0]
        for i in range(0,len(self.__args_list)):
            if self.__args_list[i] < min:
                min= self.__args_list[i]
        return f"max: {min}"


    def append_or_extend_to_list(self, item):
        if type(item) == str or type(item) == list or type(item) == tuple:
            self.extend(item)
        else:
            self.append(item)  

   
# Implementation Intersect method in the list class 
    # solution 1:   
    # big O(n) 
    def intersection_points(self,li: list):
        for item in self.__args_list:
            if item in li:
                self.__intersection.append(item)
        return f"intersection array with list: {self.__intersection}"


    # solution 2:
    # big O(n^2)
    # def intersection_points(self):
    #     # solution 1:
    #     # in this solution we used list comprehension
    #     [[self.__intersection.append(item) for value in self.__list if item == value] for item in self.__args_list]
    #     return f"intersection array with list: {self.__intersection}"

        # solution 2:
        # in this solution we used nested for
        # for item in self.__args_list:
        #     for value in self.__list:
        #         if item == value:
        #             self.__intersection.append(item)
        # return f"intersection array with list: {self.__intersection}"


    def show_list(self):
        # big O: O(1)
        print(self.__args_list)


# ============================================================== create some instances  =====================================       


instance= array()
instance.append(10)
instance.append(20)
instance.append(30)
instance.append(40)
instance.append(50)
instance.extend([60,70,80,90,120])
instance.show_list()

# instance.reverse()
# instance.show_list()

# # # print("=====================")
# instance.pop(0)
# instance.pop(50) 
# instance.show_list()
# # # print(instance.index(20))
# # # print(instance.index(200)

# # # # print("=====================")
# # # # instance.show_list()
# print(instance.max())

# instance.append_or_extend_to_list([20,12,34,10,50,28])
# instance.append_or_extend_to_list(100)
# instance.show_list()

# print(instance.intersection_points([20,12,34,10,50,28]))

instance.insert(7,7)
instance.show_list()

# instance.insert(12,77)
# instance.show_list()

# instance.insert(0,88)
# instance.show_list()

# instance.insert(7,24)
# instance.show_list()

# # print(instance.max())

# instance.remove(1000)
# instance.show_list()

# instance.remove(1000)
# instance.show_list()

# instance.remove(7)
# instance.show_list()
