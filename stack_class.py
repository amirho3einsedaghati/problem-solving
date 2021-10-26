# ================================================ implementation stack class ====================================


class stack:
    def __init__(self):
        self.__list= []
    

    @property
    def stack(self):
        return self.__list


    @stack.setter
    def stack(self, string):
        self.__list.append(string)


    def push(self, item):
        self.stack= ''
        last= len(self.__list) - 1
        self.__list[last]= item


    def pop(self):
        li= []
        count= len(self.__list)

        for i in range(0, count):
            if i != count - 1:
                li.append(self.__list[i])
        
        self.__list= li


    def peek(self):
        count= len(self.__list)

        for i in range(0, count):
            if i == count - 1:
                return self.__list[i]
    

    def isEmpty(self):
        return self.__list == []

# ================================================ create some objects ====================================

obj= stack()

print(obj.isEmpty())

obj.push(10)
obj.push(20)
obj.push(30)
print(obj.stack)

print(obj.peek())
print(obj.isEmpty())

obj.pop()
print(obj.stack)

print(obj.peek())
print(obj.isEmpty())
