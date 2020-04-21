#Largest product of 3 digit numbers is 999*999=998001
#I assume answer in form abccba
import math
def problem4():
    palindrome = 0
    for x in range(100,999):
        for y in range(100,999):
            if ispalindrome(x * y) and palindrome < x*y:
                palindrome = x*y
    return(palindrome)

def ispalindrome(product):
    if product//100000 == product%10 and (product//10000)%10 == (product%100)//10 and (product//1000)%10 == (product%1000)//100:
        return True
    return False

print(problem4())
