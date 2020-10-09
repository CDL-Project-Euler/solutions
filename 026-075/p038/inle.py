#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

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

def concat_prod(n: int, length: int):
    total = ""
    for integer in range(1, 100):
        total += str(n*integer) 
        if len(total) > length:
            return total.replace(str(n*integer),"")



def pandigital_multiples():
    largest = 0
    for number in range(9876):
        pandigit = concat_prod(number, 9)
        if len(pandigit) == 9 and int(pandigit) > largest and are_pandigital([int(pandigit)]):
            largest = int(pandigit)
    return largest

if __name__ == "__main__":
    print(pandigital_multiples())