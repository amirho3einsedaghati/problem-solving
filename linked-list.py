# ===================================================== linked-List Implementation ============================================

class linkedList:
    def __init__(self):
        self.head= None

    def __returnLinkedList__(self):
        self= self.head
        linkedList= []
        while self is not None: # in the previous Traverses self was an object of node class
            linkedList.append(self.value)
            # print(self.value) # the command is for traversing linked-list nodes
            self= self.address # in the last iterate is set None for self.address
        return linkedList
        

class node:
    def __init__(self,value=None):
        self.value= value
        self.address= None

# ===================================================== create objects ============================================

first= linkedList()
first.head= node(10) # we set a new value for self.head

second= node(20)
third= node(30)
first.head.address= second
second.address= third

print(first.__returnLinkedList__())
linkedList= first.__returnLinkedList__()
for item in linkedList:
    print(item)

