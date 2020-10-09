import itertools

def list_to_decimal(list_number):
    #Converts a list to decimal
    number = 0
    length = len(list_number)
    for index in range(length):
        number += 10**(length-1-index) * int(list_number[index])
    return number

def sub_string_divisibility():
    primes = [2,3,5,7,11,13,17]
    sum_pandigitals = 0
    for pandigital in itertools.permutations("0123456789"):
        is_sub_div = True
        for digit in range(7):
            if not list_to_decimal(pandigital[digit+1:digit+4]) % primes[digit] == 0:
                is_sub_div = False
                break
        if is_sub_div:
            print(pandigital)
            sum_pandigitals += list_to_decimal(pandigital)
    return sum_pandigitals

if __name__ == "__main__":
    print(sub_string_divisibility())