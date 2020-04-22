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

def list_to_decimal(list_number: list):
    #Converts a list to decimal
    number = 0
    length = len(list_number)
    for index in range(length):
        number += 10**(length-1-index) * int(list_number[index])
    return number

def circulations(string):
    for index in range(len(string)):
        yield (string[index:] + string[:index])

def circular_primes(threshold: int):
    #Counts circular primes below a threshold
    count = 0
    for n in range(2, threshold):
        is_circular = True
        for n_circular in circulations(str(n)):
            if not(checkprime(list_to_decimal(n_circular))):
                is_circular = False
                break
        if is_circular:
            print(n)
            count += 1
    return(count)
    


if __name__ == "__main__":
    maximum = 1000000
    print(circular_primes(maximum), "circular primes below", maximum)

