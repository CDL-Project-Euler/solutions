def checkprime(value: int):
    if value == 1:
        return False
    
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True


def check_truncatable(n: int):
    #left
    for x in range(1,len(str(n))):
        if not checkprime(int(str(n)[:-x])):
            return False
    #right
    for x in range(1, len(str(n))):
        if not checkprime(int(str(n)[-x:])):
            return False

    return True

def truncatable_primes():
    count = 0
    sum_primes = 0
    for n in range (11, 10000000000,2):
        if checkprime(n):
            if check_truncatable(n):
                print(n)
                count += 1
                sum_primes += n
                if count == 11:
                    return(sum_primes)

if __name__ == "__main__":
    print(truncatable_primes())