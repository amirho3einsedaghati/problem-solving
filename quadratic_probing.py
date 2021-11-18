# ========================================== implementation open addressing algorithm,quadratic probing, ================================


class hash:
    def __init__(self, dictSize: int):
        self.__dictionarySize= dictSize
        self.__list= [0] * dictSize


    def __hashFunction(self, key: int|str):
        if type(key) is str:
            arrayIndexKey= key.__hash__() % self.__dictionarySize
            return arrayIndexKey

        elif type(key) is int:
            arrayIndexKey= key % self.__dictionarySize
            return arrayIndexKey

        raise KeyError("the entered key must be an integer key or a string key")


    def __quadraticProbing(self, pair):
        length= len(self.__list)

        for i in range(0, length):
            arrayIndex= (self.__hashFunction(pair[0]) + (i**2)) % length

            if self.__list[arrayIndex] == 0:
                self.__list[arrayIndex]= pair
    '''
    the algorithm doesn't have the drawbacks of the linear probing overally.
    
    the quadratic probing drawback:
    this algorithm not find overally the chance of traversing some of indexes of the array.
    '''


    @property
    def Dict(self):
        try:
            return dict(self.__list)
        except TypeError:
            return self.__list


    @Dict.setter
    def fillDict(self, pair: tuple):
        arrayIndexKey= self.__hashFunction(pair[0])

        if self.__list[arrayIndexKey] == 0:
            self.__list[arrayIndexKey]= pair

        elif type(self.__list[arrayIndexKey]) == tuple:
            self.__quadraticProbing(pair)


# ========================================== create some objects ================================


obj1= hash(5)
obj1.fillDict= (1,"amir")
obj1.fillDict= (2,"reza")
obj1.fillDict= (3,"saman")
obj1.fillDict= (4,"ali")
obj1.fillDict= (12,"zahra")
print(obj1.Dict)


obj2= hash(5)
obj2.fillDict= (1,"amir")
obj2.fillDict= (2,"reza")
obj2.fillDict= (3,"saman")
obj2.fillDict= (4,"ali")
obj2.fillDict= (6,"zahra")
print(obj2.Dict)
