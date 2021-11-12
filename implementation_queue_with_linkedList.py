# ================================================ linkedListQueue ====================================
# problem: implement a queue with linked list that covers followig method.
# enqueue(), dequeue(), peek(), size(), isEmpty()


from types import NoneType


class Node:
    def __init__(self,value=None): # this calss, create a node with recieved value. 
        self.value= value
        self.__address= None # meaning: the self points to the last node 
   
    @property
    def address(self):
        # big O: O(1)
        return self.__address


    @address.setter
    def address(self, nextNode):
        # big O: O(1)
        self.__address= nextNode


class linkedList(Node):
    def __init__(self):
        self.__head= None # meaning: the linked-list is empty


    @property
    def head(self):
        # big O: O(1)
        try:
            return self.__head
        except AttributeError:
            return self._linkedList__head
        

    @head.setter
    def head(self, firstNode):
        # big O: O(1)
        try:
            self.__head= firstNode
        except:
            self._linkedList__head= firstNode
        


    def __getList(self): # create and return a linked list
        # big O: O(1)
        global linkedLi
        linkedLi= []
        return linkedLi


    # this method first update a recurisve list by the items of linked-list then return it
    def getConvertedLinkedList(self): 
        # big O: O(n)
        backupNode= self.__createBackupHead()
        ls= self.__getList()

        while backupNode is not None: # in the previous Traverses self was an object of node class
            ls.append(backupNode.value)
            backupNode= backupNode.address # in the last iterate is set None for self.address
       
        return ls


    #if we reached to the last Node in the linked-list, return the lenght of the linked-list
    # big O: O(n)
    def size(self):
        # big O: O(n)
        count= 0
        node= self.__createBackupHead()

        while node: # do we have node?
            count += 1 
            node= node.address

        return count


    def __isEmpty(self): # this is a private method
        # big O: O(1)
        return self.head== None


    def __toLastNode(self, inp): # this is a private method, this method reach us to the last node of the linked-list 
        # big O: O(1)
        return inp.address is not None # don't traverse the last node


    def __createBackupHead(self): # this is a private method
        # big O: O(1)
        node= self.head
        return node

            
    def addLast(self,nodeVal):
        # big O: O(1)
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
        # big O: O(1)
        if self.__isEmpty() or len(self.getConvertedLinkedList()) < 2: # if linked-list was empty or had a one node
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")

        else:
            # [10 -> 20 -> 30 -> 40]
            # our expected after the execution of program: [20 -> 30 -> 40]
            deletedNode= self.__createBackupHead()
            self.head= deletedNode.address
            return deletedNode.value


class linkedListQueue:
    def __init__(self):
        self.__queue= linkedList()
        self.__queue.head= Node()
        

    def getQueue(self):
        return self.__queue.getConvertedLinkedList()


    def __hasQueueNone(self, lis):
        return None in lis


    def enQueue(self, item):
        self.__queue.addLast(item)

        if self.__hasQueueNone(self.__queue.getConvertedLinkedList()):
            self.deQueue()
            

    def deQueue(self):
        firstItem= self.__queue.deleteFirst()
        return firstItem
    

    def peek(self):
        if self.__queue._linkedList__isEmpty() or len(self.__queue.getConvertedLinkedList()) < 2:
            print("there is no node in the linked-list or there is one node in the linked-list. \nat least we need 2 nodes in the linked-list.")

        else:
            firstItem= self.__queue._linkedList__createBackupHead()
            return firstItem.value


    def size(self):
        return self.__queue.size()

    
    def isEmpty(self):
        if self.__hasQueueNone(self.__queue.getConvertedLinkedList()):
            return True

        return False


# ===================================================== create some objects ============================================


obj= linkedListQueue()

obj.deQueue()
print('---------')
obj.peek()
print('---------')
print(obj.isEmpty())

obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(30)
obj.enQueue(40)
print(obj.getQueue())
print(obj.size())
print(obj.isEmpty())

print('---------')
print(obj.peek())
print(obj.deQueue())
print(obj.getQueue())
print(obj.size())
print(obj.isEmpty())
