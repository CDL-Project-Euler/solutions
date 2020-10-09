#I determined that 7* 9! = 2540160 is the maximum I need to check
def sum_digit_factorials():
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    sums = -3 #doesn't count 1 and 2
    for number in range(2540160):
        if sum(map(lambda x: factorials[int(x)], str(number))) == number:
            sums += number
    return(sums)

if __name__ == "__main__":
    print(sum_digit_factorials())