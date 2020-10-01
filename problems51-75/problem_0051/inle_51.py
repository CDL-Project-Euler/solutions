import itertools as it
def prime_dig(fam_size: int):
    '''Find the smallest prime which, 
    by replacing part of the number (not necessarily adjacent digits) with the same digit, 
    is part of an eight prime value family.
    '''
    digs = 2 # The digit length of the tested family
    not_found = True
    while not_found:
        for k in range(1, digs): #the number of replacement digits
            print(k, digs)
            for blanks in it.combinations(list(range(digs-1)), k): #Positions of blanks
                for non_fillers in it.product([0,1,2,3,4,5,6,7,8,9], repeat= digs-1-k):
                    if (non_fillers and non_fillers[0] != 0) or blanks[0] == 0:
                        for end in [1, 3, 7, 9]: #last digit
                            fam = 0
                            fam_group = []
                            for filler in [0,1,2,3,4,5,6,7,8,9]:
                                if blanks[0] != 0 or filler != 0:
                                    n = list(non_fillers)
                                    for pos in blanks:
                                        n.insert(pos, filler)
                                    n = 10 * list_to_int(n) + end
                                    
                                    if checkprime(n):
                                        fam += 1
                                        fam_group.append(n)
                                        if fam >= fam_size:
                                            x= 5
                                            print(n, blanks, fam_size, digs, non_fillers, k, fam_group)
                                            not_found = False
        digs += 1

def list_to_int(digits):
    return int(''.join(map(str, digits)))

def checkprime(value: int):
    factor = 2
    sqrt = value ** 0.5
    while factor <= sqrt:
        if value % factor == 0:
            return False
        factor += 1
    return True

if __name__ == "__main__":
    prime_dig(8)