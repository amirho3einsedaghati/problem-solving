# ================================================ implementation stack class ====================================


class stack:
    def __init__(self):
        self.__list= []


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
        last= len(self.__list) - 1
        self.__list[last]= item # inserts a item to top of stack


    def pop(self):
        # O(n)
        li= []
        count= len(self.__list)

        i= 0
        while i != count - 1:
            li.append(self.__list[i])
            i += 1

        backup= self.__list
        self.__list= li # delete a item from top of stack 
        return backup[i] # and returns the deleted item from top of stack
        

    def peek(self):
        # O(n)
        count= len(self.__list)

        for i in range(0, count):
            if i == count - 1:
                return self.__list[i] # returns a item of the top of stack without delete it
    

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
        return lefBra == '(' or lefBra == '[' or lefBra == '{' or lefBra == '<'

    def __isCloseBracket(self, rightBra):
        return rightBra == ')' or rightBra == ']' or rightBra == '}' or rightBra == '>'

    def __isBracketsMatch(self, right, left):
        # return True or False
        # True: are not match
        # False: are match
        return  (
                (right is ')' and left is not '(') or
                (right is '}' and left is not '{') or
                (right is ']' and left is not '[') or 
                (right is '>' and left is not '<')
                )

    def balanceExpression(self, string: str): # expression syntax checking
        # solution 1: by one stack -> more optimized solution
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
                    if (self.__isBracketsMatch(item, leftBracket)): 
                        return f"{string}: unbalanced" 

            if self.isEmpty():
                return f"{string}: balanced"
            else:
                return f"{string}: unbalanced"

        return "please just enter a string" 

        # solution 2: by two stacks
        # O(n)
        # if type(string) == str:
        #     self.__list= []
        #     open_collection= ['(', '[', '{', '<']
        #     close_collection= [')', ']', '}', '>']
        #     close_stack= stack()

        #     # linear search to insert the item to self.__list and checks if in received string there was not the items of list return balance 
        #     for i in range(0, len(string)):  
        #         if string[i] in open_collection:
        #             self.push(string[i]) 

        #     for j in range(len(string)- 1, -1, -1): # linear search to insert the item to close_stack
        #         if string[j] in close_collection:
        #             close_stack.push(string[j])

        #     index= 0
        #     while index < len(string): # Linear search to check whether the structure of an expression is incorrect or not
        #         if string[0] in self.__list:
        #             item= self.peek()
        #             if self.__isOpenBracket(item):
        #                     open= self.pop()
        #                     close= close_stack.pop()
        #                     if self.__isBracketsMatch(close, open): return f"{string} : unbalanced"
        #                     index += 1

        #         elif string[0] in close_stack.__list:
        #             return "stack is empty"

        #         else:
        #             index += 1

        #     return f"{string} : balanced"

        # elif type(string) != str: 
        #     return "please just enter a string"   

# ================================================ create some objects ====================================


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

print(obj.reverse("amirali"))
print(obj.stack)
obj.push(100)
obj.push(200)
print(obj.stack)

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
