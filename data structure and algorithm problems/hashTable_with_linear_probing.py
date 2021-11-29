# ========================================== implementation a hash table with the linear probing  ================================


class HashTableWithLinearProbing:
    def __init__(self, dictSize: int):
        self.__dictionarySize= dictSize
        self.__list= [0] * dictSize
        self.__countter= 0


    def __hashFunction1(self, key):
        return key % self.__dictionarySize


    def __linearProbing(self, pair):
        length= len(self.__list)

        for i in range(0, length):
            arrayIndex= (self.__hashFunction1(pair[0]) + i) % length

            if self.__list[arrayIndex] == 0 and pair not in self.__list:
                self.__list[arrayIndex]= pair
                self.__countter += 1
                break


    def update(self, pair: tuple):
        arrayIndexKey= self.__hashFunction1(pair[0])

        if self.__list[arrayIndexKey] == 0:
            self.__list[arrayIndexKey]= pair
            self.__countter += 1

        elif type(self.__list[arrayIndexKey]) == tuple:
            self.__linearProbing(pair)
 

    def Dict(self):
        try:
            return dict(self.__list)

        except TypeError:
            li= []

            for item in self.__list:
                if item != 0:
                    li.append(item)

            self.__list= li
            return dict(self.__list)


    def __contains__(self, key):
        for tuple in self.__list:

            if tuple[0] == key:
                return True

        return False       


    def getValue(self, key):
        if self.__contains__(key):
            for tuple in self.__list:

                if tuple[0] == key:
                    return f"the value of {key}: {tuple[1]}"

        return f"this {key} is not in the list"


    def pop(self, key):
        if self.__contains__(key):
            for tuple in self.__list:

                if tuple[0] == key:
                    value= tuple[1]
                    self.__list.remove(tuple)
                    self.__countter -= 1
                    return value

        return f"this {key} is not in the list"


    def size(self):
        return self.__countter


# ============================================================ create some objects ==========================================
    

def getTuple(key, value):
    return tuple([key, value])


obj= HashTableWithLinearProbing(7) # in the maximum state can keeps two more non-repetitive items than it can hold; for example if capacityBucket be 7, it can keeps up to 9 items  
obj.update(getTuple(1, "a"))
obj.update(getTuple(22, "b"))
obj.update(getTuple(2, 'd'))
obj.update(getTuple(3, 'e'))
obj.update(getTuple(4, 'e'))
obj.update(getTuple(4, 'e'))
obj.update(getTuple(5, 'f'))
obj.update(getTuple(6, 'f'))
obj.update(getTuple(21,'z'))
obj.update(getTuple(7, 'k'))
print(obj.Dict())
print(obj.size())

print(obj.getValue(1))
print(obj.getValue(7))
print(obj.getValue(22))
print(obj.Dict())
print(obj.size())


print(obj.pop(6))
print(obj.Dict())
print(obj.size())

print(obj.pop(21))
print(obj.size())
