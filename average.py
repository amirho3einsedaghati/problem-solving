

# solution 1 (dynamic):
# prints the average of the entered integer numbers

numbers= map(int,input("please enter the 4 numbers:").split())
numbers= list(numbers)

def avg(li):
    total= 0
    for item in li:
        total += item 
    length= len(li)
    avg= total / length
    print(avg)

avg(numbers)



# solution 2 (static): 
# prints the average of the 4 integer numbers

# a, b, c, d= map(int,input("please enter the 4 numbers:").split())

# def avg(a, b, c, d):
#     total= a + b + c + d
#     avg= total / 4
#     print(avg)

# avg(a,b,c,d)



