# ------------------------------- Description ------------------------------------------
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
# So, Any whole number which is greater than 1 and has only two factors that is 1 and the number itself, is called a prime number

# ------------------------ the Implementation of the solution 1 ------------------------
def is_prime1(n:int):
    if (n > 1):
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                return False
        return True # for n = 2 and n = 3, It returns True because range(2,2) is equivalent to an empty list
    else:
        return '{} is a inappropriate argument, because It is  n <= 1'.format(n)

# print(is_prime1(2))
# print(is_prime1(3))
# print(is_prime1(1029))
# print(is_prime1(12))
# print(is_prime1(1))

# ------------------------ the Implementation of the solution 2 ------------------------

from math import sqrt

def is_prime2(n: int):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True # for n = 2 and n = 3, It returns True because range(2,2) is equivalent to an empty list
    else:
        return "{} is a inappropriate argument, because It is n <= 1".format(n)

# print(is_prime2(2))
# print(is_prime2(3))
# print(is_prime2(1029128))
# print(is_prime2(16))
# print(is_prime2(-1))

# ---------- let's see how many prime numbers are in 1 million number --------------

count = 0
for i in range(2, 1000000):
    if is_prime2(i):
        count += 1
print('There are {} prime numbers in 1 million number'.format(count))
    