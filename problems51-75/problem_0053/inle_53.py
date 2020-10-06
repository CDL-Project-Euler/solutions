def combinations(n: int, r : int):
    """Gives the number of possibilities of n objects chosen r times, order matters"""
    product = 1
    for i in range(n - r + 1, n + 1):
        product *= i
    for x in range(2, r+1):
        product /= x
    return product

def perm_greater_than(minimum: int):
    count = 0
    for n in range(21,101):
        for r in range(n):
            if combinations(n,r) > minimum:
                print(n,r,combinations(n,r))
                count += 1
    return count

if __name__ == "__main__":
    print(combinations(21,5))
    print(perm_greater_than(1000000))
