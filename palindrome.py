# Palindrome(yani az do sar): 
# tarif: age az do sare yek ebarat harekat konim va be yek chiz beresim, mitavan goft an ebarat(yani oon reshte, oon list); yek palindrome ast.

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

# print(is_palindrome('wassaw'))
# print(is_palindrome("abcddcbd"))


