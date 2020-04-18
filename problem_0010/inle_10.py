def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True


def sum_primes_under(n: int):
    num = 2
    sum = 0
    while num < n:
        if checkprime(num):
            sum += num
            print(sum)
        num += 1
    return(sum)

if __name__ == "__main__":
    print(sum_primes_under(10))