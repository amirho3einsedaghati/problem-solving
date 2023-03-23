# ------------------------------------- Description ---------------------------
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The sequence starts with 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. The Fibonacci sequence has many interesting properties and is found in nature,
#  art, and music. It is also used in various fields such as computer science, finance, and cryptography.

# ------------------------------------ Implementation --------------------------
def fib(n:int):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b

fib(1000000)
