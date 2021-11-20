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


    def update(self, key, value):
        bucketIndex= self.__getBucketIndex(key)
        bucketNode= self.__getBucketNode(bucketIndex)

        if bucketNode == None:
            self.__buckets[bucketIndex]= Node(key, value) # Create node, add it, return
            return

        else:
	        while bucketNode is not None: # Collision! Iterate to the end of the linked list at provided index
		        currentNode = bucketNode
		        bucketNode = bucketNode._Node__address 

	        currentNode._Node__address = Node(key, value) # Add a new node at the end of the list with provided key/value


    def getValue(self, key):
        bucketIndex= self.__getBucketIndex(key)
        bucketNode= self.__getBucketNode(bucketIndex)

        if bucketNode == None:
            return

        elif bucketNode._Node__address == None:
            return bucketNode._Node__value 

        lastNode= self.__getlastNodeValue(bucketNode)
        return lastNode._Node__value


    def remove(self, key):
        bucketIndex= self.__getBucketIndex(key)
        bucketNode= self.__getBucketNode(bucketIndex)

        lastNode= self.__getlastNodeValue(bucketNode)

        dictionary= dict(self.__lisTuple)
        listDict= list(dictionary.items())

        for tuple in listDict:
            if tuple[1] == lastNode._Node__value:
                listDict.remove(tuple)
                self.__lisTuple= listDict
                break

        return lastNode._Node__value


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


    def __getBucketIndex(self, key: int):
        return self.__hashFunction(key) # Compute index of key


    def __getBucketNode(self, index: int):
        return self.__buckets[index]


    def __getlastNodeValue(self, node: Node):
        while node != None:
            curentNode= node
            node= node._Node__address

        return curentNode


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
