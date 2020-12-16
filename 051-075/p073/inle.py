import math

def euclidean_gcf(m: int, n: int) -> int:
    '''extended euclidean algorithm to find gcd, m > n'''
    while (remainder := m % n) != 0:
        m, n, remainder = n, remainder, n % remainder
    return n

def problem_73(limit: int):
    total = 0
    for num in range(4, limit + 1):
        print(num)
        for i in range(math.ceil(num/3), num // 2 + 1):
            if euclidean_gcf(num, i) == 1:
                total += 1
    return total

print(problem_73(12000))