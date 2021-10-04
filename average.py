# average the 4 interger number:

# raveshe 1 (dynamic):
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

# ravesh 2 (static):
# a, b, c, d= map(int,input("please enter the 4 numbers:").split())

# def avg(a, b, c, d):
#     total= a + b + c + d
#     avg= total / 4
#     print(avg)

# avg(a,b,c,d)



