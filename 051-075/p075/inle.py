from math import floor

def euclidean_gcf(m: int, n: int) -> int:
    '''extended euclidean algorithm to find gcf, m > n'''
    while (remainder := m % n) != 0:
        m, n, remainder = n, remainder, n % remainder
    return n


def problem_75(limit: int) -> int:

    arr = [0] * (limit + 1)
    for m in range(3, limit):
        for n in range(2, m):
            if (perimeter := 2 * m * m + 2 * m * n) > limit:
                break
            if euclidean_gcf(m, n) == 1:
                for k in range(1, floor(limit / perimeter) + 1):
                    arr[k * perimeter] += 1
    return arr

print(problem_75(48))