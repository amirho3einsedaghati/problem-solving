# ============================================================== counting the characters of the string =========================================
# problem: create a program that contains an algorithm for returning the first Non-repetitive characters and an algorithm for returning mod.


class main:
    def __init__(self, args= [str]):
        self.__args= args


    def __unpackStringFromList(self):
        string= self.__args[0]
        return string


    def __createDictWithArgs(self):
        string= self.__unpackStringFromList()
        dictionary= dict()

        for i in range(0, len(string)):
            dictionary.update({i: string[i]})

        return dictionary


    def __convertDictItmes(self):
        dictionary= self.__createDictWithArgs()
        dictItems= list(dictionary.items())
        return dictItems


    def __convertDictVal(self, dictVal):
        dictVal= list(dictVal)
        return dictVal


    def __countCharacters(self):
        string= self.__unpackStringFromList()
        dictionary= self.__createDictWithArgs()
        listItems= self.__convertDictItmes()

        dictVal= dictionary.values()
        dictVal= self.__convertDictVal(dictVal)
        lenght= len(dictVal)
        countEachCharList= [0] * lenght

        for i in range(0, len(listItems)):
            if listItems[i][1] == string[i]:
                popVal= dictionary.pop(listItems[i][0])
                popValIndex= dictVal.index(popVal)
                countEachCharList[popValIndex] += 1

        return countEachCharList


    def firstNonRepetitiveChar(self):
        dictionary= self.__createDictWithArgs()
        dictVal= dictionary.values()
        dictVal= self.__convertDictVal(dictVal)
        countChars= self.__countCharacters()
        
        for i in range(0, len(countChars)):
            if countChars[i] == 1:
                return f"the first Non-repetitive characters: {dictVal[i]}"


    def mod(self):
        # if we want to show the all of the mods, we should using this solution:
        dictionary= self.__createDictWithArgs()
        dictVal= dictionary.values()
        dictVal= self.__convertDictVal(dictVal)
        countChars= self.__countCharacters()


        li= [0]
        for item in countChars:
            if li[0] < item:
                li.clear()
                li.append(item)
            elif li[0] == item:
                li.append(item)
        
        modList= []
        if li[0] is not 1:
            for item in li:
                index= countChars.index(item)
                modList.append(dictVal[index])
                dictVal.pop(index)

            for item in modList:
                if item == modList[0]:
                    print(f"the mode of this {self.__args[0]} is :", end="\t")
                    
                if item == modList[len(modList) - 1]:
                    print(f"{item}", end=" ")

                else:
                    print(f"{item}", end="|")
            
            print("\n")

        else:
            print("all of the character have repeated just one time")


        # if we want to show,the first value of the mod, we should using the following solution:
        # maximum=max(countChars)
        # indexMax= countChars.index(maximum)
        # return f"mode '{self.__args[0]}': {dictVal[indexMax]}"



# ============================================================== create some objects =========================================


obj1= main(["A Green Apple"])
print(obj1.firstNonRepetitiveChar())
obj1.mod()

print('------------------')
obj2= main(["The Just Judge"])
print(obj2.firstNonRepetitiveChar())
obj2.mod()

print('------------------')
obj3= main(["A Just Judgement"])
print(obj3.firstNonRepetitiveChar())
obj3.mod()

print('------------------')
obj4= main(["A J"])
print(obj4.firstNonRepetitiveChar())
obj4.mod()