# This function is a remnant of a failed attempt (I might use it later)
# def smallest_factor(number: int):
#     for factor in range(2, int((number)**0.5+1)):
#         if number % factor == 0:    
#             return(factor)
#     #if there is no factor, it is prime
#     return number

def num_factors(n: int):
    '''The number of factors of n'''
    count = 0
    factor = 1
    max_search = n
    while factor < max_search:
        if n % factor == 0:
            if factor ** 2 == n:
                count += 1
                return count
            count += 2
            max_search = n/factor
        factor += 1
    return count

def triang_num_div(num_divs: int):
    '''The first triangle number to have num_divs divisors'''
    index = 28
    while True:
        print(index)
        triang = index * (index + 1)/2
        if num_factors(triang) >= num_divs:
            return triang
        index += 1

if __name__ == "__main__":
    print(triang_num_div(500))