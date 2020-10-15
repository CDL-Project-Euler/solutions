from itertools import combinations, permutations

def primes_sieve2(limit): #found on stack overflow ;)
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False                         #0 and 1 are false

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

def first_is_concatprime(prime_set):
    for x in prime_set[:-1]:
        if not(checkprime(int(str(x)+str(prime_set[-1]))) and checkprime(int(str(prime_set[-1])+str(x)))):
            return False
    return True

def concat_prime_pair(num_primes, max_search: int):
    primes = [[prime] for prime in primes_sieve2(max_search)]
    if num_primes == 1:
        return primes
    # if num_primes > 1:
    list_prime_concats = []
    for prime_set in concat_prime_pair(num_primes - 1, 10000):
        for index in range(len(primes)):
            if primes[index][0] > prime_set[-1] and first_is_concatprime(prime_set + [primes[index][0]]):
                list_prime_concats.append(prime_set + [primes[index][0]])
    print(num_primes)
    return list_prime_concats

def min_list_sum(list_of_lists):
    return min(map(sum, list_of_lists))

if __name__ == "__main__":
    num_primes = 5

    print(concat_prime_pair(num_primes, 500000))
# 4 solved
# 5000 is top searched for 5
    