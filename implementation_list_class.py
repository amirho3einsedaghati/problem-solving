# ================================================ implementation array class( or list class in python ) ====================================
from typing import Iterable

class array:
    def __init__(self):
        self._args_list= [] 
        self._list= []
        self._intersection= [] 


    def append(self, item): #Append the item to the end of the list.
        self._args_list= self._args_list.__add__([0])
        self._args_list[len(self._args_list)-1] = item


    def extend(self,__Iterable: Iterable[int]): #Extend list by appending elements from the iterable and add elements to the end of the list 
        for item in __Iterable:
            self._args_list= self._args_list.__add__([0])
            self._args_list[len(self._args_list) - 1]= item


    def insert(self, index: int, item:object): #Add item to the recieved index
        if 0 <= index < len(self._args_list):
            for i in range(len(self._args_list)-1, index-1, -1):
                if i == len(self._args_list) - 1:
                    copy= self._args_list[i]
                    self._args_list[i]= 0
                    self._args_list= self._args_list.__add__([copy])
                    self._args_list[i]= item
                elif i != len(self._args_list) - 1:
                    copy= self._args_list[i]
                    self._args_list[i]= 0
                    self._args_list[i + 1]= copy
                    if self._args_list[index] == 0:
                        self._args_list[index]= item
        elif index == len(self._args_list):
            self._args_list= self._args_list.__add__([0])
            self._args_list[index]= item


    def pop(self, index: int): #Remove and return item at index 
        try:
            deleted_of_list= self._args_list[index]
            self._args_list.__delitem__(index)
        except IndexError:
            print(f"the index must be: index < {len(self._args_list)}, please enter another index")
        else:
            return deleted_of_list


    def reverse(self): # reverse the main list (self._args_list)
        # solution 1:
        self._args_list= self._args_list[::-1]

        # solution 2:
        # items= []
        # for i in range(len(self._args_list)-1, -1, -1):
        #     items.append(self._args_list[i]) 
        # self._args_list= items

        # solution 3:
        # n= len(self._args_list)
        # past index= 0   1   2   3   4
        # past index == new index
        # new index= n-5  n-4 n-3 n-2 n-1    
        #            [1 , 2 , 3 , 4 , 5]    ->  reversed:[5 , 4 , 3 , 2 , 1] 
        # how to reach the 'reversed' ingredients?
        # if we want to reach the second item of 'self._args_list' at 'reversed' list:  past index: 1    ,   new index: n - 4  => answer: new index= n - (i + 1)

        # items= []
        # count= len(self._args_list)
        # for i in range(0,count):
        #     reversed= self._args_list[count - i - 1]
        #     items.append(reversed)

        # self._args_list= items

    def index(self,value): #Return first index of value.
        if value in self._args_list:
            lenght= len(self._args_list) 
            for i in range(0,lenght):
               if self._args_list[i] is value:
                    return f"index of the received value: {i}"
        else:
            print(f"{value} is not in list, please enter another index")


    def max(self): #Return maximum
        # solution 1:
        # in this solution we used for loop and considered max= 0
        index=0
        while index < len(self._args_list):
            max= 0
            if max < self._args_list[index]:
                max= self._args_list[index]
            index += 1
        return max

        # solution 2:
        # in this solution we used for loop and considered max= self._args_list[0]
        # max= self._args_list[0]
        # for i in range(0,len(self._args_list)):
        #     if self._args_list[i] > max:
        #         max= self._args_list[i]
        # return max

        # solution 3:
        # in this solution we used while loop and considered max= 0
        # index=0
        # while index < len(self._args_list):
        #     max= 0
        #     if max < self._args_list[index]:
        #         max= self._args_list[index]
        #     index += 1
        # return max


# ============================================= Implementation Intersect method in list class ==========================================    
# solution 1:   
# big O(n) 

    def intersection_points(self,li: list):
        for item in self._args_list:
            if item in li:
                self._intersection.append(item)
        return f"intersection array with list: {self._intersection}"

# ----------------------
# solution 2:
# big O(n^2)

    def append_or_extend_to_list(self, item):
        if type(item) == str or type(item) == list or type(item) == tuple:
            for value in item:
                self._list= self._list.__add__([0])
                self._list[len(self._list) - 1]= value
        else:
            self._list= self._list.__add__([0])
            self._list[len(self._list)-1] = item

    # def intersection_points(self):
    #     # solution 1:
    #     # in this solution we used list comprehension
    #     [[self._intersection.append(item) for value in self._list if item == value] for item in self._args_list]
    #     return f"intersection array with list: {self._intersection}"

        # solution 2:
        # in this solution we used nested for
        # for item in self._args_list:
        #     for value in self._list:
        #         if item == value:
        #             self._intersection.append(item)
        # return f"intersection array with list: {self._intersection}"

# ========================================   

    def show_array(self):
        print(self._args_list)
        # for item in self._args_list:
        #     print(item)


    def show_list(self):
        print(self._list)
      
# ============================================================== excercise with create instance =====================================       

instance= array()
instance.append(10)
instance.append(20)
instance.append(30)
instance.append(40)
instance.append(50)
# # # instance.extend([60,70,80,90,120,"a"])
instance.show_array()
instance.reverse()
instance.show_array()

# # print("=====================")
# instance.pop(50)
x=instance.pop(1) # akharin item ro hazf mikonad
# print(x)
instance.show_array()
# # instance.index(20)
# # instance.index(200)

# # # print("=====================")
# # # instance.show_array()
# # # print(instance.max())
# # instance.append_or_extend_to_list([20,12,34,10,50,28])
# # instance.append_or_extend_to_list(100)
# # # instance.show_array()
# # instance.show_list()
# # print(instance.intersection_points())

print(instance.intersection_points([20,12,34,10,50,28]))

instance.insert(0,7)
instance.show_array()

instance.insert(4,77)
instance.show_array()

instance.insert(6,88)
instance.show_array()

instance.insert(8,24)
instance.show_array()

# print(instance.max())
