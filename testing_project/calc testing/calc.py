# add, sub, mult, div

def add(a: int , b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def mutiply(a: int, b: int):
    return a * b


def divide(a:int , b: int):
    if b == 0:
        raise ZeroDivisionError("can not divide by zero!")
    
    return a / b


# print(13 / 2) # 6.5
# print(13 // 2) # 6
