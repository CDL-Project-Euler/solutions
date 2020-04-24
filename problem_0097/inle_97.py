def non_mersenne_prime(exponent:int):
    "last 10 digits of this non mersenne prime"
    power = 1
    for _ in range(exponent):
        power = (power * 256) % (10**11)

    return (2*power*28433+1) % (10 ** 10)

if __name__ == "__main__":
    print(non_mersenne_prime(978807))