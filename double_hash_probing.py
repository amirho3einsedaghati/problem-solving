# ========================================== implementation open addressing algorithm,3. double hash probing, ================================


class hash:
    def __init__(self, dictSize: int):
        self.__dictionarySize= dictSize
        self.__list= [0] * dictSize


    def __hashFunction1(self, key: int|str):
        if type(key) is str:
            arrayIndexKey= key.__hash__() % self.__dictionarySize
            return arrayIndexKey

        elif type(key) is int:
            arrayIndexKey= key % self.__dictionarySize
            return arrayIndexKey

        raise KeyError("the entered key must be an integer key or a string key")


    def __hashFunciton2(self, key: int):
        tableSize= self.__dictionarySize

        arrayIndexKey= (tableSize - 2) - (key % (tableSize - 2))
        return arrayIndexKey


    def __doubleHashProbing(self, pair):
        tableSize= len(self.__list)

        for i in range(0, tableSize):
            arrayIndex= (self.__hashFunction1(pair[0]) + (i * self.__hashFunciton2(pair[0]))) % tableSize

            if self.__list[arrayIndex] == 0:
                self.__list[arrayIndex]= pair
                break
    '''
    the algorithm doesn't have the drawbacks of the linear probing and quadratic probing algorithms .
    '''


    @property
    def Dict(self):
        try:
            return dict(self.__list)
        except TypeError:
            return self.__list


    @Dict.setter
    def fillDict(self, pair: tuple):
        arrayIndexKey= self.__hashFunction1(pair[0])

        if self.__list[arrayIndexKey] == 0:
            self.__list[arrayIndexKey]= pair

        elif type(self.__list[arrayIndexKey]) == tuple:
            self.__doubleHashProbing(pair)


# ========================================== create some objects ================================


obj1= hash(5)
obj1.fillDict= (6,"amir")
obj1.fillDict= (8,"reza")
obj1.fillDict= (11,"saman")
obj1.fillDict= (4,"ali")
obj1.fillDict= (12,"zahra")
print(obj1.Dict)


obj2= hash(5)
obj2.fillDict= (0,"amir")
obj2.fillDict= (2,"reza")
obj2.fillDict= (3,"saman")
obj2.fillDict= (4,"ali")
obj2.fillDict= (6,"zahra")
print(obj2.Dict)
