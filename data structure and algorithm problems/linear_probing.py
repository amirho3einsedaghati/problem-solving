# ========================================== implementation open addressing algorithm,1. linear probing, ================================


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


    def __linearProbing(self, pair):
        length= len(self.__list)

        for i in range(0, length):
            arrayIndex= (self.__hashFunction1(pair[0]) + i) % length

            if self.__list[arrayIndex] == 0:
                self.__list[arrayIndex]= pair
                break
    '''
    the linear probing drawbacks:
    1. this algorithm must be traverse all of the indexes of the array to if it not found an empty index come out.
    2. cluster -> to reach an empty index may need to be traversed a lot of indexes of the array beacause is created a cluster of the full indexes.  
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
            self.__linearProbing(pair)


# ========================================== create some objects ================================


obj= hash(5)
obj.fillDict= (1,"amir")
obj.fillDict= (2,"reza")
obj.fillDict= (3,"saman")
obj.fillDict= (4,"ali")
obj.fillDict= (6,"zahra")

print(obj.Dict)