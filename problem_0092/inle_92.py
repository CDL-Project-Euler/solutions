from math import log
from time import perf_counter

def length_num_digits(number: int):
    return(int(log(number, 10))+1)

def sum_digit_chain(number: int):
    '''Returns whether by repeating the sum of the squares of the digits. Reaches 1 or 89'''
    while True:
        if number == 1:
            return 1
        elif number == 89:
            return 89

        number = sum(map(lambda x: int(x)**2, str(number)))

def digit_square(stop: int):
    count = 0
    integer_ends = []
    for integer in range(1,81*length_num_digits(stop)):
        integer_ends.append(sum_digit_chain(integer))
        if integer_ends[integer-1] == 89:
            count += 1

    for number in range(81*length_num_digits(stop), stop):
        if integer_ends[sum(map(lambda x: int(x)**2, str(number)))-1] == 89:
            count += 1
    return count

if __name__ == "__main__":
    start = perf_counter()
    print(digit_square(10000000))
    middle = perf_counter()
    print(middle-start, " seconds")
