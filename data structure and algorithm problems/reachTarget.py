# ========================================= the sum of the indices values, bring us to the target value ========================================

# problem: if given you an array of the integer number and target value, create a program that can find the values of the indices 
# That the sum of them, bring us to the target value.


def reachTarget(li: list[int], target: int):
    # big O: O(n)
    uniqueList= list()

    for item in li:
        if item not in uniqueList:
            uniqueList.append(item)

    indicesList= []
    copy= None

    for i in range(0, len(uniqueList) - 1):
        reachTargetVal= target - uniqueList[i]

        if reachTargetVal in uniqueList and i > uniqueList.index(reachTargetVal):
            reachTargetIndex= uniqueList.index(reachTargetVal)
            
            indicesList.append(reachTargetIndex)
            indicesList.append(i)

            print(indicesList, end= " ")

            copy= indicesList.copy()
            indicesList.clear()

    if copy == None:
        print(f"can't reach to the {target}")

    print('\n')



reachTarget([2,7,2,7,11,13], 9)
reachTarget([2,7,3,6,11,13], 9)
reachTarget([1,2,11,13], 9)

