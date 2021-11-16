# ========================================== the first character that has repeated more than one time ================================
# problem: create a program that can return the first character that has repeated more than one time.

# best solutions are solution 1 and solution 3


# solution 1: using with set class statement, and we use one loop in this solution
# class main:
#     def __init__(self, string: str):
#         self.__string= string
#         self.__charsSet= set()

#     def __contain(self, item):
#         return self.__charsSet.__contains__(item)

#     def findFirstRepeatedChar(self):
#         for item in self.__string:
#             if self.__contain(item):
#                 return item
            
#             self.__charsSet.add(item)

#         return f"all of the characters are repeated one time in the string of '{self.__string}'"


# ================================ solution 2 ====================
# solution 2: using with set class statement, and we use two loops in this solution
class main:
    def __init__(self, string: str):
        self.__string= string
        self.__charsSet= set()
    

    def __stringConvertor(self):
        argList= list(self.__string)
        return argList


    def __setConvertor(self, set):
        setList= list(set)
        return setList
    

    def __targetItem(self, setList: list, item):
        firstItemIndex= setList.index(item)
        return firstItemIndex


    def findFirstRepeatedChar(self):
        argList= self.__stringConvertor()
        charsSet= self.__charsSet

        for item in argList:
            charsSet.add(item)

        setList= self.__setConvertor(charsSet)
        
        for item in charsSet:
            argList.remove(item)

        try:
            firstItem= argList[0]
            firstItemIndex= self.__targetItem(setList, firstItem)
        except IndexError:
            return f"all of the characters are repeated one time in the string of '{self.__string}'"
        else:
            return setList[firstItemIndex]


# # ========================================================== create some objects ============================================
obj1= main("the green apple")
print(obj1.findFirstRepeatedChar())

obj2= main("Just Judge")
print(obj2.findFirstRepeatedChar())

obj3= main("Just judgement")
print(obj3.findFirstRepeatedChar())

obj4= main("A I")
print(obj4.findFirstRepeatedChar())


# ================================ solution 2 ====================
# solution 2: using with function statement

# def firstCharMoreRepeatOne(string: str):
#     argList= list(string)
#     charsSet= set()

#     for item in argList:
#         charsSet.add(item)

#     setList= list(charsSet)

#     for item in charsSet:
#         argList.remove(item)

#     firstItem= argList[0]
#     firstItemIndex= setList.index(firstItem)

#     return setList[firstItemIndex]

# print(firstCharMoreRepeatOne("the green apple"))
# print(firstCharMoreRepeatOne("Just Judge"))
# print(firstCharMoreRepeatOne("Just judgement"))

