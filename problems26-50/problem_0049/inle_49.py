def are_permutations(permutations: list):
    length = len(str(permutations[0]))
    for item in range(len(permutations)):
        permutations[item] = str(permutations[item])
        if len(permutations[item]) != length:
            return False

        for digit in permutations[item]:
            if not digit in permutations[0] or permutations[item].count(digit) != permutations[0].count(digit):
                return False
    return True

def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

def prime_permutations():
    for number in range(1000,9999):
        for integer in range(1, (10000 - number)//2 + 1):
            if checkprime(number) and are_permutations([number, number + integer, number + 2* integer]) and checkprime(number + integer) and checkprime(number + 2* integer):
                print(number, number + integer, number + 2* integer)

if __name__ == "__main__":
    prime_permutations()