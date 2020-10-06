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

def concat_prime_pair(num_primes, max_search: int, start_search: int):
    primes =[x for x in primes_sieve2(max_search)]

    for index in range(primes.index(start_search), 10**10):
        print(primes[index])
        for prime_set in combinations(primes[:index], r= (num_primes - 1)):
            prime_set = list(prime_set)
            prime_set.append(primes[index])
            if sum(prime_set) > 729:
                concats_are_prime = True
                for x,y in permutations(prime_set, r= 2):
                    if not (checkprime(int(str(x)+str(y)))):
                        concats_are_prime = False
                        break

                if concats_are_prime:
                    print(prime_set)




if __name__ == "__main__":
    num_primes = 3
    max_search = 10000
    print(concat_prime_pair(num_primes,500, 2))
# 761 is top searched for 4
#733 is top searched for 5
    