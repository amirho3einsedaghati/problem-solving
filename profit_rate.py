'''
Suppose you have $<money amount of invested>, which you can invest with a 10% return each year. 
After one year, it's <money amount of invested> * 1.1= X dollars, and after two years it's <money amount of invested> * 1.1 * 1.1= X $. 
Add code to calculate how much money you end up with after n years, and print the result.

'''
#================================== functions ====================
def money_investing():
    money= input("how much money do you want to invest? ")
    try:
        money= int(money)
    except:
        money= money_investing()
    else:
        return money
    finally:
        return money

#-----------------------
def investing_years():
    year= input("how many years do you want to invest your money? ")
    try:
        year= int(year)
    except:
        year= investing_years()
    else:
        return year
    finally:
        return year
    
#================================== declaration ====================
invested_money= money_investing()
n_year= investing_years()

#================================== operations ====================
total_money= 0

for i in range(0, n_year):
    exponen_val= i + 1
    profit_rate= 1.1 ** exponen_val
    total_money= invested_money * profit_rate

print(f"your money amount after {n_year} years is: {total_money.__round__(4)}")
print(f"your pure profit is: {(total_money - invested_money).__round__(4)}")