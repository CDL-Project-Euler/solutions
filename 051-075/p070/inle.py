def totient(n: int, primes_n: list) -> float:
    tot = n
    for prime in primes_n:
        tot *= 1 - 1/prime
    return tot

def problem_70(limit: int) -> int:
    arr = [i for i in range(2, limit)] # Stores totient of integers from 2 - limit-1 inclusive

    for i in range(2, limit): # Index is i - 2
        if arr[i - 2] == i: # If prime, multiplies by 1 - 1/prime
            for m in range(i - 2, len(arr), i):
                arr[m] = arr[m] - arr[m] // i # Integer division speeds up


    min_ratio = limit + 1
    min_value = None

    for i in range(2, limit):
        if sorted([d for d in str(i)]) == sorted([d for d in str(arr[i-2])]) and i / arr[i-2] < min_ratio:
            print(i, arr[i-2])
            min_value = i

    return min_value, arr[min_value-2]


if __name__ == "__main__":
    print(problem_70(10000000))