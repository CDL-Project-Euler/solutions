def prime_sieve(maximum) -> list:
    """Return a list of primes < maximum."""
    maximum = int(maximum)
    prime_list = []
    primalities = [1] * maximum
    for i in range(2, maximum):
        if primalities[i]:
            prime_list.append(i)
            for j in range(i, len(primalities), i):
                primalities[j] = 0
    return prime_list


def solve(maximum):
    """Solve project euler problem 87 for numbers < maximum."""
    primes = prime_sieve(maximum ** 0.5 + 10)
    power_trips = set()
    i = 0
    while (i4 := primes[i] ** 4) < maximum:
        j = 0
        while i4 + (j3 := primes[j] ** 3) < maximum:
            k = 0
            while i4 + j3 + (k2 := primes[k] ** 2) < maximum:
                power_trips.add(i4 + j3 + k2)
                k += 1
            j += 1
        i += 1
    print(len(power_trips))

if __name__ == "__main__":
    solve(50000000)