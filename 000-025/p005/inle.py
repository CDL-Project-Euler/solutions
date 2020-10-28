def slow_lcm(maximum: int)-> int:
    '''lowest common multiple of natural numbers from 1 to maximum'''
    i = maximum
    while True:
        divisible = True
        for num in range(1, maximum + 1):
            if maximum % num != 0:
                divisible = False
                break
        if divisible:
            return maximum
        maximum += 1

def fast_lcm(factors: list, lcm = 1) -> int:
    '''Least common multiple of integers in list, multiplied by lcm'''
    if len(factors) == 1: 
        return lcm * factors[0]
    #Iterates function with cutting down 
    return fast_lcm(
                    [item/factors[0] * (not bool(item%factors[0])) + item * bool(item%factors[0]) for item in factors[1:]],
                    lcm * factors[0]
                    )

print(slow_lcm(10))
print(fast_lcm(list(range(1,20))))