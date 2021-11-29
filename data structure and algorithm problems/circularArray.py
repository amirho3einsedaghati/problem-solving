# ======================================================== Implementation Circular Array ===========================================
# how to implement an circular array:


class circularArray:
    def __init__(self, arrayCapacity):
        self.__lis= [0] * arrayCapacity # this is an static array 
        self.__i= -1 # this is the array pointer 


    def getCircularArray(self):
        return self.__lis


    def add(self, item): # adds an item to array 
        self.__i += 1
        length= len(self.__lis)

        if self.__i <= length - 1:
            self.__lis[self.__i]= item
        
        fromLeft= self.__i % length # if we suppose length= 5 (ex: 5 -> fromLeft=0)   why?!  remaining 5 / 5 is 0 so the value of our variable is 0
        self.__lis[fromLeft]= item


# ======================================================== Create Some Objects ===========================================


obj= circularArray(5)
obj.add(10)
obj.add(20)
obj.add(30)
obj.add(40)
obj.add(50)

print(obj.getCircularArray())

obj.add(60)
obj.add(70)

print(obj.getCircularArray())

