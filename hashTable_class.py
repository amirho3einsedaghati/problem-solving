# ========================================== implementation a hash table with the chaining method  ================================


class Node:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__address = None


    def getKeyValue(self):
        li= []
        node= self

        while node != None:
            lastNode= node
            node= node.__address

            if node != None and node.__key != self.__key:
                li.append(tuple([self.__key, self.__value]))

        li.append(tuple([lastNode.__key, lastNode.__value]))

        return li


class HashTable:
    def __init__(self, capacityBucket):
        self.__capacity= capacityBucket
        self.__buckets= [None] * self.__capacity
        self.__lisTuple= []


    def __getlistofTuple(self):
        for item in self.__buckets:

            if type(item) == Node:
                self.__lisTuple.extend(item.getKeyValue())
        
        return self.__lisTuple


    def Dict(self):
        return dict(self.__lisTuple)
        
        

    def __getlistOfList(self): # this method has came beacause see what self.__buckets looks like
        lis= self.__getlistofTuple()

        liLi= [0] * self.__capacity

        for item in lis:
            index= self.__hashFunction(item[0])

            if liLi[index] == 0:
                liLi[index]= [item]

            else:
                tup= liLi[index] 
                tup.append(item)

        return liLi


    def __hashFunction(self, key):
        return key % len(self.__buckets)


    def update(self, key, value):
	    index = self.__hashFunction(key) # Compute index of key
	    nodeLL = self.__buckets[index]

	    if nodeLL is None: # If bucket is empty:
		    self.__buckets[index] = Node(key, value) # Create node, add it, return
		    return
        
	    while nodeLL is not None: # Collision! Iterate to the end of the linked list at provided index
		    currentNode = nodeLL
		    nodeLL = nodeLL._Node__address 

	    currentNode._Node__address = Node(key, value) # Add a new node at the end of the list with provided key/value


    def getValue(self, key):
        index= self.__hashFunction(key)

        targetNode= self.__buckets[index]

        if targetNode == None:
            return

        elif targetNode._Node__address == None:
            return targetNode._Node__value 

        while targetNode != None:
            curentNode= targetNode
            targetNode= targetNode._Node__address

        return curentNode._Node__value 


    def remove(self, key):
        index= self.__hashFunction(key)

        targetNode= self.__buckets[index]

        while targetNode._Node__address != None:
            targetNode= targetNode._Node__address

        dictionary= dict(self.__lisTuple)

        listDict= list(dictionary.items())

        for tuple in listDict:
            if tuple[1] == targetNode._Node__value:
                listDict.remove(tuple)
                self.__lisTuple= listDict
                break

        return targetNode._Node__value


# ========================================== create some objects ================================
    

obj= HashTable(7) # in the maximum state can keeps two more non-repetitive items than it can hold; for example if capacityBucket be 7, it can keeps up to 9 items  
obj.update(1, "a")
obj.update(22, "b")
obj.update(2, 'd')
obj.update(3, 'e')
obj.update(4, 'e')
obj.update(4, 'e')
obj.update(5, 'f')
obj.update(6, 'f')
obj.update(21,'z')
obj.update(7, 'k')

print(obj.getValue(5))

x= obj._HashTable__getlistOfList()
print(x)

print(obj.getValue(0))

print(obj.Dict())

print(obj.remove(1))
print(obj.remove(2))
print(obj.Dict())
