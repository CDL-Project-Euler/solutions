def are_permutations(number_list: list, digits):
    #Checks through numbers in list to see if they are permutations
    length_digits = len(str(digits))

    for number in number_list:
        if len(str(number)) != length_digits:
            return False

        digits_copy = str(digits)
        for digit in str(number):
            if digit in digits_copy:
                digits_copy = digits_copy.replace(digit, "", 1)
            else:
                return False

    return True

def permuted_multiples(top_multiple: int):
    integer = 1
    while True:
        if are_permutations([integer * x for x in range(2,top_multiple + 1)], str(integer)):
            return integer
        integer += 1

if __name__ == "__main__":
    print(permuted_multiples(6))

#interrestingly 142857 = 999999/7