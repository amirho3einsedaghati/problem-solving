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
        self.__list[last]= item


    def pop(self):
        # O(1)
        li= []
        count= len(self.__list)
        i= 0
        while i != count - 1:
            li.append(self.__list[i])
            i += 1

        backup= self.__list
        self.__list= li
        return backup[i]
        


    def peek(self):
        # O(1)
        count= len(self.__list)

        for i in range(0, count):
            if i == count - 1:
                return self.__list[i]
    

    def isEmpty(self):
        # O(1)
        return self.__list == []


    def reverse(self, string):
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
