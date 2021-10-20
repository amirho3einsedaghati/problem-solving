# ===================================================== linked-List Implementation ===========================================


class Node:
    def __init__(self,value=None): # this calss, create a node with recieved value. 
        self.value= value
        self.__address= None # meaning: the self points to the last node 
   
    @property
    def address(self):
        return self.__address


    @address.setter
    def address(self, nextNode):
        self.__address= nextNode



class linkedList(Node):
    def __init__(self):
        self.__head= None # meaning: the linked-list is empty


    @property
    def head(self):
        return self.__head


    @head.setter
    def head(self, firstNode):
        self.__head= firstNode


    def __getList(self): # create and return a linked list
        global linkedLi
        linkedLi= []
        return linkedLi


    # this method first update a recurisve list by the items of linked-list then return it
    def getLinkedList(self): 
        backupNode= self.__createBackupHead()
        ls= self.__getList()
        while backupNode is not None: # in the previous Traverses self was an object of node class
            ls.append(backupNode.value)
            backupNode= backupNode.address # in the last iterate is set None for self.address
       
        return ls


    def contains(self,value):
        # solution 1: with use of indexOf method
        return type(self.indexOf(value)) == int 

        # solution 2: with use of linkedLi
        # if value in linkedLi:
        #     return "True"
        # else:
        #     return "False


    # we need first create index for Nodes then we should check node.value with received value, if they was equal; return the index
    def indexOf(self,value):
        if value in linkedLi:
            index= 0
            node= self.__createBackupHead()
            while self.__toLastNode(node):
                if node.value is value:
                    return index

                node= node.address
                index += 1

            return index

        return f"ValueError: {value} is not in list, please enter another value" 


    #if we reached to the last Node in the linked-list, return the lenght of the linked-list
    # big O: O(n)
    def size(self):
        count= 0
        node= self.__createBackupHead()
        while node: # do we have node?
            count += 1 
            node= node.address

        return count


    def __isEmpty(self): # this is a private method
        return self.head== None


    def __toLastNode(self, inp): # this is a private method, this method reach us to the last node of the linked-list 
        return inp.address is not None # don't traverse the last node


    def __createBackupHead(self): # this is a private method
        node= self.head
        return node
    

    def addFirst(self,node):
        # solution 1: with use of Node class
        newNode= Node(node)
        # the blow command checks linked-list is empty or not
        if self.__isEmpty():
            self.head= newNode
        # if was not empty 
        # first we have to create address pointer based-on a node
        newNode.address= self.head
        # then change the value of head.
        self.head= newNode


    def addBetween(self, newVal, availableNode):
        userNode= Node(newVal)
        if len(linkedLi) < 2:
            print(f"OPPs!! you should first add at least 2 nodes to the linked-list; now the count of nodes is {len(linkedLi)}")

        elif availableNode in linkedLi:
            newNode= self.__createBackupHead()
            while newNode.value is not availableNode:
                previNode= newNode
                newNode= newNode.address
        
            previNode.address= userNode
            userNode.address= newNode
        else:
            print(f"the value of {availableNode} is not in the linked-list")

            
    def addLast(self,nodeVal):
        # solution 1: with use of Node class
        newNode= Node(nodeVal)

        # the blow command checks linked-list is empty or not
        if self.__isEmpty():
            self.head= newNode

        # if was not empty
         # we sure at least we have a item  in the linked-list
        node= self.__createBackupHead()
        while self.__toLastNode(node):
            node= node.address

        node.address= newNode


    def deleteFirst(self):
        if self.__isEmpty() or len(linkedLi) < 2: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")

        else:
            # [10 -> 20 -> 30 -> 40]
            # our expected after the execution of program: [20 -> 30 -> 40]

            # solution 1:
            # in this solution the address of the first node is automatically set with None
            # in the solution 1, we need to 2 nodes if we don't have them, we must print a message for user.
            deletedNode= self.__createBackupHead()
            self.head= deletedNode.address
            
            # solution 2: we delete the field of the address of the first Node.
            # in the solution 2, we need to 2 nodes if we don't have them, we must print a message for user.
            # deletedNode= self.head.address
            # self.head.address= None
            # self.head= deletedNode


    def deleteBetween(self, node):
        if self.head== None or len(linkedLi) == 1: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")

        newNode= self.__createBackupHead()
        while newNode.value is not node:
            previNode= newNode
            newNode= newNode.address

        nextNode= newNode.address
        previNode.address= nextNode  

        
    def deleteLast(self):
        if len(linkedLi) < 2: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")

        else:
            # solution 1:
            # in this solution the address of the first node is automatically set with None
            node= self.__createBackupHead()
            while self.__toLastNode(node):
                # previous node 
                previNode= node
                # new node
                node= node.address

            previNode.address= node.address


    # def __generateVacentString(self):
    #     li= ['']
    #     length= self.size()
    #     li *= length

    #     return li


    # i implemented the blow method in the linked-list class but really we don't need it beacause, "getLinkedList" method in the linked-list class
    # update the linked-list to a list and return it and __getList create and return a list

    # def toList(self): # convert linked-list to list and return it 
    #     i= 0
    #     lis= self.__generateVacentString()
    #     backUpNode= self.__createBackupHead()
    #     while self.__toLastNode(backUpNode):
    #         lis[i]= backUpNode.value
    #         backUpNode= backUpNode.address
    #         i += 1
        
    #     lis[i]= backUpNode.value
    #     return lis
              

# ===================================================== create objects ============================================

first= linkedList()

# we should set a value for self.headbecause the value of self.headis None in the class and we have to add a node to the linked-list;
# or we have to use the addFirst or addLast methods 
first.head= Node(10) # we set a new value for self.head
# print(first.size()) # 1

second= Node(20)
# print(first.size()) # 1

third= Node(30)
# print(first.size()) # 1

# we must describe out of class: what does each node 'address pointer', refer to?
first.head.address= second
second.address= third
# print(first.size()) # 3

# we have to use the below method to return the created linked-list 
print(first.getLinkedList())

# print(first.size())

# print(first.indexOf(30))
# print(first.indexOf(7))
 
# the command is for traversing linked-list nodes
# linkedList= first.getLinkedList()
# for item in linkedList:
#     print(item)

# print(first.contains(10))
# print(first.contains(100))

# calling addFirst() method:
first.addFirst(0)
print(first.getLinkedList())
# print(first.size())

# calling solution addLast() method:
first.addLast(40)
print(first.getLinkedList())
# print(first.size())

first.deleteFirst()
print(first.getLinkedList())
# print(first.size())

first.deleteLast()
print(first.getLinkedList())
# print(first.size())

first.deleteBetween(20)
print(first.getLinkedList())
# print(first.size())

first.addBetween(20,40)
# print(first.size())

first.addBetween(20,30)
print(first.getLinkedList())
# print(first.size())

# print(type(first.getLinkedList())) # <class 'list'>

