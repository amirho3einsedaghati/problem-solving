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
        

    def balanceExpression(self, string: str): # expression syntax checking
        # solution 1: by one stack
        # O(n)
        # open bracket   -> push
        # close bracket  -> pop
        if type(string) == str:
            self.__list= []

            count_brackets= 0
            for item in string:
                if item == '(': 
                    count_brackets += 1
                    self.push(item)
                
                if item == ')':
                    if self.isEmpty():
                        return "stack is empty"

                    count_brackets += 1
                    self.pop()

                if item == '[':
                    count_brackets += 1
                    self.push(item)
                
                if item == ']':
                    if self.isEmpty():
                        return "stack is empty"

                    count_brackets += 1
                    self.pop()

                if item == '{':
                    count_brackets += 1
                    self.push(item)
                
                if item == '}':
                    if self.isEmpty():
                        return "stack is empty"

                    count_brackets += 1
                    self.pop()

                if item == '<':
                    count_brackets += 1
                    self.push(item)
                
                if item == '>':
                    if self.isEmpty():
                        return "stack is empty"

                    count_brackets += 1
                    self.pop()

            if count_brackets == 0:
                return f"{string}: balanced"

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
        #     count_brackets= 0
        #     close_stack= stack()

        #     for item in string:
        #         if item == ')' or item == ']' or item == '}' or item == '>':
        #             if self.isEmpty():
        #                 return "stack is empty"
        #             count_brackets += 1

        #     # linear search to insert the item to self.__list and checks if in received string there was not the items of list return balance 
        #     for i in range(0, len(string)):  
        #         if string[i] in open_collection:
        #             self.push(string[i]) 

        #     for j in range(len(string)- 1, -1, -1): # linear search to insert the item to close_stack
        #         if string[j] in close_collection:
        #             close_stack.push(string[j])

        #     index= 0
        #     while index < len(string): # Linear search to check whether the structure of an expression is incorrect or not
        #         if self.peek() == '(':
        #             if close_stack.peek() == ')':
        #                 self.pop()
        #                 close_stack.pop()
        #                 index += 1
        #             else:
        #                 return f"{string} : unbalanced"

        #             count_brackets += 1 

        #         elif self.peek() == '[':
        #             if close_stack.peek() == ']':
        #                 self.pop()
        #                 close_stack.pop()
        #                 index += 1
        #             else:
        #                 return f"{string} : unbalanced"
                                            
        #             count_brackets += 1

        #         elif self.peek() == '{':
        #             if close_stack.peek() == '}':
        #                 self.pop()
        #                 close_stack.pop()
        #                 index += 1
        #             else:
        #                 return f"{string} : unbalanced"
                                            
        #             count_brackets += 1

        #         elif self.peek() == '<':
        #             if close_stack.peek() == '>':
        #                 self.pop()
        #                 close_stack.pop()
        #                 index += 1
        #             else:
        #                 return f"{string} : unbalanced"
                                            
        #             count_brackets += 1

        #         else:
        #             index += 1

        #     if count_brackets == 0:
        #         return f"{string} : balanced"

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