# ===================================================== linked-List Implementation ============================================

class Node:
    def __init__(self,value=None): # this calss, create a node with recieved value. 
        self.value= value
        self.address= None
        
class linkedList:
    def __init__(self):
        self.head= None

    # getter
    def GetlinkedList(self):
        return linkedLi

    # setter
    def SetLinkedList(self, val=None):
        if val == None:
            self= self.head
            global linkedLi
            linkedLi= []
            while self is not None: # in the previous Traverses self was an object of node class
                linkedLi.append(self.value)
                # print(self.value) # the command is for traversing linked-list nodes
                self= self.address # in the last iterate is set None for self.address
        else:
            linkedLi= val
    
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

    def resize(self, item): # this is a private method 
        resizedList= [""]
        if type(item) == int or type(item) == int:
            size= len(linkedLi)
            size += 1 
            resizedList *= size
            return resizedList

    def addFirst(self,node):
        # solution 1: with use of Node class
        newNode= Node(node)
        newNode.address= self.head
        self.head= newNode
        
        # solution 2: without use of Node class and with use of resize method
        # res= self.resize(node)
        # for i in range(0, len(res)):
        #     if i == 0:
        #         res[i] = node
        #     elif 0 < i <= len(res) - 1:
        #         res[i]= linkedLi[i - 1]
        # self.SetLinkedList(res)
             
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

        # solution 2:
        # res= self.resize(node)
        # for i in range(0, len(res)):
        #     if 0 <= i <= len(res) - 2:
        #         res[i]= linkedLi[i]
        #     elif i == len(res) - 1:
        #         res[i] = node
        # self.SetLinkedList(res)

    def deleteFirst(self, node):
        if node not in linkedLi:
            print(f"the node of {node} is not in the linked-list")
        else:
            pass



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

# calling in solution 1 for addFirst() method:
first.addFirst(0)
first.SetLinkedList()
print(first.GetlinkedList())

# calling solution 2 for addFirst() method:
# first.addFirst(0)
# print(first.GetlinkedList())

# calling solution 1 for addLast() method:
first.addLast(40)
first.SetLinkedList()
print(first.GetlinkedList())

# calling solution 2 for addLast() method:
first.addLast(40)
print(first.GetlinkedList())

# first.deleteFirst(100)