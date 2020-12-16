def problem_7(num: int):
    '''Finds a largest prime between 2 and n'''
    return eratosthenes_sieve(num)

def eratosthenes_sieve(argument: int):
    number_set = list(range(2, argument + 1))
    prime_set = list()
    
    for f in number_set:
        p = f
        for i in number_set:
            if i % p != 0 and i == p:
                prime_set.append(p)
    return prime_set[-1]
    


if __name__ == "__main__":
    print(problem_7(10001))