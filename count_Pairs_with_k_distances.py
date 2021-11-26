# ============================================================== count Pairs with k distances =========================================

# problem: if given you an array of the integer number and k, create a program that can find the number of unique tuples,
# that their items have k distances.


def countPairsWithKdistances(li: list[int], k: int):
    countPairs= 0
    arg= li
    arg= set(arg)
    uniqueList= list(arg)

    for item in uniqueList:
        item += k
        if item in uniqueList:
            countPairs += 1

    return f"the count of the pairs of the {li} is: {countPairs}"


print(countPairsWithKdistances([1,3,4,6,4,5,9,11,12], 2))
print(countPairsWithKdistances([1,3,4,6,4,5,9,11,12,8,5], 2))
print(countPairsWithKdistances([1,3,4,6,4,5,9,11,12,8,5], 3))
print(countPairsWithKdistances([1,4,7,10], 2))
