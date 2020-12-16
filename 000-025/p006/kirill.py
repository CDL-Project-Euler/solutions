def problem_6(num: int):
    '''Finds the difference between square of sums and sum of squares for series of 1 to a num'''
    result = sqr_sum(num) - sum_sqr(num)
    return result

def sum_sqr(argument):
    result = 0
    for i in range(argument + 1):
        result += i ** 2
    return result

def sqr_sum(argument):
    result = ((argument/2) * argument + (argument/2)) ** 2 #Calculating square of sum by adding the number in order (e.g. 1+9, 8+2, 7+3 etc)
    return result

if __name__ == "__main__":
    print(problem_6(100))