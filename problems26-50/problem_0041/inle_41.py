def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

def loop_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in loop_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def list_to_decimal(list_number: list):
    #Converts a list to decimal
    number = 0
    length = len(list_number)
    for index in range(length):
        number += 10**(length-1-index) * list_number[index]
    return number

def pandigital_primes(digits = [9,8,7,6,5,4,3,2,1]):
    #Returns the largest n-pandigital prime that exists
    pandigital_prime_list = []
    for n in range(len(digits)):
        n_digits = digits[n:]
        for n_pandigit in loop_perms(n_digits):
            if checkprime(list_to_decimal(n_pandigit)):
                pandigital_prime_list.append(list_to_decimal(n_pandigit))
    return(max(pandigital_prime_list))
    


if __name__ == "__main__":
    print(pandigital_primes())
    
    
                                        
