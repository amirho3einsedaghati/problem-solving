# Palindrome(yani az do sar): 
# tarif: age az do sare yek ebarat harekat konim va be yek chiz beresim, mitavan goft an ebarat(yani oon reshte, oon list); yek palindrome ast.

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

# print(is_palindrome('wassaw'))
# print(is_palindrome("abcddcbd"))

# ------------------------------------
# baraye maghloob kardan(ya invert kardan) yek reshte ya list, mitavan az dastresi be item az tarighe index estefade kard.
# string= "amiimd"
# invert= string[::-1]
# print(invert)

# li= [12,4,5,12,6,12]
# invert_li= li[::-1]
# print(invert_li)
# print(li[1:4:])