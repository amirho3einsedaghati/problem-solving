# ============================================================== the mod of the integer list =========================================

# problem: create a program that can returns the most repeated element of the integer array


def mod(args: list[int]):
    # big O: O(n)
    li= [0] * len(args)
    dictionary= dict()

    for i in range(0, len(args)):

        if dictionary.__contains__(args[i]):
            itemValue= dictionary.get(args[i])
            itemValue += 1
            dictionary.update({args[i]: itemValue})

        else:
            li[i] += 1
            dictionary.update({args[i]: li[i]})

    listOfItems= list(dictionary.items())
    listOfKeys= list(dictionary.keys())
    listOfValues= list(dictionary.values())

    listEqualCount= []
    countRepeated= listOfItems[0][1]

    for item in listOfItems:

        if countRepeated < item[1]:
            countRepeated= item[1]
        
        elif item[1] > 1 and countRepeated == item[1]:
            countRepeatedIndex= listOfValues.index(countRepeated)
            listEqualCount.append(listOfKeys[countRepeatedIndex])
            listEqualCount.append(item[0])

    if listEqualCount != []:
        setCount= set(listEqualCount)
        listEqualCount= list(setCount)

        print(f"the mod of {args} is:", end= ' ')

        for item in listEqualCount:

            if listEqualCount[0] <= item < listEqualCount[len(listEqualCount) - 1]:
                print(item, end= " | ")

            elif item == listEqualCount[len(listEqualCount) - 1]:
                print(item, end= "\n")

    elif countRepeated == 1:
        print("None of the items are not mod")

    else:
        indexCountRepeatedItem= listOfValues.index(countRepeated)
        print(f"the mod of {args} is: {listOfItems[indexCountRepeatedItem][0]}")



mod([1,2,4])
mod([1,2,2,2,4,4])
mod([1,2,2,2,4,4,4])
mod([1,2,2,2,4,4,4,3,3,3])

