# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#At most 1 number can be 4 digits, so only look at up to 9876

def are_pandigital(number_list: list, digits = "123456789"):
    #Checks through numbers in list to see if they are pandigital
    total_length = 0
    length_digits = len(digits)

    for number in number_list:
        total_length += len(str(number))
        for digit in str(number):
            if digit in digits:
                digits = digits.replace(digit, "")
            else:
                return False
    if total_length != length_digits:
        return False
    return True

def problem_32():
    product_list = []
    for a in range(9876):
        for b in range (a + 1, 9876):
            product = a*b
            if are_pandigital([a,b,product]):
                print(a,b,product)
                if not product in product_list:
                    product_list.append(product)
    return(sum(product_list))

if __name__ == "__main__":
    print(problem_32())