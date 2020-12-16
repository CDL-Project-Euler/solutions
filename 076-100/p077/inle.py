import copy

def erastosthenes_sieve(limit: int) -> list:
    nums = [1] * limit
    nums[2] = 1
    primes = []
    for i in range(2, limit):
        if nums[i] != 0:
            for j in range(i, limit, i):
                nums[j] = 0
            primes.append(i)
    return primes


def problem_77(limit: int, search_limit = 100):
    primes = erastosthenes_sieve(search_limit)
    sum_ways = [0] * search_limit
    sum_ways[0] = 1
    temp_ways = copy.copy(sum_ways)
    for prime in primes: # Loops through primes
        for multiple in range(prime, len(sum_ways), prime): # Loops through multiples of primes
            for i in range(0, len(sum_ways) - multiple): # Adds paths for each path
                temp_ways[multiple + i] += sum_ways[i]
        sum_ways = copy.copy(temp_ways)
    
    for i in range(len(sum_ways)): # Checks for first under limit
        if sum_ways[i] > limit:
            return i, sum_ways[i]


print(problem_77(5000))