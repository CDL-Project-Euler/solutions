def count_prime_factors(variable: int):
    '''Returns the number of prime factors a number has'''
    count = 0
    while variable != 1:
        for factor in range(2, variable + 1):
            if variable % factor == 0:
                count += 1
                variable = variable // factor
                break  
    return count

def problem_708(maximum: int, minimum = 1):
    sum_numbs = 0
    for n in range(minimum, maximum + 1):
        sum_numbs += 2**count_prime_factors(n)
    return int(sum_numbs)

if __name__ == "__main__":
    print(problem_708(20**4))

