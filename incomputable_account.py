# incomputable account:

Dep= 0
min= 0
li= []

def transaction():
    global tx
    try:
        tx= int(input("enter the number of your daily transaction (1 <= tx <= 100): "))
    except ValueError:
        transaction()
    else:
        if tx <= 0 or tx > 100:
            transaction()

try:
    tx= int(input("enter the number of your daily transaction (1 <= tx <= 100): "))
except ValueError:
    transaction()
else:
    if tx <= 0 or tx > 100:
        transaction()

print(f" \n the daily transaction informations are: \n 1.type 'withdraw' or 'deposit' \n 2.the amount of the transaction \n 3.the transaction time \n 4.type 'ok' for successful withdraw, and type 'fail' if your transaction has succeeded \n Example1: deposit 100 12:00 \n Example2: withdraw 1400 18:00 fail \n Example3: withdraw 600 16:30 ok \n")

for i in range(1,tx + 1):
    info_tx= map(str, input(f"the information of the transaction {i}: ").split())
    li.append(list(info_tx))
    
             

for i in range(0,len(li)):

    if (tx == 2) and (li[i][0] == "withdraw") and (li[i][3] == "ok"):
        if li[i + 1][0] == "deposit" or li[i + 1][3] == "fail":
            print(f"the minimum money today: {li[i][1]}")
        elif li[i + 1][3] == "ok":
            print(f"the minimum money today: {int(li[i][1]) + int(li[i + 1][1])}")

    if (tx == 2) and li[i][0] == "withdraw" and li[i][3] == "fail":
        if li[i + 1][0] == "deposit":
            print("imposible")
        elif li[i + 1][3] == "ok":
            print(f"the minimum money today: {li[i + 1][1]}")
        elif li[i + 1][3] == "fail":
            print(f"the minimum money today: {0}")
    
    if (tx == 2) and li[i][0] == "deposit":
        if li[i + 1][0] == "deposit" or li[i + 1][3] == "fail":
            print(f"the minimum money today: {0}")
        elif li[i + 1][3] == "ok" and li[i][1] > li[i + 1][1]:
            print(f"the minimum money today: {0}")
        elif li[i + 1][3] == "ok" and li[i][1] < li[i + 1][1]:
            subtrac= int(li[i][1]) - int(li[i + 1][1])
            min = -(subtrac)
            print(f"the minimum money today: {min}")


    if  tx == 1 and li[i][0] == "withdraw":
        print(f"the minimum money today: {li[i][1]}")

    if  tx == 1 and li[i][0] == "deposit":
        print(f"the minimum money today: {0}")

    if tx > 2 and li[i][0] == "deposit":
        if Dep >= 0:
            Dep += int(li[i][1])

    
    if tx > 2 and li[i][0] == "withdraw":
        if Dep >= 0 and li[i][3] == "ok":
            Dep -= int(li[i][1])
            if Dep < 0:
                res= -(Dep)
                min += res
                Dep= 0

    if tx > 2 and i == len(li) - 1:
        print(f"the minimum money today: {min}")

         