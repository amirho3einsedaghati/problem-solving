# ===================================================== linked-List Implementation ============================================

class Node:
    def __init__(self,value=None): # this calss, create a node with recieved value. 
        self.value= value
        self.address= None
        
class linkedList(Node):
    def __init__(self):
        self.head= None

    # getter
    def GetlinkedList(self):
        return linkedLi

    # setter
    def SetLinkedList(self, val=None):
        self= self.head
        global linkedLi
        linkedLi= []
        while self is not None: # in the previous Traverses self was an object of node class
            linkedLi.append(self.value)
            # print(self.value) # the command is for traversing linked-list nodes
            self= self.address # in the last iterate is set None for self.address


    def contains(self,value):
        if value in linkedLi:
            return "True"
        else:
            return "False"


    def indexOf(self,value):
        if value in linkedLi:
            for i in range(0,len(linkedLi)):
                if linkedLi[i] == value:
                    return i 
        else:
            return f"ValueError: {value} is not in list, please enter another value" 


    def isEmpty(self):
        return self.head == None


    def toLastNode(self, inp):
        return inp.address is not None


    def addFirst(self,node):
        # solution 1: with use of Node class
        newNode= Node(node)
        newNode.address= self.head
        self.head= newNode


    def addBetween(self, newVal, availableNode):
        userNode= Node(newVal)
        if len(linkedLi) < 2:
            print(f"OPPs!! you should add at least 2 nodes to the linked-list, now the count of nodes is {len(linkedLi)}")
        elif availableNode in linkedLi:
            newNode= self.head
            while newNode.value is not availableNode:
                previNode= newNode
                newNode= newNode.address
        
            previNode.address= userNode
            userNode.address= newNode
        else:
            print(f"the value of {availableNode} is not in the linked-list")


    def addLast(self,node):
        # solution 1: with use of Node class
        newNode= Node(node)
        # the blow command checks linked-list is empty or not
        if self.head == None:
            self.head= newNode
        # if was not empty
         # we sure at least we have a item  in the linked-list
        isNode= self.head
        while isNode.address:
            isNode= isNode.address
        isNode.address= newNode


    def deleteFirst(self):
        if self.head == None: # if linked-list was empty
            print(f"there is no node in the linked-list")
        else:
            deletedNode= self.head
            self.head= deletedNode.address


    def deleteBetween(self, node):
        if self.head == None: # if linked-list was empty
            print(f"there is no node in the linked-list")

        newNode= self.head
        while newNode.value is not node:
            previNode= newNode
            newNode= newNode.address
        nextNode= newNode.address
        previNode.address= nextNode   
    

    def deleteLast(self):
        if self.head == None: # if linked-list was empty
            print(f"there is no node in the linked-list")
        else:
            # nextNode= self.head
            deletedNode= self.head
            # self.head= deletedNode.address
            while deletedNode.address != None:
                # previous node 
                previNode= deletedNode
                # new node
                deletedNode= deletedNode.address

            previNode.address= deletedNode.address


# ===================================================== create objects ============================================

first= linkedList()
# we must set a value for self.head because the value of self.head is None in the class.
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