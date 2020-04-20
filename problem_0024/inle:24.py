# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



def permutations(n: int, r : int):
    """Gives the number of possibilities of n objects chosen r times, order matters"""
    product = 1
    for i in range(n - r + 1, n + 1):
        product *= i
    return product


def nth_perm(n: int, digits =  "0123456789"):
    nth_perm = ""
    length = len(digits)
    n = n-1
    for perm_digit in range(1, length + 1):
        perm = permutations(length - perm_digit, length - perm_digit)
        nth_perm = nth_perm + digits[n//perm]
        digits = digits[:n//perm] + digits[n//perm+1:]
        n -= perm * (n//perm)
    return nth_perm

if __name__ == "__main__":
    print(nth_perm(1000000))