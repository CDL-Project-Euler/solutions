def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

def spiral_primes():
    #Checks through the spiral and counts the ratio of corners that are primes
    increment = 2
    corner_value = 1
    prime_count = 0

    while True:
        for corner in range(1,5):
            if checkprime(corner_value + corner * increment):
                prime_count += 1

        ratio = prime_count/(2* increment + 1)
        if ratio < 0.1 :
            return increment + 1

        corner_value += 4 * increment
        increment += 2

if __name__ == "__main__":
    print(spiral_primes())