def pow_digit_sum(base: int, power: int):
    string = str(base**power)
    sum_digs = 0
    for digit in string:
        sum_digs += int(digit)
    return sum_digs

if __name__ == "__main__":
    print(pow_digit_sum(2,1000))