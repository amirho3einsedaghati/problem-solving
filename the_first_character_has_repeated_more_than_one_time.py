# ========================================== the first character that has repeated more than one time ================================
# problem: create a program that can return the first character that has repeated more than one time.

# solution 1: using with class statement
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


    def firstCharMoreRepeatOne(self):
        argList= self.__stringConvertor()
        charsSet= self.__charsSet

        for item in argList:
            charsSet.add(item)

        setList= self.__setConvertor(charsSet)
        
        for item in charsSet:
            argList.remove(item)

        firstItem= argList[0]
        firstItemIndex= self.__targetItem(setList, firstItem)

        return setList[firstItemIndex]


# ========================================================== create some objects ============================================
obj1= main("the green apple")
print(obj1.firstCharMoreRepeatOne())

obj2= main("Just Judge")
print(obj2.firstCharMoreRepeatOne())

obj3= main("Just judgement")
print(obj3.firstCharMoreRepeatOne())