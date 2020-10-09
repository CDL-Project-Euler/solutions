from itertools import combinations, permutations

def primes_sieve2(limit): #found on stack overflow ;)
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

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

def concats_are_prime(prime_set):
    for x,y in permutations(prime_set, r= 2):
        if not (checkprime(int(str(x)+str(y)))):
            return False
    return True

def last_is_concatprime(prime_set):
    for x in prime_set[:-1]:
        if not (checkprime(int(str(x)+str(prime_set[-1]))) or checkprime(int(str(prime_set[-1])+str(x)))):
            return False
    return True

def concat_prime_pair(num_primes, max_search: int):
    primes = [[prime] for prime in primes_sieve2(max_search)]
    if num_primes == 1:
        return primes
    # if num_primes > 1:
    list_prime_concats = []
    for prime_set in concat_prime_pair(num_primes - 1, 1000):
        for index in range(len(primes)):
            if primes[index][0] < prime_set[-1] and last_is_concatprime(prime_set + [primes[index][0]]):
                list_prime_concats.append(prime_set + [primes[index][0]])
    print(num_primes)
    return list_prime_concats

def min_list_sum(list_of_lists):
    return min(map(sum, list_of_lists))

# def concat_prime_pair(num_primes, max_search: int, start_search: int):
#     primes = [prime for prime in primes_sieve2(max_search)]
#     min_sum = 10 ** 10
#     lists = []
#     for index in range(primes.index(start_search), len(primes)):
#         print(primes[index])
#         for prime_set in combinations(primes[:index], r = (num_primes - 1)):
#             prime_set = list(prime_set)
#             prime_set.append(primes[index])

#             if sum(prime_set) < 1000000000000 and sum(prime_set) > 0 and concats_are_prime(prime_set):
#                 min_sum = sum(prime_set)
#                 print(prime_set)
#                 lists.append(prime_set)
#     print(lists)
#     return min_sum

if __name__ == "__main__":
    num_primes = 4
    #primes = [prime for prime in primes_sieve2(max_search)]
    #for prime in primes

    print(concat_prime_pair(num_primes, 1000))
# 4 solved
# 1031 is top searched for 5
    