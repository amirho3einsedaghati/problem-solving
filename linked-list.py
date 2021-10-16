# ===================================================== linked-List Implementation ============================================

class Node:
    def __init__(self,value=None): # this calss, create a node with recieved value. 
        self.value= value
        self.address= None
        
class linkedList(Node):
    def __init__(self):
        self.head= None


    # getter
    def GetlinkedList(self): # return a setted value
        return linkedLi


    # setter
    def SetLinkedList(self): # update and create a linked-list
        self= self.createBackupHead()
        global linkedLi
        linkedLi= []
        while self is not None: # in the previous Traverses self was an object of node class
            linkedLi.append(self.value)
            # print(self.value) # the command is for traversing linked-list nodes
            self= self.address # in the last iterate is set None for self.address


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
            node= self.createBackupHead()
            while self.toLastNode(node):
                if node.value is value:
                    return index

                node= node.address
                index += 1

            return index

        return f"ValueError: {value} is not in list, please enter another value" 

   
    def isEmpty(self):
        return self.head == None


    def toLastNode(self, inp):
        return inp.address is not None


    def createBackupHead(self):
        node= self.head
        return node


    def addFirst(self,node):
        # solution 1: with use of Node class
        newNode= Node(node)
        # the blow command checks linked-list is empty or not
        if self.isEmpty():
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
            newNode= self.createBackupHead()
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
        if self.isEmpty():
            self.head= newNode
        # if was not empty
         # we sure at least we have a item  in the linked-list
        node= self.createBackupHead()
        while self.toLastNode(node):
            node= node.address

        node.address= newNode


    def deleteFirst(self):
        if self.head == None or len(linkedLi) < 2: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")
        else:
            # [10 -> 20 -> 30 -> 40]
            # our expected after the execution of program: [20 -> 30 -> 40]

            # solution 1:
            # in this solution the address of the first node is automatically set with None
            # in the solution 1, we need to 2 nodes if we don't have them, we must print a message for user.
            deletedNode= self.createBackupHead()
            self.head= deletedNode.address

            # solution 2: we delete the field of the address of the first Node.
            # in the solution 2, we need to 2 nodes if we don't have them, we must print a message for user.
            # deletedNode= self.head.address
            # self.head.address= None
            # self.head= deletedNode
    

    def deleteBetween(self, node):
        if self.head == None or len(linkedLi) < 2: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")

        newNode= self.createBackupHead()
        while newNode.value is not node:
            previNode= newNode
            newNode= newNode.address

        nextNode= newNode.address
        previNode.address= nextNode  
    

    def deleteLast(self):
        if self.head == None or len(linkedLi) < 2: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")
        else:
            node= self.createBackupHead()
            while self.toLastNode(node):
                # previous node 
                previNode= node
                # new node
                node= node.address

            previNode.address= node.address


# ===================================================== create objects ============================================

first= linkedList()

# we should set a value for self.head because the value of self.head is None in the class and we have to add a node to the linked-list;
# or we have to use the addFirst or addLast methods 
first.head= Node(10) # we set a new value for self.head

second= Node(20)
third= Node(30)

# we must describe out of class: what does each node 'address pointer', refer to?
first.head.address= second
second.address= third

# we have to use the below method to create and update linked-list 
first.SetLinkedList()

# this method return the created linked-list
print(first.GetlinkedList())

# print(first.indexOf(30))
# print(first.indexOf(7))
 
# the command is for traversing linked-list nodes
# linkedList= first.__returnLinkedList__()
# for item in linkedList:
#     print(item)

# print(first.contains(10))
# print(first.contains(100))

# calling solution 1 for addFirst() method:
first.addFirst(0)
first.SetLinkedList()
print(first.GetlinkedList())

# calling wrong solution for addFirst() method:
# first.addFirst(0)
# print(first.GetlinkedList())

# calling solution 1 for addLast() method:
first.addLast(40)
first.SetLinkedList()
print(first.GetlinkedList())

# calling wrong solution for addLast() method:
# first.addLast(40)
# print(first.GetlinkedList())

first.deleteFirst()
first.SetLinkedList()
print(first.GetlinkedList())

first.deleteLast()
first.SetLinkedList()
print(first.GetlinkedList())

first.deleteBetween(20)
first.SetLinkedList()
print(first.GetlinkedList())

first.addBetween(20,40)

first.addBetween(20,30)
first.SetLinkedList()
print(first.GetlinkedList())