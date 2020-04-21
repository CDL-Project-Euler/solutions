#I determined that 7* 9! = 2540160 is the maximum I need to check
def sum_digit_power(power: int):
    '''Returns the sum of all numbers which the sum of the powers of their digits = number. Note:Checks beneath a max'''
    sums = -1 #doesn't count 1
    for number in range(354924):
        if sum(map(lambda x: int(x)**power, str(number))) == number:
            sums += number
    return(sums)

if __name__ == "__main__":
    print(sum_digit_power(5))