# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def checkprime(value: int):
    if value == 0 or value == 1:
        return False

    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

def consecutive_prime_sum(maximum):
    longest_length = 0
    longest = 0

    for start in range(1, maximum):
        prime_sum = 0
        count = 0
        if checkprime(start):
            for number in range(start,maximum):
                if checkprime(number):
                    prime_sum += number
                    count += 1
                    
                    if prime_sum > maximum:
                        break

                    if count > longest_length and checkprime(prime_sum):

                        longest_length = count
                        longest = prime_sum
    return longest


if __name__ == "__main__":
    print(consecutive_prime_sum(1000000))