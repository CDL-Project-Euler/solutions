def palindrom_check(num):
    raw_list = list(str(num))
    num_list = list(map(int, raw_list))
    digits = 0

    for i in num_list:
        digits += 1

    if digits == 5:
        digit_pair_1 = (num_list[0] == num_list[-1])
        digit_pair_2 = (num_list[1] == num_list[-2])

        if digit_pair_1 == digit_pair_2 == True:
            return True
        else:
            return False
    elif digits == 6:
        digit_pair_1 = (num_list[0] == num_list[-1])
        digit_pair_2 = (num_list[1] == num_list[-2])
        digit_pair_3 = (num_list[2] == num_list[-3])

        if digit_pair_1 == digit_pair_2 == digit_pair_3 == True:
            return True
        else:
            return False
    return output

factor1 = 99
factor2 = 100
old_palindrom = 0
while factor1 != 1000:
    factor1 += 1
    factor2 = 100
    while factor2 != 1000:
        number = factor1 * factor2
        output = palindrom_check(number)
        if output == True and old_palindrom < number:
            old_palindrom = number
            factor2 += 1
        else:
            factor2 += 1
            
print(old_palindrom)

    
