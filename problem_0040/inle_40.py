import math

def champernowne_at_x(x:int):
    digits = 1
    n_max = 0
    while True:
        n_max += (digits - 1) * 9 * 10 ** (digits-2)
        if x > n_max and x <= n_max + digits * 9 * 10 ** (digits -1):
            x -= n_max
            number = 10**(digits-1) + math.ceil(x/digits) -1
            digit = int((x-1) % digits)
            return int(str(number)[digit])
        digits += 1
    
if __name__ == "__main__":
    prod_champs = 1
    for power in range(7):
        prod_champs *= champernowne_at_x(10**power)
    print(prod_champs)