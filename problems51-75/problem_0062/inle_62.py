def cube_permutations(lim_perms: int):
    """Find the smallest cube for which exactly lim_perms permutations of its digits are cube."""
    base = 1
    while True:
        cube = base ** 3
        perm_count = 1
        limit = 10 ** len(str(cube))
        comp_base = base + 1
        while comp_base ** 3 < limit: #Checks against all greater cubes with the same number of digits
            if is_permutation(comp_base ** 3, cube):
                perm_count += 1
            comp_base += 1
            #print("Comp:",comp_base)
        if perm_count >= lim_perms:
            return cube
        base += 1
        print(base)

def is_permutation(num1, num2:int):
    '''Checks through digits to see if numbers are permutations'''
    num1, num2 = str(num1), str(num2)
    # if len(num1) != len(num2):
    #     return False

    for digit in str(num1):
        if digit in num2:
            num2 = num2.replace(digit, "", 1)
            num1 = num1[1:]
        else:
            return False
    return True

        

if __name__ == "__main__":
    print(cube_permutations(5))