def fact_dig_sum(base: int):
    '''Find the sum of the digits in the number base!'''
    factorial = 1

    for number in range(1, base + 1):
        factorial *= number

    sum = 0
    for dig in str(int(factorial)):
        sum += int(dig)
    return sum

if __name__ == "__main__":
    print(fact_dig_sum(100))