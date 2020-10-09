def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

def quadratic_primes(maximum: int):
    #n2+an+b , where |a|<maximum and |b|≤maximum and a,b are even
    #makes maximum odd so that it can only look at multiples of 2s
    maximum += 1 + maximum%2
    current_max = 0
    max_a = 0
    max_b = 0

    for a in range(-maximum, maximum + 1, 2):
        for b in range(1, maximum + 1, 2):
            n= 0            
            while (n + 1) ** 2 + a*(n + 1) + b > 1 :
                if checkprime((n) ** 2 + a*(n) + b):
                    if n > current_max:
                        max_a, max_b = a,b
                        current_max = n
                    n += 1
                else:
                    break
    return max_a, max_b, current_max


if __name__ == "__main__":
    a, b, maxim = quadratic_primes(1000)
    print(a,b, maxim)
    print(a*b)