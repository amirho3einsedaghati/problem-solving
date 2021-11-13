# ================================================ queueReverser ====================================
# problem: if we had an integer number like k and an integer queue like Q, How to reverse the list to the Kst element?


class QueueReverser:
    def __init__(self):
        self.__list= []
        self.__end= -1 # self.__end points to the end of the queue 
        self.__start= -1 # self.__start points to the front of the queue 


    @property
    def queue(self):
        return self.__list


    @queue.setter
    def queue(self, val):
        self.__list.append(val)


    def add(self, item): # add method is like enqueue that adds an item to the end of the queue
        # big O: O(1)
        self.queue= ""
        self.__end += 1
        self.__list[self.__end]= item


    def remove(self): # remove method is like dequeue that deletes an item from the front of the queue and returns the value of it
        # big O: O(1)
        if self.isEmpty():
            return "queue is empty"

        self.__start += 1
        frontQueue= self.__list.pop(self.__start)
        self.__start= -1
        return frontQueue


    def isEmpty(self): # checks queue is empty or not 
        # big O: O(1)
        return self.__list == []


    def __addItmesToQueue(self, item):
        self.add(item)


    def __resetEnd(self):
        self.__end= len(self.__list) -1


    def __resetStart(self):
        self.__start= -1


    def __difference_length_from_k(self, k):
        return len(self.__list) - k


# solution 1: if the reverse method gets one argument.
    # def reverse(self, k: int):
    #     # big O: O(n)
    #     # if we suppose the self.__list be equal [10, 20, 30, 40, 50, 60, 70] and the received k be equal 3
    #     newQueue= QueueReverser()

    #     for i in range(len(self.queue) - 1, -1, -1): # newQueue: [70, 60, 50, 40, 30, 20, 10]
    #         if i > k - 1:
    #             newQueue.__addItmesToQueue(self.queue[i])

    #         elif i <= k - 1:
    #             newQueue.__addItmesToQueue(self.queue[i])

    #     li= []
    #     for i in range(0, newQueue.__difference_length_from_k(k)): # newQueue: [30, 20, 10], li: [70, 60, 50, 40]
    #         newQueue.__resetStart()
    #         li.append(newQueue.remove())
        
    #     newQueue.__resetEnd()
    #     for i in range(len(li) -1, -1, -1): # newQueue: [30, 20, 10, 40, 50, 60, 70]
    #         newQueue.add(li[i])

    #     return newQueue.__list


# solution 2: if the reverse method gets two argument.
    def reverse(self, queue, k):
        # big O: O(n)
        que= QueueReverser()
        que.__list= queue
        li = []

        for i in range(0, k):
            que.__resetStart()
            li.append(que.remove())

        que.__resetEnd()
        while li != []:
            que.__addItmesToQueue(li.pop())


        for i in range(0, que.__difference_length_from_k(k)):
            que.__resetStart()
            front=que.remove()
            que.__resetEnd()
            que.add(front)


        return que.__list


# ================================================ create some objects ====================================


obj= QueueReverser()

obj.add(10)
obj.add(20)
obj.add(30)
obj.add(40)
obj.add(50)
obj.add(60)
obj.add(70)
print(obj.queue)

# print(obj.reverse(3)) # this object is for the first solution of the reverse method
print(obj.reverse([10,20,30,40,50], 4)) # this object is for the second solution of the reverse method
print(obj.queue)

