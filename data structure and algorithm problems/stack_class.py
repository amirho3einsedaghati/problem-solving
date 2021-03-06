# ================================================ implementation stack class ====================================
# implement one stack by an array.


class stack:
    def __init__(self):
        self.__list= []
        self.__top= -1
        self.__leftBracket= ('(', '[', '{', '<')
        self.__rightBracket= (')', ']', '}', '>')


    @property
    def stack(self):
        # O(1)
        return self.__list


    @stack.setter
    def stack(self, vacentString):
        # O(1)
        self.__list.append(vacentString)


    def push(self, item):
        # O(1)
        self.stack= ''
        self.__top += 1
        last= len(self.__list) - 1
        self.__list[last]= item # inserts a item to top of stack


    def pop(self):
        # solution 1: 
        # big O: O(1)
        if self.isEmpty():
            return "stack is empty"
        
        self.__top += (-1)
        delTop= self.__list.pop()
        return delTop

        # solution 2: 
        # O(n)
        # li= []
        # count= len(self.__list)

        # i= 0
        # while i != count - 1:
        #     li.append(self.__list[i])
        #     i += 1

        # backup= self.__list
        # self.__list= li # delete a item from top of stack 
        # return backup[i] # and returns the deleted item from top of stack
        

    def peek(self):
        # solution 1: 
        # big O: O(1)
        if self.isEmpty(): return "stack is empty"

        return self.__list[self.__top]

        # solution 2: 
        # O(n)
        # count= len(self.__list)

        # for i in range(0, count):
        #     if i == count - 1:
        #         return self.__list[i] # returns a item of the top of stack without delete it
    

    def isEmpty(self):
        # O(1)
        return self.__list == []


    def reverse(self, string): # return the reversed string 
        # O(n)
        self.__list= []
        for item in string:
            self.push(item)

        li= []
        for i in range(len(self.__list) - 1, -1, -1): # this loop is for deleting the items
            li.append(self.pop())
            
        reversed= ""
        for i in range(0, len(li)):
            reversed += "".join(li[i])

        return reversed
        

    def __isOpenBracket(self, lefBra):
        return self.__leftBracket.__contains__(lefBra)


    def __isCloseBracket(self, rightBra):
        return self.__rightBracket.__contains__(rightBra)


    def __isBracketsMatch(self, left, right):
        # returns True or False
        # True: are not match
        # False: are match
        return  self.__leftBracket.index(left) is not self.__rightBracket.index(right)


    def balanceExpression(self, string: str): # expression syntax checking
        # solution 1: implemented by one stack -> more optimized solution
        # O(n)
        # open bracket   -> push
        # close bracket  -> pop
        if type(string) == str:
            self.__list= []

            for item in string:
                if self.__isOpenBracket(item): 
                    self.push(item)
                
                if self.__isCloseBracket(item):
                    if self.isEmpty(): return "stack is empty"
                    
                    leftBracket= self.pop()
                    if (self.__isBracketsMatch(leftBracket, item)): 
                        return f"{string}: unbalanced" 

            if self.isEmpty():
                return f"{string}: balanced"
            else:
                return f"{string}: unbalanced"

        return "please just enter a string" 

        # solution 2: implemented by two stacks 
        # note: it works if you use the solution of the second peek and pop
        # O(n)
        # if type(string) == str:
        #     self.__list= []
        #     close_stack= stack()

        #     # linear search to insert the item to self.__list and checks if in received string there was not the items of list return balance 
        #     for i in range(0, len(string)):  
        #         if string[i] in self.__leftBracket:
        #             self.push(string[i]) 

        #     for j in range(len(string)- 1, -1, -1): # linear search to insert the item to close_stack
        #         if string[j] in self.__rightBracket:
        #             close_stack.push(string[j])

        #     index= 0
        #     while index < len(string): # Linear search to check whether the structure of an expression is incorrect or not
        #         if string[0] in self.__list:
        #             item= self.peek()
        #             if self.__isOpenBracket(item):
        #                     open= self.pop()
        #                     close= close_stack.pop()
        #                     if self.__isBracketsMatch(open, close): return f"{string} : unbalanced"
        #                     index += 1

        #         elif string[0] in close_stack.__list:
        #             return "stack is empty"

        #         else:
        #             index += 1

        #     return f"{string} : balanced"

        # elif type(string) != str: 
        #     return "please just enter a string"  
        # 


# question: design a stack contains push, pop and min; that min method return the smallest value through constant time
class minStack:
    def __init__(self):
        self.valueStack= stack()
        self.minStack= stack()
    

    def push(self, item):
        # O(1)
        self.valueStack.push(item)
    
        if self.minStack.isEmpty():
            self.minStack.push(item)
        
        elif item < self.minStack.peek():
            self.minStack.push(item)
    

    def pop(self):
        # O(1)
        if self.valueStack.isEmpty():
            return "stack is empty"

        top= self.valueStack.pop()

        if top == self.minStack.peek():
            self.minStack.pop()
        
        return top


    def min(self): 
        # constant time: big O: O(1)
        if self.minStack.isEmpty():
            return "stack is empty"

        return self.minStack.peek()


# ================================================ create some objects ====================================


print('======================================= Stack =================================')
obj= stack()

print(obj.isEmpty())

obj.push(10)
obj.push(20)
obj.push(30)
print(obj.stack)

print(obj.peek())
print(obj.isEmpty())

x= obj.pop()
print(obj.stack)
print(x) # 30

print(obj.peek())
print(obj.isEmpty())

print('===================')
print(obj.reverse("amirali"))
print(obj.stack)
obj.push(100)
obj.push(200)
print(obj.stack)

print('===================')
print(obj.balanceExpression("([2 + 4 [3])")) ## unbalanced
print(obj.balanceExpression("(<[{2 + 4 [3]}]>)")) ## balanced
print(obj.balanceExpression("( 1 + 2 < 13[{ 4 + 9 + [5 {6}]}]>)")) ## balanced
print(obj.balanceExpression("( 1 + 2 < 13[{ 4 + 9 + [5 {6}]]>)")) ## unbalanced
print(obj.balanceExpression("1 + 2"))
print(obj.balanceExpression(""))
print(obj.balanceExpression("$"))
print(obj.balanceExpression([]))
print(obj.balanceExpression(")12 + 1("))
print(obj.balanceExpression("(12 + 1>"))

print('======================================= minStack =================================')
instance= minStack()
print(instance.min())

instance.push(10)
instance.push(5)
instance.push(30)
instance.push(6)
print(instance.min())

print('------------')
print(instance.pop())
print(instance.min())

print('------------')
print(instance.pop())
print(instance.min())

print('------------')
print(instance.pop())
print(instance.min())

