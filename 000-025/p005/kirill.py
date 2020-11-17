def problem_5(maximum: int, max_factor: int) -> int:
    '''Smallest multiple of natural numbers from 1 to "max_factor" for 1 to maximum'''
    for number in range(max_factor, maximum):
        #print(number , even_division(number, max_factor) == True)
        if even_division(number, max_factor) == True:
            answer = number
            break
    return answer

def even_division(number, max_factor):
    '''Returns boolean if the number is evenly divisible by natural numbers from 1 to "max_factor"'''
    ###Dirty option:
    checking_list = []
    for factor in range(1, (max_factor+1)):
        truth_element = (number % factor) == 0
        checking_list.append(truth_element)
    for element in checking_list:
        if element == False:
            return False
    return True

    ###Clean option:
    # for factor in range(1, max_factor + 1):
    #     if number % factor != 0:
    #         return False
    # return True
            
    

if __name__ == "__main__":
    print(problem_5(10000000000,20))  