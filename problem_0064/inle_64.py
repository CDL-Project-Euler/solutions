#How many continued fractions for N≤10000 have an odd period?

def sqrt_period(x:int):
    a = (x**0.5)//1
    d = 1
    period = 0
    while True:
        if d == x-a**2: # if the denomenator of the new fraction is 1, 1 period has finished
                    return period+1
        d = (x-a**2)/d
        a = d*((x**0.5+a)//d)-a
        period += 1

def problem64(max: int):
    '''Returns num of odd period continued fractions. max included'''
    count = 0
    for x in range(1, max+1):
        if x**0.5 != (x**0.5)//1 and sqrt_period(x)%2 == 1:
            count += 1
    return count

if __name__ == "__main__":
    print(problem64(10000))