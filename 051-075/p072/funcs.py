# Contains functions that Inle explored for this problem

def euclidean_gcf(m: int, n: int) -> int:
    '''extended euclidean algorithm to find gcd'''
    while (remainder := m % n) != 0:
        m, n, remainder = n, remainder, n % remainder
    return m

def prime_factorization(n: int, primes: list) -> list:
    # returns a list of the primes which divide n
    sqrt_n = n ** 0.5
    i = 2
    while primes[i] <= n ** 0.5:

        if n % primes[i] == 0:
            n /= primes
        while n 
        i += 1

def erastosthenes_sieve(limit: int) -> list:
    nums = [1] * limit
    nums[2] = 1
    for i in range(2, limit):
        if nums[i] != 0:
            for j in range(i, limit, i):
                nums[j] = 0
        yield i

def count_proper_factors(n: int) -> int:
    ''' Counts the proper factors of n '''
    count = 1 # assumes 1 is proper factor
    for i in range(2, n):
        if gcf(i, n) == 1:
            count += 1
    return count


def problem_72(limit: int):
    total = 0
    for num in range(2, limit + 1):
        print(num)
        total += count_proper_factors(num)
    return total

if __name__ == "__main__":
    for i in erastosthenes_sieve():
    # print(problem_72(10000))
