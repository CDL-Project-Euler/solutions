def max_triplet_sum(maximum: int):
    '''Returns the number which is the perimeter of the most pythagorean triplet.
    Maximum included
    '''
    most = 0
    most_solutions = 0

    for num in range(maximum + 1):
        sol_count = 0
        for a in range(1,num):
            for b in range(1,num):
                if num == a + b + (a**2 + b**2)**0.5:
                    sol_count += 1
        if most_solutions < sol_count/2:
            print(num, ":", sol_count/2)
            most = num
            most_solutions = sol_count/2
    return most

if __name__ == "__main__":
    print(max_triplet_sum(1000))