def sum_under_x(n,x):
    '''Find the sum of all the multiples of n below x.'''
    sumofn = 0
    i = 1
    while n * i < x:
        sumofn += n * i
        i += 1
        
    return sumofn

def problem1():
    return sum_under_x(3,1000) + sum_under_x(5,1000) - sum_under_x(15,1000)

print(problem1())