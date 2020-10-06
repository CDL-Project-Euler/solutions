limit = 600851475143
num = 1

def composite_check(x):
    f = 2
    composite = False
    while f < x-1 and composite == False:
        if x % f == 0:
            composite = True
        elif x % f > 0:
            f += 1
    if composite == True:
        return True
    elif composite == False:
        return False

 
while num < limit:
    if limit % num == 0 and composite_check(num) == False:
        prime_factor = num
    num += 1
    print(num)

print(prime_factor)

